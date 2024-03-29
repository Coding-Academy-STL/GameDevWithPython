import pygame, sys
import math
from pygame.locals import *

pygame.init()

# Background color (R, G, B)
BACKGROUND = (255, 255, 255)

GAME_STATE_MENU = 0
GAME_STATE_PLAY = 1
GAME_STATE_END = 2

gameState = GAME_STATE_MENU

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

# The maximum angle the ball can bounce off the paddle at
MAX_ANGLE = math.radians(50)

SCREEN_MIDDLE = [WINDOW_WIDTH / 2.0, WINDOW_HEIGHT / 2.0]

PADDLE_TO_SCREEN_DISTANCE = 20  # Distance from the edge of the paddles to the closest vertical edge of the screen

SCORE_OFFSET = 25

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Game!")

# create the font that we will be using
# font = pygame.font.Font(os.path.abspath(os.path.dirname(__file__)) + "/PressStart2P-Regular.ttf", 32)

font = pygame.font.SysFont(pygame.font.get_default_font(), 32)

titleFont = pygame.font.SysFont(pygame.font.get_default_font(), 64)


def draw_text(text: str, color, center, useFont=font):
    text = useFont.render(text, True, color)

    WINDOW.blit(
        text, [center[0] - text.get_width() / 2, center[1] - text.get_height() / 2]
    )


def draw_center_dashed_line(num_dashes, color):
    divisions = num_dashes * 2 - 1  # the number of spaces + number of lines

    division_width = WINDOW_WIDTH / divisions  # width of each division

    x_off = 0
    while x_off < WINDOW_WIDTH:
        pygame.draw.line(
            WINDOW,
            color,
            (x_off, SCREEN_MIDDLE[1]),
            (x_off + division_width, SCREEN_MIDDLE[1]),
        )

        x_off += division_width * 2


class Paddle:
    def __init__(self, pos, dimensions, color, speed, leftKey, rightKey):
        self.pos = pos  # An array [x, y]
        self.dimensions = dimensions  # An array [width, height]
        self.color = color  # An array [R, G, B]
        self.speed = speed  # A number (how fast the paddle moves)
        self.leftKey = leftKey  # The key you want to make the paddle go left (eg K_a)
        self.rightKey = (
            rightKey  # The key you want to make the paddle go right (eg K_d)
        )

    def update(self, ai=False, overrideLeft=False, overrideRight=False):
        if (ai and overrideLeft) or (not ai and pygame.key.get_pressed()[self.leftKey]):
            self.pos[0] -= self.speed
        if (ai and overrideRight) or (
            not ai and pygame.key.get_pressed()[self.rightKey]
        ):
            self.pos[0] += self.speed

        if self.pos[0] < 0:
            self.pos[0] = 0
        if self.pos[0] > WINDOW_WIDTH - self.dimensions[0]:
            self.pos[0] = WINDOW_WIDTH - self.dimensions[0]

    def draw(self):
        pygame.draw.rect(
            WINDOW,
            self.color,
            (self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[1]),
        )


class Ball:
    def __init__(self, pos, radius, color, velocity):
        self.pos = pos  # array [x, y]
        self.radius = radius  # number
        self.color = color  # array [r, g, b]
        self.velocity = velocity  # array [vx, vy]
        self.initial_velocity = velocity
        self.score = [0, 0]

    def update(self):
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        # Check for collisisons

        if self.pos[0] - self.radius < 0:  # Collided with the left wall
            self.pos[0] = self.radius
            self.velocity[
                0
            ] *= (
                -1
            )  # Key moving with the same vertical speed, change directions horizontally

        elif self.pos[0] + self.radius > WINDOW_WIDTH:  # Collided with the right wall
            self.pos[0] = WINDOW_WIDTH - self.radius
            self.velocity[0] *= -1

        elif self.pos[1] - self.radius < 0:  # Top wall
            self.pos = SCREEN_MIDDLE.copy()
            self.velocity = self.initial_velocity.copy()

            self.score[PADDLE_BOTTOM] += 1

        elif self.pos[1] + self.radius > WINDOW_HEIGHT:  # Bottom wall
            self.pos = SCREEN_MIDDLE.copy()
            self.velocity = self.initial_velocity.copy()
            self.velocity[1] *= -1

            self.score[PADDLE_TOP] += 1

    def draw(self):
        pygame.draw.circle(WINDOW, self.color, self.pos, self.radius)

    def get_speed(self):
        return math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)


