from Player import Player
from Fly import Fly
from Powerup import Powerup
from Car import Car
from Log import Log

keyPressedOnce = False

def setup():
    global player, frog_img, fly_one, score, fly_respawn_timer, fly_respawn_delay
    global p1, p2, p3, lives, start_screen, game_started, car, car_img, back_img, cars
    global player_dead, death_timer, saved_lives, game_over, game_over_image, logs
    
    start_screen = loadImage("start_screen.png")
    game_over_image = loadImage("game_over_image.png")
    game_started = False
    game_over = False

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
    logs = []
    
    player_dead = False
    death_timer = 0
    

    logs.append(Log(-310, -10, "right", speed=5))
    logs.append(Log(900, 35, "left", speed=5))
    logs.append(Log(-310, 80, "right", speed=5))
    logs.append(Log(-310, 125, "right", speed=5))
    logs.append(Log(900, 170, "left", speed=5))


    
    cars.append(Car(-10, 515, direction="right", speed=4, vehicle_type="car"))
    cars.append(Car(-160, 515, direction="right", speed=4, vehicle_type="car"))
    cars.append(Car(-310, 515, direction="right", speed=4, vehicle_type="car"))
    
    cars.append(Car(800, 465, direction="left", speed=2, vehicle_type="truck"))
    cars.append(Car(950, 465, direction="left", speed=2, vehicle_type="truck"))
    cars.append(Car(1100, 465, direction="left", speed=2, vehicle_type="truck"))
    
    cars.append(Car(-30, 425, direction="right", speed=9, vehicle_type="car"))
    cars.append(Car(-180, 425, direction="right", speed=9, vehicle_type="car"))
    cars.append(Car(-330, 425, direction="right", speed=9, vehicle_type="car"))
    
    cars.append(Car(-30, 375, direction="right", speed=7, vehicle_type="truck"))
    cars.append(Car(-180, 375, direction="right", speed=7, vehicle_type="truck"))
    cars.append(Car(-330, 375, direction="right", speed=7, vehicle_type="truck"))
    
    cars.append(Car(800, 330, direction="left", speed=5, vehicle_type="car"))
    cars.append(Car(950, 330, direction="left", speed=5, vehicle_type="car"))
    cars.append(Car(1100, 330, direction="left", speed=5, vehicle_type="car"))
    

def draw():
    global player, fly_one, score, fly_respawn_timer, fly_respawn_delay
    global p1, p2, p3, lives, game_started, car, car_img, back_img, cars
    global player_dead, death_timer, saved_lives, game_over, game_over_image, logs
    
    if game_over:
        image(game_over_image, 0, 0, width, height)
        return

    if not game_started:
        background(0)
        image(start_screen, 0, 0, width, height)
        return

    image(back_img, 0, 0, width, height)
    
    
    for log in logs:
        log.move()
        log.display()
    
    # Bucketing cars
    for c in cars:
        c.move()
        c.display()
        if not player_dead and player is not None and c.check_collision(player):
            saved_lives = player.lives - 1
            if saved_lives <= 0:
                game_over = True
                player = None
            else:
                player_dead = True
                death_timer = frameCount
                player = None
            break


    if p1 is not None and player is not None:
        if p1.collides_with(player):
            player.lives += 1
            p1 = None

    if fly_one is not None and player is not None:
        if player.collides_with(fly_one):
            score += 10
            fly_one = None
            fly_respawn_timer = frameCount
            fly_respawn_delay = int(random(270, 330))

    elif fly_one is None and frameCount - fly_respawn_timer > fly_respawn_delay:
        fly_one = Fly()


    fill(0)
    textSize(24)
    text("Score: " + str(score), 10, 30)
    if player is not None:
        text("Lives: " + str(player.lives), 10, 50)
        player.display()
    else:
        text("Lives: " + str(saved_lives), 10, 50)
        
        # Handle respawn
    if player_dead and frameCount - death_timer > 60:  # Wait 2 seconds (30 fps x 2)
        player = Player(width/2, 548, 40, saved_lives, frog_img)
        player_dead = False
        
        # Show the powerup and fly
    if p1 is not None:
        p1.display()
    
    if fly_one is not None:
        fly_one.move()
           
    if player is not None:
        on_log = False
        for log in logs:
            if log.check_collision(player):
                on_log = True
                # Move the player with the log
                if log.direction == "right":
                    player.x += log.speed
                else:
                    player.x -= log.speed
                break  # Only move with one log
 
        # If player is in water (not on a log) and in water zone, die
        if not on_log and 0 < player.y < 230:  # Adjust the Y range to match your river area
            saved_lives = player.lives - 1
            if saved_lives <= 0:
                game_over = True
                player = None
            else:
                player_dead = True
                death_timer = frameCount
                player = None


    
    if player is not None:
        player.display()




def keyPressed():
    global keyPressedOnce
    if not keyPressedOnce and player is not None:
        player.move(keyCode)
        keyPressedOnce = True


def keyReleased():
    global keyPressedOnce
    keyPressedOnce = False
    
def mousePressed():
    global game_started
    if not game_started:
        game_started = True
