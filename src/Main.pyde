from Player import Player
from Fly import Fly
from Powerup import Powerup

game_started = False

def setup():
    global player, frog_img, fly_one, score, fly_respawn_timer, fly_respawn_delay, p1, p2, p3, lives, start_screen, game_started, car, car_img
    start_screen = loadImage("start_screen.png")  # Make sure this file exists in your project
    game_started = False

    size(800, 600)
    frameRate(30)
    frog_img = loadImage("Frogger_Frog_Front_Two.gif")
    fly_one = Fly()
    player = Player(width/2-20, 436, 40, 3, frog_img)
    print(fly_one.frame_1)
    score = 0
    fly_respawn_timer = 0
    fly_respawn_delay = 0
    lives = 3
    
    p1 = Powerup("c")  


def draw():
    global player, fly_one, score, fly_respawn_timer, fly_respawn_delay, p1, p2, p3, lives, game_started, car, car_img

    if not game_started:
        background(0)
        image(start_screen, 0, 0, width, height)
        return  # Skip the game logic until started

    # --- Your actual game code starts here ---

    if (p1 != None): # This prevents the program from trying to display it after it gets deleted.
        p1.display() 
        if (p1.collides_with(p1) == True):
                score += 1
                p1 = None

    
    background(2, 33, 84)
    background(255)
    #street
    fill(107, 103, 110)
    rect(0, height * 0.8, width, height * 0.1)  # Adjust for screen size
    rect(0, height * 0.6, width, height * 0.1)

    # Water blue
    fill(85, 153, 242)
    rect(0, 0, width, height * 0.5)

    # Grass green
    fill(16, 125, 45)
    rect(0, height * 0.9, width, height * 0.1)
    rect(0, height * 0.7, width, height * 0.1)
    rect(0, height * 0.5, width, height * 0.1)

    # Safe goals level ended
    rect(0, 0, width * 0.125, height * 0.1)
    rect(width * 0.225, 0, width * 0.125, height * 0.1)
    rect(width * 0.45, 0, width * 0.125, height * 0.1)
    rect(width * 0.675, 0, width * 0.125, height * 0.1)
    rect(width * 0.9, 0, width * 0.125, height * 0.1)

    # Yellow dashes
    fill(232, 229, 30)
    dash_width = width * 0.075  # Set width of the dashes relative to canvas size
    rect(0, height * 0.85, dash_width, 5)
    for i in range(1, 7):
        rect(i * width * 0.15, height * 0.85, dash_width, 5)

    # Yellow dashes higher line
    for i in range(7):
        rect(i * width * 0.15, height * 0.65, dash_width, 5)
    
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

    player.display()


def keyPressed():
    player.move(keyCode)
    
def mousePressed():
    global game_started
    if not game_started:
        game_started = True
