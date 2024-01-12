# Programmer: 
# Description: 

# Import and initialize the pygame library
import pygame
from pygame.locals import *
pygame.init()

# Import functions for drawing gridlines and using sprites
from pygame_grid import make_grid
from ucc_sprite import Sprite

### SET UP GLOBAL CONSTANTS HERE
WIDTH = 800
HEIGHT = 640
BACKGROUND_COLOR = "black"
FONT_COLOR = "#6aa84f"
GAME_OVER_COLOR = "crimson"
PAUSED_COLOR = "gold"

# Create and open a pygame screen with the given size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
grid = make_grid()

# Set the title of the pygame screen
pygame.display.set_caption("My Game")

# Create a clock to keep track of time
clock = pygame.time.Clock()

# Group to hold all of the active sprites
all_sprites = pygame.sprite.LayeredUpdates()

# Load the images
walkway = pygame.image.load ("walkway.jpeg")
walkway = pygame.transform.rotozoom(walkway, 0, 7)
knight = pygame.image.load ("knight.png")
knight = pygame.transform.rotozoom(knight, 0, 1)
hole = pygame.image.load ("hole.png")
hole = pygame.transform.rotozoom(hole, 0, 5.5)

#Create sprites for background and character
walkways = pygame.sprite.Group()

bridge = Sprite (walkway)
bridge.center = (WIDTH / 2, 300)
bridge.add(all_sprites, walkways)
bridge.direction = 270
bridge.rotates = False
bridge.speed = 0.6

bridge_b = Sprite (walkway)
bridge_b.center = (WIDTH / 2, -150)
bridge_b.add(all_sprites, walkways)
bridge_b.direction = 270
bridge_b.rotates = False
bridge_b.speed = 0.6

#create statement to replace the bridge
if bridge.top >= 0:
    bridge.center == (WIDTH / 2, -150)
if bridge_b.top == 0:
    bridge.center = (WIDTH / 2, -150)
    

player = Sprite (knight)
player.center = (WIDTH / 2, 300)
player.add(all_sprites)

obstacle_a = Sprite (hole)
obstacle_a.center = (230, 200)
obstacle_a.add(all_sprites)

### SET UP YOUR GAME HERE



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

        ### MANAGE OTHER EVENTS SINCE THE LAST FRAME
        


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