# Find the distance between two points
# p1: [x, y]
# p2: [x, y]
# return: distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


PADDLE_TOP = 0
PADDLE_BOTTOM = 1


# Check if a ball and paddle are colliding
# return True if they collide
def ball_paddle_collision(ball: Ball, paddle: Paddle, which):
    # Let's make this simple:
    #    - Treat the paddle as a line

    # First, check if the ball is within the x bounds of the paddle
    if (
        ball.pos[0] + ball.radius < paddle.pos[0]
        or ball.pos[0] - ball.radius > paddle.pos[0] + paddle.dimensions[0]
    ):
        # The ball is outside of the x bounds
        return False

    # Second, check the distance of the ball's center from the edges of the paddle
    distance_left = distance(ball.pos, paddle.pos)
    distance_right = distance(
        ball.pos, [paddle.pos[0] + paddle.dimensions[0], paddle.pos[1]]
    )

    # If the distances are less than the radius of the ball, there is a collision
    if distance_left < ball.radius or distance_right < ball.radius:
        return True

    if which == PADDLE_BOTTOM:
        # Check if the Y value of the ball matches a collision
        if ball.pos[1] + ball.radius > paddle.pos[1]:
            return True
    elif which == PADDLE_TOP:
        # Check if the Y value of the ball matches a collision
        if ball.pos[1] - ball.radius < paddle.pos[1] + paddle.dimensions[1]:
            return True

    return False


# Clamp a value within a range
# For example, if your range is -1.0 < x < 1.0
# and x is -1.2, x will be clamped to -1.0
# If x is 1.2, x will be clamped to 1.0
# If x is, say, 0.2, it will remain 0.2 as it is within the range
def clamp(value, lower, upper):
    return lower if value < lower else upper if value > upper else value


def run_menu():
    global gameState
    draw_text("PONG", (0, 0, 0), SCREEN_MIDDLE, titleFont)

    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 50
    BUTTON_BOTTOM_OFF = 100

    button_rect = pygame.Rect(
        SCREEN_MIDDLE[0] - BUTTON_WIDTH / 2,
        SCREEN_MIDDLE[1] + BUTTON_BOTTOM_OFF - BUTTON_HEIGHT / 2,
        BUTTON_WIDTH,
        BUTTON_HEIGHT,
    )

    pygame.draw.rect(WINDOW, (255, 0, 255), button_rect, border_radius=10)

    draw_text(
        "play",
        (
            0,
            0,
            0,
        ),
        (SCREEN_MIDDLE[0], SCREEN_MIDDLE[1] + BUTTON_BOTTOM_OFF),
    )

    # check if the user clicks the button
    if pygame.mouse.get_pressed()[0] and button_rect.collidepoint(
        pygame.mouse.get_pos()
    ):
        gameState = GAME_STATE_PLAY


LEFT = 0
RIGHT = 1


def move_for_me(paddle: Paddle, ball: Ball):
    if ball.pos[0] < paddle.pos[0]:
        return LEFT
    else:
        return RIGHT


