class Player:
    def __init__(self, x, y, speed, lives, img):
        self.x = x
        self.y = y
        self.speed = 46.1
        self.lives = lives
        self.img = img
        self.width = img.width
        self.height = img.height

    def move(self, key_code):
        if key_code == LEFT or key == 'a':
            self.x -= self.speed
        elif key_code == RIGHT or key == 'd':
            self.x += self.speed
        elif key_code == UP or key == 'w':
            self.y -= self.speed
        elif key_code == DOWN or key == 's':
            self.y += self.speed
    
        # Keep the player inside the screen
        self.x = constrain(self.x, 0, width - (self.width-12))
        self.y = constrain(self.y, 0, height - (self.height-12))


    def display(self):
        image(self.img, self.x, self.y)
        
    def collides_with(self, other):
        buffer_x = 10  # horizontal padding
        buffer_y = 10   # vertical padding
        return (
            self.x + buffer_x < other.x + other.width and
            self.x + self.width - buffer_x > other.x and
            self.y + buffer_y < other.y + other.height and
            self.y + self.height - buffer_y > other.y
        )
