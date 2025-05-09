from Player import Player
from Fly import Fly
from Powerup import Powerup
from Car import Car

game_started = False

def setup():
    global player, frog_img, fly_one, score, fly_respawn_timer, fly_respawn_delay, p1, p2, p3, lives, start_screen, game_started, car, car_img, back_img, cars
    
    start_screen = loadImage("start_screen.png")
    game_started = False

    size(800, 600)
    frameRate(30)
    
    frog_img = loadImage("Frogger_Frog_Front_Two.gif")
    back_img = loadImage("backdrop.png")
    fly_one = Fly()
    player = Player(width/2, 548, 40, 3, frog_img)
    score = 0
    fly_respawn_timer = 0
    fly_respawn_delay = 0
    p1 = Powerup("c")
    
    cars = []
    
    cars.append(Car(-10, 520, direction="right", speed=4, vehicle_type="car"))
    cars.append(Car(800, 470, direction="left", speed=2, vehicle_type="truck"))
    cars.append(Car(-10, 425, direction="right", speed=9, vehicle_type="car"))
    cars.append(Car(-10, 380, direction="right", speed=7, vehicle_type="truck"))
    cars.append(Car(800, 335, direction="left", speed=5, vehicle_type="car"))

def draw():
    global player, fly_one, score, fly_respawn_timer, fly_respawn_delay, p1, p2, p3, lives, game_started, car, car_img, back_img, cars

    if not game_started:
        background(0)
        image(start_screen, 0, 0, width, height)
        return

    # --- Actual game code starts here ---

    image(back_img, 0, 0, width, height)
    
    for car in cars:
        car.move()
        car.display()
        if car.check_collision(player):
            player.lives -= 1
    

    if p1 is not None:
        p1.display()
        if p1.collides_with(player):
            player.lives += 1
            p1 = None
    
    if car.check_collision(player):
        player.lives -= 1

    if fly_one is not None:
        fly_one.move()
        if player.collides_with(fly_one):
            score += 10
            fly_one = None
            fly_respawn_timer = frameCount
            fly_respawn_delay = int(random(270, 330))
    else:
        if frameCount - fly_respawn_timer > fly_respawn_delay:
            fly_one = Fly()

    fill(0)
    textSize(24)
    text("Score: " + str(score), 10, 30)
    text("Lives: " + str(player.lives), 10, 50)

    player.display()


def keyPressed():
    player.move(keyCode)
    
def mousePressed():
    global game_started
    if not game_started:
        game_started = True
