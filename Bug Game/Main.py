import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Bugging')
crash_sound = pygame.mixer.Sound('scream.wav')


black = (0,0,0)
white = (255,255,255)
green = (0, 128, 0)
red = (255, 0, 0)
brightgreen = (124,252,0)
brightred = (255, 102, 102)

clock = pygame.time.Clock()


def things_dodged (count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+ str(count), True, white)
    screen.blit(text,(0,0))

def rock(x,y):
    rock = pygame.image.load('asteroid.png')
    rock_rect = rock.get_rect()  
    rock_list = []

    for i in range(1):
        x = random.randrange(0, display_width)
        y = random.randrange(0, display_height)
        rock_list.append([x, y])

    for i in range(len(rock_list)):
    
        screen.blit(rock, (x,y))
           
        rock_list[i][1] += 1
    
    if rock_list[i][1] > display_height:
        rock_list[i][1] = 600 - display_height
        rock_list[i][0] = random.randrange(0,display_width)

    clock.tick(60)
     
def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def quitgame ():
    pygame.quit()
    quit()
            
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 90)
    TextSurf, TextRect = text_objects(text, largeText,white)
    TextRect.center = ((display_width / 2), (display_height / 2))
    screen.blit(TextSurf, TextRect)

    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    
    pygame.display.update()
    time.sleep(2)
    game_loop()
    

def bug(x,y):
    carimg = pygame.image.load('Bug.png')
    bug_rect =  carimg.get_rect()
    screen.blit(carimg, (x,y))
    

def crash():
    message_display('You have crashed!')
    

def button(msg,x,y,w,h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText,black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
    
def gameMenu():

    intro = True

    while intro:
        for event in pygame.event.get():
            print (event)
            if event.type == pygame.QUIT:                         
                pygame.quit()
                quit()

        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Dodge Dat", largeText,black)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        button("Go!", 150, 450, 100, 50, green, brightgreen, game_loop )
        button("Quit", 550, 450, 100, 50, red, brightred, quitgame)
        pygame.display.update()
        clock.tick(15)

def game_loop():
    
    dodged = 0
    thingCount = 1
    Star_img = pygame.image.load('Star.png')
    star_rect = Star_img.get_rect()
    star_list = []
    rock = pygame.image.load('asteroid.png')
    rock_rect = rock.get_rect()
    carimg = pygame.image.load('Bug.png')
    carimg_rect = carimg.get_rect()
    rock_list = []

       
    # Loop 50 times and add a star in a random x,y position
    for i in range(50):
        x = random.randrange(0, display_width)
        y = random.randrange(0, display_height)
        star_list.append([x, y])
    #Loop 1 time and add rock to random x,y position
    for i in range(1):
        x = random.randrange(0, display_width)
        y = 600 - display_height
        rock_list.append([x, y])
    #Initiate position of Player(bug)
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    
#-------- event handling ---------------  
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    

            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                elif event.key == pygame.K_RIGHT:
                    x_change = 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
       
        x += x_change
#-----------------------------------------------
        
# ---------------code for star-----------------     
         # Set the screen background
        screen.fill(black)
     
        # Process each star flake in the list
        for i in range(len(star_list)):
     
            # Draw the snow flake
            screen.blit(Star_img, star_list[i])
           
            
     
            # Move the star down 
            star_list[i][1] += 5
     
            # If the star has moved off the bottom of the screen
            if star_list[i][1] > display_height:
                star_list[i][1] = 600 - display_height
                star_list[i][0] = random.randrange(0,display_width)
#---------------------------------------------------------   

        for i in range(len(rock_list)):
    
            screen.blit(rock, rock_list[i])
           
            rock_list[i][1] += 6
        
        if rock_list[i][1] > display_height:
            rock_list[i][1] = 600 - display_height
            rock_list[i][0] = random.randrange(0,display_width)
            dodged +=1

        if carimg_rect.colliderect(rock_rect):
            print("crash")
   
        bug(x,y)     
        things_dodged(dodged)
        pygame.display.update()
        clock.tick(60)

gameMenu()
game_loop()
pygame.quit()
quit()


