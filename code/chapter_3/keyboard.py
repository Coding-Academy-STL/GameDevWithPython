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

    # Another way to detect key presses
    # Triggers whenever the key is being held
    if pygame.key.get_pressed()[K_a]:
        print("You pressed the \"a\" key!")

    # Draw a rectangle!
    pygame.draw.rect(WINDOW, (0, 0, 0), pygame.Rect(10, 10, 100, 100))

    # Update the display!
    pygame.display.update()

    # Update the clock limit framerate to FPS
    fpsClock.tick(FPS)
 
main()
