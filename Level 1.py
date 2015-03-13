import pygame, sys , time
from pygame.locals import *



key1 = 0
blue=(0,0,255)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0 , 0 , 0)
tel_out = (25 , 25 , 122)
tel_in = (49 , 79 , 79)
die = (0 , 100 , 0)
key = (173,234,234)
end = (255 , 255 , 0)
hidden = (255,99,71)
DISPLAY=pygame.display.set_mode((630,460),0,32)
key_img = pygame.image.load("key.png").convert()
win_img = pygame.image.load("win.png").convert()
nokey_img = pygame.image.load("nokey.png").convert()
pygame.init()
pygame.display.set_caption('Math game')
size = [640, 480]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
x = 0
y = 460
step = 20
screen = pygame.display.set_mode([640, 480])
background_position = (0,0)
# by default the key repeat is disabled
# call set_repeat() to enable it
pygame.key.set_repeat(50, 50)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # check if key is pressed
        # if you use event.key here it will give you error at runtime
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x == 120 and y == 100:
                    n = 0
                elif x == 40 and y < 480 and y > 0:
                    n = 0
                elif x == 300 and y == 220:
                    n = 0
                elif x == 340 and y > 40 and y < 280:
                    n = 0
                elif x == 400 and y > 100 and y < 240 :
                    n = 0
                else:
                    x -= step
            if event.key == pygame.K_RIGHT:
                if x == 80 and y == 100:
                    n = 0
                elif x == 0 and y < 480 and y > 0:
                    n = 0
                elif x == 80 and y == 220:
                    n = 0
                elif x == 80 and y == 220:
                    n = 0
                elif x == 300 and y > 40 and y < 260:
                    n = 0
                elif x == 80 and y == 260:
                    n = 0
                elif x == 360 and y > 120 and y < 220:
                    n = 0
                elif x == 440 and y == 280:
                    n = 0
                elif x == 440 and y == 240:
                    n = 0
                elif x == 440 and y == 260:
                    n = 0
                else:
                    x += step
            if event.key == pygame.K_UP:
                if x == 100 and y == 120:
                    n = 0
                elif x > 80 and x < 300 and y == 240:
                    n = 0
                elif x > 80 and x < 340 and y == 280:
                    n = 0
                elif x > 320 and x < 400 and y == 240:
                    n = 0
                elif x > 320 and x < 380 and y == 140:
                    n = 0
                elif x > 440 and x < 640 and y == 300:
                    n = 0
                elif x > 440 and x < 640 and y == 260:
                    n = 0
                else:
                    y -= step
            if event.key == pygame.K_DOWN:
                if x == 100 and y == 80:
                    n = 0
                elif x == 20 and y == 0:
                    n = 0
                elif x > 80 and x < 300 and y == 200:
                    n = 0
                elif x > 80 and x < 320 and y == 240:
                    n = 0
                elif x == 320 and y == 40:
                    n = 0
                elif x > 320 and x < 400 and y == 100:
                    n = 0
                elif x > 320 and x < 380 and y == 200:
                    n = 0
                elif x > 440 and x < 640 and y == 220:
                    n = 0
                elif x > 440 and x < 640 and y == 260:
                    n = 0
                else:
                    y += step
     # limit the rectangle from going out of the visible area
    if (x < 0): x = 0
    elif (x > (640-step)): x = 640-step
    if (y < 0): y = 0
    elif (y > (480-step)): y = 480-step
    
    
    screen.fill(red)
    
    # Drawings start
    pygame.draw.rect(screen, black, ((x, y), (step, step)), 0)
    ##                             x ,y,left and right size,down and up size
    pygame.draw.rect(DISPLAY,blue,(20,20,20,500))
    pygame.draw.rect(DISPLAY,blue,(100,100,20,20))
    pygame.draw.rect(DISPLAY,tel_in,(200,200,20,20))
    pygame.draw.rect(DISPLAY,tel_in,(340,160,20,20))
    pygame.draw.rect(DISPLAY,tel_out,(340,200,20,20))
    pygame.draw.rect(DISPLAY,tel_out,(240,200,20,20))
    pygame.draw.rect(DISPLAY,die,(300,300,20,20))
    pygame.draw.rect(DISPLAY,blue,(100,220,200,20))
    # out of order pygame.draw.rect(DISPLAY,blue,(100,340,200,20))
    pygame.draw.rect(DISPLAY,blue,(100,260,240,20))
    pygame.draw.rect(DISPLAY,blue,(320,260,20,-200))
    pygame.draw.rect(DISPLAY,blue,(340,220,60,20))
    pygame.draw.rect(DISPLAY,blue,(380,220,20,-100))
    pygame.draw.rect(DISPLAY,blue,(380,120,-60,20))
    pygame.draw.rect(DISPLAY,key,(360,180,20,20))
    pygame.draw.rect(DISPLAY,end,(620,260,20,20))
    pygame.draw.rect(DISPLAY,hidden,(520,260,60,20))
    pygame.draw.rect(DISPLAY,blue,(460,240,180,20))
    pygame.draw.rect(DISPLAY,blue,(460,280,180,20))
    pygame.draw.rect(DISPLAY,blue,(460,260,20,20))
    pygame.draw.rect(DISPLAY,tel_in,(120,240,20,20))
    pygame.draw.rect(DISPLAY,tel_out,(480,260,20,20))
   # Drawing end
    if x == 120 and y == 240:
        x = 480
        y = 260
    if x == 200 and y == 200:
        x = 340
    if x == 300 and y == 300:
        print "You died!!!"
        pygame.quit()
        sys.exit()
    if x == 340 and y == 160:
        x = 240
        y = 200
    if event.type == pygame.MOUSEBUTTONDOWN:
        print "Your position is " , x , y
        time.sleep(0.09)
    if x == 620 and y == 260:
        if key1 == 1:
            print "You win"
            screen.blit(win_img, background_position)
            
        else:
            print "You need a key"
            screen.blit(nokey_img, background_position)
    if x == 360 and y ==180:
        
        screen.blit(key_img, background_position)
        key1 = 1
    #pygame.display.update()
    pygame.display.update()
    clock.tick(20)
    
