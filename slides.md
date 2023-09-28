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

---

# Code

You can find the code at https://github.com/Coding-Academy-STL/GameDevWithPython/tree/main/code/chapter_1

---
layout: cover
---
# Chapter 2: Drawing

---

# Drawing Basics

Your screen is made up of a bunch of little lights called pixels

<img src="https://www.orientdisplay.com/wp-content/uploads/2021/01/1-5.png" width="200"/>

As you can see, each little box of color you see on your screen is made from blending red, green, and blue light

---

# Screen Coordinates


- In order to draw an image or a shape, you need to tell the computer which pixels to fill in. In order to do that, you need to be able to give them each a unique name.
- Since they are ordered in rows and columns, can give each pixel a "x" coordinate and a "y" coordinate.

<img src="https://pbaumgarten.com/pygame/img/pygame-coordinate-system.png"/>

---

# Colors

- You can make any color by combining different shades of Red, Green, and Blue. This is how LCD screens work.
- In order to represent different shades of Red, Green, and Blue (RGB), we use numbers from 0-255.

[Color Picker](https://g.co/kgs/9Motck)
[Color Game](https://primozz.github.io/colorgame/)

---

# Drawing

[Draw Functions in Pygame](https://www.pygame.org/docs/ref/draw.html)

---

# Code

You can find the code at https://github.com/Coding-Academy-STL/GameDevWithPython/tree/main/code/chapter_2

---
layout: cover
---
# Chapter 3: Input

Input is a large part of GameDev. Is a game really a game if you can't interact with it?

---

# Input Basics

Take this bit of code

```python
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
```

What is it doing?

---

# Input Basics

When you run your loop, pygame accumulates a list of inputs recieved by the system

These inputs can include
- Window Events (Close, Minimize)
- Keyboard Events (Key pressed down, Key released)
- Mouse Events (Mouse position, Mouse button pressed, Mouse button released)

---

# Input Basics

```python
for event in pygame.event.get() :
```

- This loops through all of the events python has recieved from the system
- `pygame.event.get()` returns an array of all of the events
- `event` is the current event in the loop

---

# Input Basics

- The `event` variable has the type `Event`. You can find the definition for that [here](https://www.pygame.org/docs/ref/event.html#pygame.event.Event)
- The `Event` type has a member variable called `type` which is an integer and represents the type of event
- Pygame provides us with some constants that contain the number for their respective events. Some event types include `QUIT`, `MOUSEDOWN`, `MOUSEUP`, `KEYDOWN`, `KEYUP`
- So, for example, if we want to check if an event is a quit event, we use the code 
```python
if event.type == QUIT:
    # Do the things you want to do when you recieve the QUIT event
```

---

# Keyboard Events

- Checking for key events is simple
- When a key is pressed down, pygame receieves a KEYDOWN event and when a key is released, it recieves a KEYUP event
- A keyboard event has a member called key which contains the key that was pressed

- This code checks if the `a` key was pressed
```python
    for event in pygame.event.get() :
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if even.type == KEYDOWN:
        if event.key == K_a:
          print("key \"a\" was pressed")
```

- You can find a list of keys [here](https://www.pygame.org/docs/ref/key.html) if you scroll down

---

# Keyboard Events

- This way of checking for keyboard events is annoying though, because you can only check for key presses in a single spot.
- Luckily, pygame provides a function where you can get the state of a key anywhere in your code

```python
if pygame.key.get_pressed()[K_a]:
  print("key \"a\" was pressed")

# Does the exact same thing as
for event in pygame.event.get() :
  if even.type == KEYDOWN:
    if event.key == K_a:
      print("key \"a\" was pressed")

# But you can do it anywhere in the code
```

- The function `pygame.key.get_pressed()` returns an array of booleans that represent the up or down state of the keys on the keyboard. You can access the array using the key constants provided by python
- For example, `pygame.key.get_pressed()[K_a]` returns true if the `a` key is pressed

---

# Mouse Events

- You could check for mouse events in the event for loop, but we've found that there are easier ways to do this.
- Similar to the `pygame.keyboard.get_pressed` function, there is a `pygame.mouse.get_pressed` function. This doesn't return an array, however. Rather, it returns a tuple with three values. Index 0 in the tuple represents the state of the left mouse button, the second represents the state of the right mouse button, and the third represents the state of the middle mouse.
- You can find the definition for the function [here](https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pressed)

---


# Code

You can find the code at https://github.com/Coding-Academy-STL/GameDevWithPython/tree/main/code/chapter_3

---

# Mouse Events

- It is also useful to determine the location of the mouse. The function for this is simple.
- `pygame.mouse.get_pos()` simply returns a tuple with the x and y coordinates of the mouse

---
layout: cover
---
# Chapter 4: Object Oriented Programming
---

# Object Oriented Programming

Object Oriented Programming gives us a way to represent things, or objects, in our world and keep all of their data in one place.

For example, if we wanted to represent a paddle in, say, pong, without OOP, we would declare its data like
```python
paddlePos = [0, 0]
paddleColor = (255, 0, 0)
paddleSize = (100, 25)
```
and its functions like

```python
def setPaddlePos(newPos):
    paddlePos = newPos
```

This gets very unorganized very quickly. All of these variables and functions are scattered across the code, and what if we want to create multiple paddles? There are two paddles in Pong, of course.

---

# Object Oriented Programming

With OOP, we can simplify this. The data and functions above become

```python
class Paddle:
    def __init__(self, dim, pos, color):
        self.dim = dim
        self.pos = pos
        self.color = color
    def set_pos(self, pos):
        self.pos = pos

...

paddle1 = Paddle((100, 50), (0, 0), (255, 0, 0))
paddle2 = Paddle([100, 50], (100 0), (255, 0, 0))

paddle1.set_pos([10, 10])
```

You may not understand the code above right now, but the point is that OOP condenses your code and helps you stay organized

---

# Object Oriented Programming

Here's a quick W3 schools tutorial on OOP: https://www.w3schools.com/python/python_classes.asp

---

# Object Oriented Programming Homework

- Create a class called Paddle
- Give it these variables:
    - position
    - dimensions
    - color
- Give it these functions:
    - draw()
        - This function should draw the paddle on the screen
    - update()
        - This function should check for keyboard input and move the paddle left and right using the arrow keys or `a` and `d`
        - This function should also ensure that the paddle doesn't go outside of the screen

---

# Helpful Hints

- When writing the `update()` function, in order to make sure the paddle isn't out of bounds
    - Check if the x coordinate is < 0. If so, set the X coordinate to 0
    - Check if the x coordinate minus the width of the paddle is greater than the window width. If it is, it means the paddle is out of bounds and the x coordinate should be set to the window width minus the paddle width

---

# Contact Me

Contact me at aidenl@codingacademystl.org
