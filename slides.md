---
layout: cover
theme: seriph
---

# Game Dev in Python!

---
layout: cover
---

# Intro

---

# Why Python

- Most game development involves the use of C++ and C#
- This is because performance is a major concern in 3D games
- We’re going to build 2D games where performance isn’t a huge concern and simplicity is.
- Enter Python

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Python_logo_01.svg/800px-Python_logo_01.svg.png" width="200" height="200" class="absolute right-20px bottom-20px"/>


---

# Why Python

- Many libraries
- You’ll learn the concepts without the hassle of C++

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Python_logo_01.svg/800px-Python_logo_01.svg.png" width="200" height="200" class="absolute right-20px bottom-20px"/>

---

# PyGame

- Graphics is Hard
- Graphics is platform dependent

<img src="https://www.pygame.org/docs/_images/pygame_logo.png" width="400" class="absolute right-20px bottom-20px"/>

---

# Getting Started

Download Python at https://www.python.org/downloads

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Python_logo_01.svg/800px-Python_logo_01.svg.png" width="200" height="200" class="absolute right-20px bottom-20px"/>
---

# Getting Started

Install VSCode at https://code.visualstudio.com/


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/2048px-Visual_Studio_Code_1.35_icon.svg.png" width="200" height="200" class="absolute right-20px bottom-20px"/>
---

# Install PyGame

```shell
$ pip3 install pygame
```
<img src="https://www.pygame.org/docs/_images/pygame_logo.png" width="400" class="absolute right-20px bottom-20px"/>

---

# Basic PyGame Program

```python

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
```

---

# Basic PyGame Program

```python
# The main function that controls the game
def main () :
  # The main game loop
  while True:
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
    
 
    # Render elements of the game
    WINDOW.fill(BACKGROUND)

    pygame.draw.rect(WINDOW, (0, 0, 0), pygame.Rect(10, 10, 100, 100))

    pygame.display.update()
    fpsClock.tick(FPS)
 
main()

```
