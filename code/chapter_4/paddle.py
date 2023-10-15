import pygame, sys, random
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


# The main function that controls the game
def main () :
  paddle = Paddle([100, 250], [100, 25], [255, 0, 0], 10, K_a, K_d)
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

    # Update the display!
    pygame.display.update()

    # Update the clock limit framerate to FPS
    fpsClock.tick(FPS)
 
main()
