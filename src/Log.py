class Log:
    def __init__(self, x, y, direction="right", speed=2):
        self.x = x
        self.start_x = x
        self.y = y
        self.direction = direction
        self.speed = speed

        self.image = Image("Log.png")
        self.image.set_size(self.image.get_width() * 0.25, self.image.get_height() * 0.25)
        self.image.set_position(self.x, self.y)
        add(self.image)

        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def move(self):
        if self.direction == "right":
            self.x += self.speed
            if self.x > 800:
                self.x = self.start_x  
        elif self.direction == "left":
            self.x -= self.speed
            if self.x + self.width < 0:
                self.x = self.start_x 

        self.image.set_position(self.x, self.y)

    def display(self):
        if self.image not in get_elements():
            add(self.image)
        self.image.set_position(self.x, self.y)
