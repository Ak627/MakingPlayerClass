import pygame
pygame.init()  
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((832, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3
SPACE = 4


class player:
    def __init__(self, x_offset, y_offset):
        self.xpos = 400
        self.ypos = 400
        self.vx = 0
        self.vy = 0
        self.isAlive = True
        self.xoffset = x_offset
        self.yoffset = y_offset
        
    def move(self, dire):

        if dire == LEFT:
            if self.xpos > 400:
                self.vx = -3
        
        elif dire == RIGHT:
            if self.xpos<400:
                self.vx=3
                
        else:
            self.vx = 0
            
        if dire == DOWN:
            if self.ypos<400:
                self.vy=3
                
        elif dire == UP:
            if self.ypos > 400:
                self.vy = -3
        else:
            self.vy = 0
            
        self.xpos += self.vx
        self.ypos += self.vy
        
#     def collision(self, map):
#         #down collision
#         if map[int((self.ypos-self.yoffset+frameHeight)/50)][int((self.xpos-self.xoffset+frameWidth/2)/50)]==2:
#             self.ypos-=3
#         #up collision
#         if map[int((self.ypos-self.yoffset)/50)][int((self.xpos-self.xoffset+frameWidth/2)/50)]==2:
#             self.ypos+=3     
#         #left collision
#         if map[int((self.ypos-self.yoffset+frameHeight-10)/50)][int((self.xpos-self.xoffset-10)/50)]==2 :
#             self.xpos+=3
#         #right collision
#         if map[int((self.ypos-self.yoffset)/50)][int((self.xpos-self.xoffset+frameWidth+5)/50)]==2:
#             self.xpos-=3
            
            
        #stop moving if you hit edge of screen (will be removed for scrolling)
        if self.xpos+frameWidth > 800:
            self.xpos-=3
        if self.xpos<0:
            self.xpos+=3
            
    #def attack(self):
    def draw(self):
        if self.isAlive == True:
            screen.blit(Link, (self.xpos, self.ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
            
    



#MAP: 1 is grass, 2 is tree
map = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2],
       [2, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2 ,0 ,0, 2,2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2 ,2 ,2, 2,2],
       [2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0 ,0 ,2, 2,2],
       [2, 0, 2, 2, 2, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 2,0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 3, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 2, 0, 0, 3, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 3, 0 ,0 ,0, 0,0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0 ,0 ,2, 2,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 3, 2, 0, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 2, 3, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0 ,0 ,3, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0 ,0 ,2, 2,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 3,2],
       [2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0 ,0 ,2, 2,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 2, 0, 2, 2, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 0,2],
       [2, 2, 3, 0, 2, 0, 0, 2, 0, 0, 2, 2, 2 ,2 ,0, 0,0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0 ,2 ,2, 0,2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2]]

tree = pygame.image.load('tree.png') #load your spritesheet
Link = pygame.image.load('link.png') #load your spritesheet
rock = pygame.image.load('Dwayne.png')
grass = pygame.image.load('Grass.png')
Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

#player variables
# xpos = 400 #xpos of player
# ypos = 400 #ypos of player
# vx = 0 #x velocity of player
# vy = 0 #y velocity of player
x_offset = 0
y_offset = 0
keys = [False, False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
movingx = False
movingy = False

#animation variables variables
frameWidth = 32
frameHeight = 46
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
direction = DOWN

p1 = player(x_offset, y_offset)

while not gameover:
    clock.tick(60) #FPS
   
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
     
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            elif event.key == pygame.K_UP:
                keys[UP]=True
            elif event.key == pygame.K_DOWN:
                keys[DOWN]=True
            elif event.key == pygame.K_SPACE:
                keys[SPACE] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False
            elif event.key == pygame.K_DOWN:
                keys[DOWN]=False
            elif event.key == pygame.K_SPACE:
                keys[SPACE] = False
         

    #LEFT MOVEMENT
    if keys[LEFT]==True:
        direction = LEFT
        p1.move(direction)
        if x_offset < 0:
            x_offset += 3
            p1.vx = 0
        RowNum = 0
        movingx = True
       
    #RIGHT MOVEMENT
    elif keys[RIGHT] == True:
        direction = RIGHT
        p1.move(direction)
        if x_offset>-800:
                x_offset-=3
                p1.vx = 0
        RowNum = 1
        movingx = True
        
    #turn off velocity
    else:
        movingx = False
       
    #DOWN MOVEMENT
    if keys[DOWN] == True:
        direction = DOWN
        p1.move(direction)
        if y_offset>-800:
                y_offset -=3
                p1.vy = 0
        RowNum = 1
        RowNum = 3
        movingy = True

         #UP MOVEMENT
    elif keys[UP]==True:
        direction = UP
        p1.move(direction)
        if y_offset<0:
                y_offset +=3
                p1.vy = 0
        RowNum = 0
        RowNum = 2
        movingy = True
    #turn off velocity
    else:
        movingy = False
       


   
    #COLLISION
        
#     p1.collision(map)


    #ANIMATION-------------------------------------------------------------------
       
    # Update Animation Information

    if movingx == True or movingy == True: #animate when moving
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
          frameNum+=1
        if frameNum>7:
           frameNum = 0
 
    # RENDER--------------------------------------------------------------------------------
    # Once we've figured out what frame we're on and where we are, time to render.
           
    screen.fill((51,117,70)) #wipe screen so it doesn't smear
   
    #draw map
    for i in range (28):
        for j in range(33):
            if map[i][j]==0:
                screen.blit(grass, (j*50+x_offset, i*50+y_offset), (0, 0, 50, 50))
            if map[i][j]==2:
                screen.blit(tree, (j*50+x_offset, i*50+y_offset), (0, 0, 50, 50))
            if map[i][j]==3:
                screen.blit(rock, (j*50+x_offset, i*50+y_offset), (0, 0, 50, 50))
        
    #draw player
    p1.draw()
    pygame.display.flip()#this actually puts the pixel on the screen
   
#end game loop------------------------------------------------------------------------------
pygame.quit()

