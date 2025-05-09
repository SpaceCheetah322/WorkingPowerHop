class Car:
    def __init__(self, x, y, direction="right", speed=5, vehicle_type="car"):
        self.x = x
        self.start_x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        self.vehicle_type = vehicle_type

        image_file = "Car.png" if self.vehicle_type == "car" else "Frogger_Red_Truck.gif"
        self.image = loadImage(image_file)

        scale = 1 if self.vehicle_type == "car" else 1
        self.width = self.image.width * scale
        self.height = self.image.height * scale
        self.image.resize(int(self.width), int(self.height))

    def move(self):
        if self.direction == 'right':
            self.x += self.speed
            if self.x > 800:
                self.x = self.start_x
        elif self.direction == 'left':
            self.x -= self.speed
            if self.x + self.width < 0:
                self.x = self.start_x

    def display(self):
        image(self.image, self.x, self.y)

    def check_collision(self, frog):
        return (frog.x < self.x + self.width and
                frog.x + frog.width > self.x and
                frog.y < self.y + self.height and
                frog.y + frog.height > self.y)
