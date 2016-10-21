# Import a library of functions called 'pygame'
import pygame
import random
 
# Initialize the game engine
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
 
# Set the height and width of the screen
display_width = 800
display_height = 600
 
screen = pygame.display.set_mode((display_width,display_height))

class Scroller:
    Star_img = pygame.image.load('Star.png')

     
    # Create an empty array
    star_list = []
     
    # Loop 50 times and add a snow flake in a random x,y position
    for i in range(25):
        x = random.randrange(0, display_width)
        y = random.randrange(0, display_height)
        star_list.append([x, y])
     
    clock = pygame.time.Clock()
     
    # Loop until the user clicks the close button.
    done = False
    while not done:
     
        for event in pygame.event.get():   # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True   # Flag that we are done so we exit this loop
     
        # Set the screen background
        screen.fill(BLACK)
     
        # Process each snow flake in the list
        for i in range(len(star_list)):
     
            # Draw the snow flake
            screen.blit(Star_img, star_list[i])
           
            
     
            # Move the snow flake down one pixel
            star_list[i][1] += 5
     
            # If the snow flake has moved off the bottom of the screen
            if star_list[i][1] > display_height:
                star_list[i][1] = 600 - display_height
                star_list[i][0] = random.randrange(0,display_width)
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.update()
        clock.tick(60)
     
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
