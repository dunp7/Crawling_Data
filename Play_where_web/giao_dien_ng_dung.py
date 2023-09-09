import pygame
import math
#Intialize pygame
pygame.init()

#create a screen
screen = pygame.display.set_mode((1200, 800))

#Title and icon
pygame.display.set_caption("Đi chơi đâu?")
icon = pygame.image.load(r"picture\motoicon.png")
pygame.display.set_icon(icon)

#Moto image
motoImp =  pygame.image.load(r"picture\motocross.png")
motocx = 150
motocy = 560
motocx_change = 0
motocy_change = 0
#Drawing the moto
def moto(x, y):
    screen.blit(motoImp, (x, y))

#Game image
gamestaImp = pygame.image.load(r"picture\gamestation.png")
#Drawing game station
def game_station():
    screen.blit(gamestaImp, (925, 475))

#Event image
eventImp = pygame.image.load(r"picture\eventstation.png")
#Drawing event station
def event_station():
    screen.blit(eventImp, (925, 650))

#Road image
roadImp = pygame.image.load(r"picture\road.png")
#Drawing road
def road(x,y):
    screen.blit(roadImp, (x, y))

#backgroud
bgImp = pygame.image.load(r"picture\backgroud.png")
def backgroud():
    screen.blit(bgImp, (0, 0))

#Interaction with station
#Game
def action_with_game(x1,y1):
    distance = math.sqrt(math.pow((x1-925), 2) + math.pow((y1-475), 2))
    if distance < 25:
        return False
    else:
        return True

#Event
def action_with_event(x1,y1):
    distance = math.sqrt(math.pow((x1-925), 2) + math.pow((y1-650), 2))
    if distance < 25:
        return False
    else:
        return True

#Title
#font = pygame.font.Font("adobehebrew", 32)
#def showtitle():
#    title = font.render("Đi chơi đâu?", True, (125, 125, 125))
#    screen.blit(title, (600, 100))


print(pygame.font.get_fonts())
#Game loop
running = True
while running:
    for event in pygame.event.get():
        #click X = ending the game
        if event.type == pygame.QUIT:
            running = False
        #Moving the moto
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                motocy_change = -7
            if event.key == pygame.K_DOWN:
                motocy_change = 7
            if event.key == pygame.K_LEFT:
                motocx_change = -7
            if event.key == pygame.K_RIGHT:
                motocx_change = 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                motocy_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                motocx_change = 0


    #Screen RGB _ Red - Green - Blue
    screen.fill((0, 200, 200))

    #Drawing background
    backgroud()
    road(0, 348)
    road(470, 348)
    road(970, 348)
    road(0, 510)
    road(470, 510)
    road(970, 510)

    #Driving the moto
    motocy += motocy_change
    motocx += motocx_change

    #Drawing opject
    game_station()
    event_station()
    moto(motocx, motocy)
#    showtitle()

    #interaction
    running = action_with_event(motocx, motocy)
    if running == False:
        break
    running = action_with_game(motocx, motocy)

    #Always updating the screen
    pygame.display.update()