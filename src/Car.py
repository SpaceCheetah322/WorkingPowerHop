class Car:
    def __init__(self, x, y, direction="right", speed=5, vehicle_type="car", scale=1, spacing=150):
        self.x = x
        self.y = y
        self.direction = direction 
        self.speed = speed
        self.vehicle_type = vehicle_type
        self.spacing = spacing

        image_file = "Car.png" if vehicle_type=="car" else "Frogger_Red_Truck.gif"
        self.image = loadImage(image_file)

        # scale up everything a bit
        self.scale = scale * 1.5
        self.width = self.image.width * self.scale
        self.height= self.image.height * self.scale
        self.image.resize(int(self.width), int(self.height))

    def move(self):
        # advance
        if self.direction == 'right':
            self.x += self.speed
            # off the right edge?
            if self.x > width:
                # respawn just off the left edge
                self.x = -self.width - self.spacing

        else:  # 'left'
            self.x -= self.speed
            # off the left edge?
            if self.x + self.width < 0:
                # respawn just off the right edge
                self.x = width + self.spacing

    def display(self):
        image(self.image, self.x, self.y)
        
    def check_collision(self, frog):
        left = max(self.x, frog.x)
        right = min(self.x + self.width, frog.x + frog.width)
        top = max(self.y, frog.y)
        bottom = min(self.y + self.height, frog.y + frog.height)

        if left >= right or top >= bottom:
            return False  # no overlap at all
    
        for px in range(int(left), int(right)):
            for py in range(int(top), int(bottom)):
                car_img_x = int(px - self.x)
                car_img_y = int(py - self.y)
                frog_img_x = int(px - frog.x)
                frog_img_y = int(py - frog.y)
    
                if (0 <= car_img_x < self.image.width and
                    0 <= car_img_y < self.image.height and
                    0 <= frog_img_x < frog.img.width and
                    0 <= frog_img_y < frog.img.height):
    
                    car_pixel = self.image.get(car_img_x, car_img_y)
                    frog_pixel = frog.img.get(frog_img_x, frog_img_y)
    
                    # If both pixels are visible (not transparent), it's a hit
                    if alpha(car_pixel) > 10 and alpha(frog_pixel) > 10:
                        return True
    
        return False
