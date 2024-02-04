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

pipe_image = pygame.image.load("resources/images/steelpipe.jpg")
pipe_image = pygame.transform.scale(pipe_image, (pipe_image.get_width() * 0.5, pipe_image.get_height() * 0.5))
pipe_image_position = (50, 50)

pipe_sound = pygame.mixer.Sound("resources/sound/metal-pipe.mp3")

# The main function that controls the game
def main () :
  # The main game loop
  while True:
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
    
 
    # Render (Draw) elements of the game
    WINDOW.fill(BACKGROUND)

    # Draw a rectangle!
    # pygame.draw.rect(WINDOW, (0, 0, 0), pygame.Rect(10, 10, 100, 100))

    WINDOW.blit(pipe_image, pipe_image_position)

    if pygame.mouse.get_pressed()[0] and pygame.Rect(pipe_image_position[0], pipe_image_position[1], pipe_image.get_width(), pipe_image.get_height()).collidepoint(pygame.mouse.get_pos()):
        pipe_sound.stop()
        pipe_sound.play()

    # Update the display!
    pygame.display.update()

    # Update the clock limit framerate to FPS
    fpsClock.tick(FPS)
 
main()
