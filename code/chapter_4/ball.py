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

# The main function that controls the game
def main () :
  ball = Ball([100, 100], 10, [255, 0, 0], [10, 12])

  # The main game loop
  while True:
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
    
 
    # Render (Draw) elements of the game
    WINDOW.fill(BACKGROUND)

    ball.update()
    ball.draw()

    # Update the display!
    pygame.display.update()

    # Update the clock limit framerate to FPS
    fpsClock.tick(FPS)
 
main()
