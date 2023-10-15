import pygame, sys, random
import math
from pygame.locals import *

pygame.init()
 
# Background color (R, G, B)
BACKGROUND = (255, 255, 255)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')

class Paddle:
    def __init__(self, pos, dimensions, color, speed, leftKey, rightKey):
        self.pos = pos                    # An array [x, y]
        self.dimensions = dimensions      # An array [width, height]
        self.color = color                # An array [R, G, B]
        self.speed = speed                # A number (how fast the paddle moves)
        self.leftKey = leftKey            # The key you want to make the paddle go left (eg K_a)
        self.rightKey = rightKey          # The key you want to make the paddle go right (eg K_d)

    def update(self):
        if pygame.key.get_pressed()[self.leftKey]:
            self.pos[0] -= self.speed
        if pygame.key.get_pressed()[self.rightKey]:
            self.pos[0] += self.speed

        if self.pos[0] < 0:
            self.pos[0] = 0
        if self.pos[0] > WINDOW_WIDTH - self.dimensions[0]:
            self.pos[0] = WINDOW_WIDTH - self.dimensions[0]

    def draw(self):
        pygame.draw.rect(WINDOW, self.color, (self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[1]))

class Ball:
    def __init__(self, pos, radius, color, velocity):
        self.pos = pos             # array [x, y]
        self.radius = radius       # number
        self.color = color         # array [r, g, b]
        self.velocity = velocity   # array [vx, vy]

    def update(self):
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        # Check for collisisons

        if self.pos[0] - self.radius < 0: # Collided with the left wall
            self.pos[0] = self.radius
            self.velocity[0] *= -1 # Key moving with the same vertical speed, change directions horizontally

        elif self.pos[0] + self.radius > WINDOW_WIDTH: # Collided with the right wall
            self.pos[0] = WINDOW_WIDTH - self.radius
            self.velocity[0] *= -1

        elif self.pos[1] - self.radius < 0: # Top wall
            self.pos[1] = self.radius
            self.velocity[1] *= -1

        elif self.pos[1] + self.radius > WINDOW_HEIGHT: # Bottom wall
            self.pos[1] = WINDOW_HEIGHT - self.radius
            self.velocity[1] *= -1

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

# Check if a ball and paddle are colliding
# return True if they collide
def ball_paddle_collision(ball: Ball, paddle: Paddle):
    # Let's make this simple:
    #    - Treat the paddle as a line
    
    # First, check if the ball is within the x bounds of the paddle
    if ball.pos[0] + ball.radius < paddle.pos[0] or ball.pos[0] - ball.radius > paddle.pos[0] + paddle.dimensions[0]:
        # The ball is outside of the x bounds
        return False

    # Second, check the distance of the ball's center from the edges of the paddle
    distance_left = distance(ball.pos, paddle.pos)
    distance_right = distance(ball.pos, [paddle.pos[0] + paddle.dimensions[0], paddle.pos[1]])

    # If the distances are less than the radius of the ball, there is a collision
    if distance_left < ball.radius or distance_right < ball.radius:
        return True

    # Check if the Y value of the ball matches a collision
    if ball.pos[1] + ball.radius > paddle.pos[1]:
        return True


    return False

# Clamp a value within a range
# For example, if your range is -1.0 < x < 1.0
# and x is -1.2, x will be clamped to -1.0
# If x is 1.2, x will be clamped to 1.0
# If x is, say, 0.2, it will remain 0.2 as it is within the range
def clamp(value, lower, upper):
    return lower if value < lower else upper if value > upper else value
    

# The main function that controls the game
def main () :
  paddle = Paddle([100, 250], [100, 15], [255, 0, 0], 10, K_a, K_d)
  ball = Ball([100, 100], 10, [255, 0, 0], [2.5, 3])

  MAX_ANGLE = math.radians(50)
  # The main game loop
  while True:
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
    
 
    # Render (Draw) elements of the game
    WINDOW.fill(BACKGROUND)

    paddle.update()
    paddle.draw()

    ball.update()
    ball.draw()

    if ball_paddle_collision(ball, paddle):
        ball.pos = [ball.pos[0], paddle.pos[1] - ball.radius]
        
        # This is a simple collision resolution
        # ball.velocity[1] *= -1

        # But let's do some accurate Pong collision handling
        x_distance_from_paddle_center = ball.pos[0] - (paddle.pos[0] + paddle.dimensions[0] / 2.0)

        # Get a decimal percentage betwen -1.0 and 1.0 of how far from the center the ball is
        x_percentage = x_distance_from_paddle_center / (paddle.dimensions[0] / 2.0)
        x_percentage = clamp(x_percentage, -1.0, 1.0)

        new_ball_speed = ball.get_speed() + .2

        ball.velocity = [new_ball_speed * math.sin(MAX_ANGLE * x_percentage), -1 * new_ball_speed * math.cos(MAX_ANGLE * x_percentage)]

    # Update the display!
    pygame.display.update()

    # Update the clock limit framerate to FPS
    fpsClock.tick(FPS)
 
main()
