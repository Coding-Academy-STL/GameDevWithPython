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

# The main function that controls the game
def main () :
  # Just some variables and constants
  PADDLE_WIDTH = 100
  PADDLE_HEIGHT = 33
  PADDLE_COLOR = (255, 0, 0) # Red paddle

  PADDLE_SPEED = 5 # How fast the paddle moves in pixels/frame

  paddle_pos = [200, 200] # The position of the paddle [x, y]

  # The main game loop
  while True:
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()

      # This is one way to check if a key is pressed
      # Check if the "y" key is pressed
      # Only triggers when you first press down the key and not when you hold it
      if event.type == KEYDOWN:
        if event.key == K_y:
            print("You pressed the y key!")
 
    # Render (Draw) elements of the game
    WINDOW.fill(BACKGROUND)

    # Move the paddle based on user input
    if pygame.key.get_pressed()[K_a]:
      # Move left
      paddle_pos[0] -= PADDLE_SPEED
    if pygame.key.get_pressed()[K_d]:
      # Move right
      paddle_pos[0] += PADDLE_SPEED

    # Make sure we don't move the paddle off of the screen
    if paddle_pos[0] <= 0:
      # If the X coordinate of the top left-hand corner of the rectangle is less than 0,
      # it means that the rectangle is outside of the screen
      # so we want to bring it back to 0
      paddle_pos[0] = 0
    elif paddle_pos[0] + PADDLE_WIDTH > WINDOW_WIDTH:
      # This check is a little harder conceptually
      # Here, we are checking if the paddle is outside of the right side of the screen
      # paddle_pos[0] + PADDLE_WIDTH gets you the X coordinate of the right side of the paddle 
      # and if this coordinate is greater than the width, it means that the paddle is outside
      # of the window. If this is true, then we just reset the let corner to the point where the right corner
      # is touching the right edge of the window
      paddle_pos[0] = WINDOW_WIDTH - PADDLE_WIDTH


    # Draw a rectangle!
    pygame.draw.rect(WINDOW, PADDLE_COLOR, pygame.Rect(paddle_pos[0], paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))

    # Update the display!
    pygame.display.update()

    # Update the clock limit framerate to FPS
    fpsClock.tick(FPS)
 
main()
