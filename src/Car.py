class Car:
    def __init__(self, x, y, direction="right", speed=5, vehicle_type="car"):
        self.x = x
        self.start_x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        self.vehicle_type = vehicle_type


        image_file = "Car.png"
        if self.vehicle_type == "truck":
            image_file = "Truck.png"

        self.image = Image(image_file)
        

        scale = 0.2 if self.vehicle_type == "car" else 0.3
        self.image.set_size(self.image.get_width() * scale, self.image.get_height() * scale)
        self.image.set_position(self.x, self.y)
        add(self.image)

        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def move(self):
        if self.direction == 'right':
            self.x += self.speed
            if self.x > 800:
                self.x = self.start_x
        elif self.direction == 'left':
            self.x -= self.speed
            if self.x + self.width < 0:
                self.x = self.start_x

        self.image.set_position(self.x, self.y)

    def check_collision(self, frog):
        if (frog.x < self.x + self.width and
            frog.x + frog.width > self.x and
            frog.y < self.y + self.height and
            frog.y + frog.height > self.y):
            return True
        return False

    def display(self):
        if self.image not in get_elements():
            add(self.image)
        self.image.set_position(self.x, self.y)
