# Written by Katelyn
# NOTES: Display and collision functioning! Powerup should appear in a random location when called. Effects usable(?)
# Might end up having to resize graphics.
"""
Powerups:
a. Slow time
b. Point X2
c. Extra life
Use the letters each powerup is assigned when calling them in, eg. 'health = Powerup("c")'
More might be added in the future; these are some basic ones that should be easy to put in.

Other Ideas:
d. Luck boost (Increased chances of powerup/fly spawning?)
e. Long Leap (Jump further. Not sure if this is as helpful to the player as it seems.)
"""
import time
import random

class Powerup:
    # Constructor
    def __init__(self, type):
        self.type = type
        self.x = random.randint(0, 500) # 500 is temporary! Replace with game length.
        self.y = random.randint(0, 500) # 500 is temporary! Replace with game height.
        self.width = 30
        self.height = 30
        self.time_slow = loadImage("Frogger_Clock_Powerup.gif") # Shows up as a blue icon with a frozen clock.
        self.double_points = loadImage("Frogger_Point_Powerup.gif") # Shows up as a yellow icon witih a four-pointed star. A bit off-center, nothing to be done about it though.
        self.health_bonus = loadImage("Frogger_Health_Powerup.gif") # Shows up as a red icon with a medical (+) sign.

    # Methods
    def display(self): # Displays powerup
        if self.type == "a": 
            image(self.time_slow, self.x, self.y)
        elif self.type == "b": 
            image(self.double_points, self.x, self.y)
        elif self.type == "c": 
            image(self.health_bonus, self.x, self.y)

    def collides_with(self, other):
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )
