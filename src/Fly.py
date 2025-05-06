import time
import random
from Timer import Timer

# Class
class Fly:
    # Constructor
    def __init__(self): # Initialization
        # Variable Declaration
        self.frame_num = 0
        self.x = random.randint(100, 400) # Spawn location! Temporary and can/will change!
        self.y = random.randint(100, 400) # Spawn location! Temporary and can/will change!
        self.speed = 1
        self.height = 30 #For collision Detection
        self.width = 30 #For collision Detection
        self.x_loc = random.randint(0, 500) # Target location! Replace 500 with game width!
        self.y_loc = random.randint(0, 500) # Target location! Replace 500 with game height!
        self.waiting = False
        # Defining Images
        self.frame_1 = loadImage("Frogger_Fly_Frame1.gif")
        self.frame_2 = loadImage("Frogger_Fly_Frame2.gif")
        self.frame_3 = loadImage("Frogger_Fly_Frame3.gif")
        self.frame_4 = loadImage("Frogger_Fly_Frame2.gif")
        # Compiling a list of frames
        self.animation = [self.frame_1, self.frame_2, self.frame_3, self.frame_4]
        self.fly_time = Timer(2000)
        
    # Methods
    def display(self): # Displays fly, uses frame_num as a counter to change frames
        image(self.animation[self.frame_num // 2], self.x, self.y) # Multiples of two to slow down animation
        if (self.frame_num >= 0 and self.frame_num < 6):
            self.frame_num += 1
        elif (self.frame_num == 6):
            self.frame_num = 0 # Loop

    def move(self): # Moves fly towards random location. If location reached, wait a couple seconds and choose a new target.
        if self.waiting == True: # If the timer is already started (and the fly is stopped)
            if (self.fly_time.done() == True): # Checks if timer has ended
                self.x_loc = random.randint(0, 500)
                self.y_loc = random.randint(0, 500)
                self.speed = 1
                self.waiting = False
        else:
            # Moves Left/Right
            if (self.x < self.x_loc):
                self.x += self.speed
            elif (self.x > self.x_loc):
                self.x -= self.speed
            # Moves Up/Down
            if (self.y < self.y_loc):
                self.y += self.speed
            elif (self.y > self.y_loc):
                self.y -= self.speed
            # Checks if target is reached and begins timer
            if (self.x == self.x_loc and self.y == self.y_loc):
                time_start = False
                self.speed = 0
                self.fly_time.start()
                self.waiting = True
        self.display()
