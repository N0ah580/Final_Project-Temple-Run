# Programmer: 
# Description: 

# Import and initialize the pygame library
import pygame
from pygame.locals import *
from random import randint
pygame.init()

# Import functions for drawing gridlines and using sprites
from pygame_grid import make_grid
from ucc_sprite import Sprite

### SET UP GLOBAL CONSTANTS HERE
WIDTH = 800
HEIGHT = 640
BACKGROUND_COLOR = "#111111"
FONT_COLOR = "#6aa84f"
GAME_OVER_COLOR = "crimson"
PAUSED_COLOR = "gold"
START_TIME = 1

# Create and open a pygame screen with the given size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
grid = make_grid()

# Set the title of the pygame screen
pygame.display.set_caption("My Game")

# Create a clock to keep track of time
clock = pygame.time.Clock()

# Group to hold all of the active sprites
all_sprites = pygame.sprite.LayeredUpdates()
obstacles = pygame.sprite.Group()

# Load the images

start_button_image = pygame.image.load("play.png")
start_button_image = pygame.transform.rotozoom(start_button_image, 0, 0.40)
pause_button_image = pygame.image.load("pause.png")
pause_button_image = pygame.transform.rotozoom(pause_button_image, 0, 0.40)
stop_button_image = pygame.image.load("stop.png")
stop_button_image = pygame.transform.rotozoom(stop_button_image, 0, 0.40)

walkway = pygame.image.load ("walkway2.png")
walkway = pygame.transform.rotozoom(walkway, 0, 4)
knight = pygame.image.load ("knight.png")
knight = pygame.transform.rotozoom(knight, 0, 1)
knight_flipped = pygame.transform.flip (knight, True, False)
hole = pygame.image.load ("hole.png")
hole = pygame.transform.rotozoom(hole, 0, 5.5)

#Sprite for game over screen
baloo_font_large = pygame.font.Font("Baloo.ttf", 72)
game_over = Sprite(baloo_font_large.render("GAME OVER", True, GAME_OVER_COLOR))
game_over.center = (WIDTH / 2, HEIGHT / 2)

#create timer for sprite
time_left = START_TIME


# Create a timer event for the countdown
COUNTDOWN_EVENT = pygame.event.custom_type()
OBSTACLE_EVENT = pygame.event.custom_type()

#Create sprites for background and character
walkways = pygame.sprite.Group()

bridge = Sprite (walkway)
bridge.center = (WIDTH / 2, 300)
bridge.add(all_sprites, walkways)
bridge.direction = 270
bridge.rotates = False
bridge.speed = 1.8

bridge_b = Sprite (walkway)
bridge_b.center = (WIDTH / 2, -340)
bridge_b.add(all_sprites, walkways)
bridge_b.direction = 270
bridge_b.rotates = False
bridge_b.speed = 1.8

#Sprites for the buttons
start_button = Sprite(start_button_image)
start_button.center = (100, 550)
start_button.add(all_sprites)
start_button.layer = 1

pause_button = Sprite(pause_button_image)
pause_button.center = (100, 550)
pause_button.layer = 1

stop_button = Sprite(stop_button_image)
stop_button.center = (700, 550)
stop_button.add(all_sprites)
stop_button.layer = 1

    

player = Sprite (knight)
player.flipped = False


### DEFINE HELPER FUNCTIONS




# Main Loop
running = True
while running:
    # Set the frame rate to 60 frames per second
    clock.tick(60)

    for event in pygame.event.get():
        # Check if the quit (X) button was clicked
        if event.type == QUIT:
            running = False
            
          #timer made to flip sprite
        elif event.type == COUNTDOWN_EVENT:
            if player.flipped == False:
                player.image = knight_flipped
                player.flipped = True
            else:
                player.image = knight
                player.flipped = False

        ### MANAGE OTHER EVENTS SINCE THE LAST FRAME
                
        #set to randomize obstacles
        elif event.type == OBSTACLE_EVENT:
            obstacle_a = Sprite (hole)
            obstacle_a.midbottom = (randint(220, 510), randint(-80, 50))
            obstacle_a.add(all_sprites, obstacles)

            obstacle_a.direction = 270
            obstacle_a.rotates = False
            obstacle_a.speed = 1.8
            pygame.time.set_timer(OBSTACLE_EVENT, randint (2000, 2400), 1)
        
        # Check for a mouse click
        elif event.type == MOUSEBUTTONDOWN:
            # If the exit button was clicked on, close the game
            if stop_button.mask_contains_point(event.pos):
                 running = False     
        
            #Start game
            if start_button.mask_contains_point(event.pos) and start_button.alive():
               
                bridge_b.speed = 1.8
                bridge_b.add(all_sprites, walkways)
                
                bridge.speed = 1.8
                bridge.add(all_sprites, walkways)
                
                for obstacle in obstacles:
                    obstacle.speed = 1.8
                
                player.center = (WIDTH / 2, 300)
                player.add(all_sprites)
                
                
                # Start the countdown timer
                pygame.time.set_timer(COUNTDOWN_EVENT, 300)
                pygame.time.set_timer(OBSTACLE_EVENT, 50, 1)
                
                # Swap the start/pause buttons
                pause_button.add(all_sprites)
                start_button.kill()
            
            elif pause_button.mask_contains_point(event.pos) and pause_button.alive():
                for obstacle in obstacles:
                    obstacle_a.speed = 0
                    bridge_b.speed = 0
                    bridge.speed = 0
                    pygame.time.set_timer(COUNTDOWN_EVENT, 0)
                    start_button.add(all_sprites)
                    pause_button.kill()
                    pygame.time.set_timer(OBSTACLE_EVENT, randint (0, 0), 1)
                
            

    #create statement to replace the bridge
    if bridge.top >= HEIGHT:
        bridge.bottom = 0
    if bridge_b.top >= HEIGHT:
        bridge_b.bottom = 0
        
    #Create code to handle collisions
    for obstacle in obstacles:
        if pygame.sprite.collide_mask(obstacle, player):
            all_sprites.empty()
            game_over.add(all_sprites)
            start_button.add(all_sprites)
            stop_button.add(all_sprites)
            pygame.time.set_timer(OBSTACLE_EVENT, 0)
            for obstacle in obstacles:
                obstacle.kill()
            break
            
        
        
        
    # Check for a key press
    keys_down = pygame.key.get_pressed() 
    #if the arrow keys were pressed move the character left/right
    if keys_down[K_RIGHT] and player.right < 550:
        player.x += 2
        
    if keys_down[K_LEFT] and player.left > 235:
        player.x -= 2
            
            

    ### MANAGE GAME STATE FRAME-BY-FRAME
    


    # Update the sprites' locations
    all_sprites.update()

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Redraw the sprites
    all_sprites.draw(screen)

    # Uncomment the next line to show a grid
    # screen.blit(grid, (0,0))

    # Flip the changes to the screen to the computer display
    pygame.display.flip()
    
# Quit the pygame program
pygame.quit()



##NEED HELP WITH
#How to make Obstacles random and continus
#Flip the player sprite
#Hitting start pauses the game
#Cant get collisions to work.