def run_game(paddleBottom, paddleTop, ball):
    paddleBottom.update()
    paddleBottom.draw()

    topMove = move_for_me(paddleTop, ball)
    topMoveLeft = topMove == LEFT
    topMoveRight = topMove == RIGHT
    paddleTop.update(overrideRight=topMoveRight, overrideLeft=topMoveLeft, ai=True)
    paddleTop.draw()

    ball.update()
    ball.draw()

    draw_text(
        str(ball.score[PADDLE_BOTTOM]),
        [0, 0, 0],
        (SCREEN_MIDDLE[0], SCREEN_MIDDLE[1] + SCORE_OFFSET),
    )

    draw_text(
        str(ball.score[PADDLE_TOP]),
        [0, 0, 0],
        (SCREEN_MIDDLE[0], SCREEN_MIDDLE[1] - SCORE_OFFSET),
    )

    draw_center_dashed_line(11, (0, 0, 0))

    if ball_paddle_collision(ball, paddleBottom, PADDLE_BOTTOM):
        # offset the ball such that it isn't colliding with the paddle anymore
        # this is to avoid running collision calculations for the same collision
        # multiple frames in a row
        ball.pos = [ball.pos[0], paddleBottom.pos[1] - ball.radius]

        # This is a simple collision resolution
        # ball.velocity[1] *= -1

        # But let's do some accurate Pong collision handling
        x_distance_from_paddle_center = ball.pos[0] - (
            paddleBottom.pos[0] + paddleBottom.dimensions[0] / 2.0
        )

        # Get a decimal percentage betwen -1.0 and 1.0 of how far from the center the ball is
        x_percentage = x_distance_from_paddle_center / (
            paddleBottom.dimensions[0] / 2.0
        )
        x_percentage = clamp(x_percentage, -1.0, 1.0)

        new_ball_speed = ball.get_speed() + 0.2

        # This is just right angle trig to calculate the velocity in the x and y directions given an angle (MAX_ANGLE * x_percentage)
        # and a speed (new_ball_speed). Notice that we multiply by -1 here because we want the ball to go up (which is the negative direction)
        ball.velocity = [
            new_ball_speed * math.sin(MAX_ANGLE * x_percentage),
            -1 * new_ball_speed * math.cos(MAX_ANGLE * x_percentage),
        ]

    elif ball_paddle_collision(ball, paddleTop, PADDLE_TOP):
        # Same thing as the previous if statement, but we need to keep into account that the ball will hit the bottom
        # edge of the paddle. Since we are offsetting the ball from the top edge, we need to take into account
        # the height of the paddle, hence paddleTop.dimensions[1]. Try deleting that addition and notice what happens
        ball.pos = [
            ball.pos[0],
            paddleTop.pos[1] + paddleTop.dimensions[1] + ball.radius,
        ]

        # This is a simple collision resolution
        # ball.velocity[1] *= -1

        # But let's do some accurate Pong collision handling
        x_distance_from_paddle_center = ball.pos[0] - (
            paddleTop.pos[0] + paddleTop.dimensions[0] / 2.0
        )

        # Get a decimal percentage betwen -1.0 and 1.0 of how far from the center the ball is
        x_percentage = x_distance_from_paddle_center / (paddleTop.dimensions[0] / 2.0)
        x_percentage = clamp(x_percentage, -1.0, 1.0)

        # Speed the ball up after every collision. This is optional
        new_ball_speed = ball.get_speed() + 0.2

        ball.velocity = [
            new_ball_speed * math.sin(MAX_ANGLE * x_percentage),
            new_ball_speed * math.cos(MAX_ANGLE * x_percentage),
        ]

    pass


# The main function that controls the game
def main():
    paddleBottom = Paddle(
        [100, WINDOW_HEIGHT - PADDLE_TO_SCREEN_DISTANCE - 15],
        [100, 15],
        [255, 0, 0],
        10,
        K_a,
        K_d,
    )
    paddleTop = Paddle(
        [100, PADDLE_TO_SCREEN_DISTANCE], [100, 15], [0, 0, 255], 10, K_LEFT, K_RIGHT
    )

    ball = Ball([100, 100], 10, [255, 0, 0], [2.5, 10])

    # The main game loop
    while True:
        # Get inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Render (Draw) elements of the game
        WINDOW.fill(BACKGROUND)

        if gameState == GAME_STATE_PLAY:
            run_game(paddleBottom, paddleTop, ball)
        elif gameState == GAME_STATE_MENU:
            run_menu()

        # Update the display!
        pygame.display.update()

        # Update the clock limit framerate to FPS
        fpsClock.tick(FPS)


main()
