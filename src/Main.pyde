from Player import Player
from Fly import Fly
from Powerup import Powerup
from Car import Car
from Log import Log
from Timer import Timer

keyPressedOnce = False

def setup():
    global player, frog_img, fly_one, score, fly_respawn_timer, fly_respawn_delay, won, win_screen
    global p1, p2, p3, lives, start_screen, game_started, car, car_img, back_img, cars, heart
    global player_dead, death_timer, saved_lives, game_over, game_over_image, logs, last_known_lives
    global currentFrog, player1, player2, player3, player4, player5, lily_pads, occupied_pads, pixelFont
    global game_timer, timer_duration, p1_respawn_timer, p2_respawn_timer, p3_respawn_timer, p1_respawn_delay, p2_respawn_delay, p3_respawn_delay
    global car_original_speeds, log_original_speeds, slowdown_active, slowdown_start_frame, slowdown_duration
    global level, base_car_speeds, base_log_speeds
    
    start_screen = loadImage("start_screen.png")
    game_over_image = loadImage("game_over_image.png") 
    win_screen = loadImage("win_screen.png")
    game_started = False
    game_over = False
    won = False

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
    p2 = Powerup("b")
    p3 = Powerup("a")
    
    car_original_speeds = []
    log_original_speeds = []
    slowdown_active = False
    slowdown_start_frame = 0
    slowdown_duration = 300  # ~5 seconds at 60 FPS

    
    pixelFont = createFont("PressStart2P-Regular.ttf", 16)  # Replace with your font file name
    textFont(pixelFont)
    
    
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
    
    lily_pads = [105, 255, 405, 555, 705]  # X positions for lily pads
    occupied_pads = [False] * len(lily_pads)
    
    player1 = Player(width/2, 548, 40, 3, frog_img)
    player = player1
    currentFrog = player1
    
    
    player2 = player3 = player4 = player5 = None
    
    timer_duration = 90000  # 30 seconds, for example
    game_timer = Timer(timer_duration)
    game_timer.start()
    
    p1_respawn_timer = 0
    p2_respawn_timer = 0
    p3_respawn_timer = 0
    
    p1_respawn_delay = 0
    p2_respawn_delay = 0
    p3_respawn_delay = 0
    
    heart = loadImage("Frogger_Life_Icon.gif")
    last_known_lives = 0
    
    base_car_speeds = [c.speed for c in cars]
    base_log_speeds = [l.speed for l in logs]

def level_up():
    global level, occupied_pads, player, currentFrog, cars, logs
    level += 1

    # reset the pads
    for i in range(len(occupied_pads)):
        occupied_pads[i] = False

    # reset the frog
    player = Player(width/2, 548, 40, player.lives, frog_img)
    currentFrog = player

    # rescale every vehicle
    speed_multiplier = 1 + 0.1 * (level - 1)  # +10% per level
    for i, c in enumerate(cars):
        c.speed = base_car_speeds[i] * speed_multiplier
    for i, l in enumerate(logs):
        l.speed = base_log_speeds[i] * speed_multiplier
    

def draw():
    global player, fly_one, score, fly_respawn_timer, fly_respawn_delay, won
    global p1, p2, p3, lives, game_started, car, car_img, back_img, cars, heart, last_known_lives
    global player_dead, death_timer, saved_lives, game_over, game_over_image, logs
    global currentFrog, player1, player2, player3, player4, player5, lily_pads, occupied_pads
    global car_original_speeds, log_original_speeds, slowdown_active, slowdown_start_frame, slowdown_duration
    global game_timer, timer_duration, p1_respawn_timer, p2_respawn_timer, p3_respawn_timer, p1_respawn_delay, p2_respawn_delay, p3_respawn_delay
    global level, base_car_speeds, base_log_speeds, cars
    
    
    if game_over:
        image(game_over_image, 0, 0, width, height)
        return

    if not game_started:
        background(0)
        image(start_screen, 0, 0, width, height)
        return
    if won:
        image(win_screen, 0, 0, width, height)
        return

    image(back_img, 0, 0, width, height)
    
    
    
    if player != None:
        last_known_lives = player.lives
    
    for i in range(last_known_lives):
        image(heart, 770 - i * 25, 560)

    
    
    
    
    # Check if time has run out
    if game_timer.done() and player is not None:
        saved_lives = player.lives - 1
        if saved_lives <= 0:
            game_over = True
            player = None
        else:
            player_dead = True
            death_timer = frameCount
            player = None

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


    # Powerup p1 (extra life)
    if p1 is not None and player is not None:
        if p1.collides_with(player):
            player.lives += 1
            p1 = None
            p1_respawn_timer = frameCount
            p1_respawn_delay = int(random(300, 450))  # 10–15 seconds at 30fps
    
    elif p1 is None and frameCount - p1_respawn_timer > p1_respawn_delay:
        p1 = Powerup("c")

            
    # Powerup p2 (score)
    if p2 is not None and player is not None:
        if p2.collides_with(player):
            score += 10
            p2 = None
            p2_respawn_timer = frameCount
            p2_respawn_delay = int(random(300, 450))
    
    elif p2 is None and frameCount - p2_respawn_timer > p2_respawn_delay:
        p2 = Powerup("b")
    
    # Powerup p3 (extra life)
    if p3 is not None and player is not None:
        if p3.collides_with(player):
            print("Powerup 'a' collected: Slowing down cars and logs...")
            
            car_original_speeds = [c.speed for c in cars]
            log_original_speeds = [l.speed for l in logs]
    
            for c in cars:
                print("Original speed of car at y=" + str(c.y) + ": " + str(c.speed))
                c.speed *= 0.5
            
            for l in logs:
                print("Original speed of log at y=" + str(l.y) + ": " + str(l.speed))
                l.speed *= 0.5
    
            slowdown_active = True
            slowdown_start_frame = frameCount
    
            p3 = None
            p3_respawn_timer = frameCount
            p3_respawn_delay = int(random(300, 450))
    
    elif p3 is None and frameCount - p3_respawn_timer > p3_respawn_delay:
        p3 = Powerup("a")
        
    if slowdown_active and frameCount - slowdown_start_frame > slowdown_duration:
        print("Slowdown expired: Restoring speeds...")
        for i in range(len(cars)):
            cars[i].speed = car_original_speeds[i]
        for i in range(len(logs)):
            logs[i].speed = log_original_speeds[i]
        
        slowdown_active = False






    if fly_one is not None and player is not None:
        if player.collides_with(fly_one):
            score += 10
            fly_one = None
            fly_respawn_timer = frameCount
            fly_respawn_delay = int(random(270, 330))

    elif fly_one is None and frameCount - fly_respawn_timer > fly_respawn_delay:
        fly_one = Fly()


    fill(0)
    textSize(9)
    text("Score: " + str(score), 10, 30)

        
        # Handle respawn
    if player_dead and frameCount - death_timer > 60:  # Wait 2 seconds (30 fps x 2)
        player = Player(width/2, 548, 40, saved_lives, frog_img)
        player_dead = False
        game_timer = Timer(timer_duration)
        game_timer.start()
        
    for log in logs:
        log.move()
        log.display()

        
        # Show the powerup and fly
    if p1 is not None:
        p1.display()
        
    if p2 is not None:
        p2.display()
        
    if p3 is not None:
        p3.display()
    
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
        if not on_log and 35 < player.y < 265: #35
            saved_lives = player.lives - 1
            if saved_lives <= 0:
                game_over = True
                player = None
            else:
                player_dead = True
                death_timer = frameCount
                player = None
    
    if player is not None and player.y <= 35:
        closest_index = min(range(len(lily_pads)), key=lambda i: abs(player.x - lily_pads[i]))
        snap_distance = abs(player.x - lily_pads[closest_index])
        snap_radius = 40  # Radius within which a frog can land on a lily pad
    
        if snap_distance <= snap_radius and not occupied_pads[closest_index]:
            # Successfully landed on a lily pad
            player.x = lily_pads[closest_index]
            player.y = 40
            occupied_pads[closest_index] = True
    
            if all(occupied_pads):
                level_up()
            else:
                saved_lives = player.lives
                player = Player(width / 2, 548, 40, saved_lives, frog_img)
                currentFrog = player
        else:
            # Missed lily pad (i.e., landed on grass)
            saved_lives = player.lives - 1 if player is not None else 0
            if saved_lives <= 0:
                game_over = True
                player = None
            else:
                player_dead = True
                death_timer = frameCount
                player = None

                
    for i in range(len(lily_pads)):
        if occupied_pads[i]:
            image(frog_img, lily_pads[i] - 22, 0, 65, 65)
            

        
        
    # Timer bar display
    # Timer circle display
    remaining_time = max(0, timer_duration - (millis() - game_timer.saved_time))
    angle = map(remaining_time, 0, timer_duration, 0, TWO_PI)
    
    cx = width - 30  # x position of circle
    cy = 26          # y position of circle
    radius = 20      # size of the timer circle
    
    # Background circle (full)
    fill(34, 97, 0)
    noStroke()
    ellipse(cx, cy, radius * 2, radius * 2)
    
    # Remaining time arc
    fill(68, 185, 4)
    arc(cx, cy, radius * 2, radius * 2, -HALF_PI, -HALF_PI + angle, PIE)

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
