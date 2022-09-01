import pygame
import random
import sys
import time
from math import atan , pi
from menu import character_selected

pygame.init()

screen = pygame.display.set_mode((800, 600))
# Each block of the matrix is 30 by 30 pixels
# map looks like this:, '#' represents a gate
'''
0 0 0 0   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0   0 0 
0 0 0 0   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0   0 0 
0                           0 0 0 0         0 0 
0   0 0 0 0   0 0   0 0 0   0 0 0 0   0 0   0 0 
0   0 0 0 0   0 0   0 0 0   0 0 0 0   0 0   0 0 
0   0 0 0 0   0 0   0 0 0   0 0 0 0   0 0   0 0 
0           #             #                 0 0 
0   0 0 0 0   0 0 0 0 0 0   0 0   0 0 0 0   0 0 
0   0 0 0 0   0 0 0 0 0 0   0 0   0 0 0 0   0 0 
0   0 0 0 0                 0 0             0 0 
    0 0 0 0   0 0 0   0 0 0 0 0   0 0 0 0       
0   0 0 0 0   0 0 0   0 0 0 0 0   0 0 0 0   0 0 
0   0 0 0 0   0 0 0   0 0 0 0 0   0 0 0 0   0 0 
0                   #                       0 0 
0   0 0   0 0 0 0 0   0 0   0 0 0 0   0 0   0 0 
0   0 0   0 0 0 0 0   0 0   0 0 0 0   0 0   0 0 
0   0 0   0 0 0 0 0   0 0   0 0 0 0   0 0   0 0 
0         0 0 0 0 0                         0 0 
0 0 0 0   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0   0 0 
0 0 0 0   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0   0 0
'''
map = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
    ]


BG = pygame.image.load("pics/BG2.png")  # Background image variable
reloadtop = pygame.image.load("pics/reloadtop.png")
reloadbottom = pygame.image.load("pics/reloadbottom.png")
reloadBar = pygame.image.load("pics/ReloadBar.png")

screen.blit(BG, (0, 0))
pygame.display.update()
red = (255, 0, 0)
score = 0
tenPts = [(330, 180),(540,120),(570,390)]
twentyPts = [(30,240),(540,270)]
fiftyPts = [(240,390),(480, 510),(600,180)]
hundredPts = [(360,270),(450,390)]
gameOver = False
finalScoreStr = ''
totalScore = len(tenPts) * 10 + len(twentyPts) * 20 + len(fiftyPts) * 50 + len(hundredPts) * 100
startTime = time.time()
running = True


def loadPts(p, pts):
    for crt in pts:
        screen.blit(p, crt)


# Returns index of the coordinate player collided with
def gainedPts(pts):
    collided = False
    for i in range(len(pts)):
        tup = pts[i]
        if (c_x == tup[0]) and (c_y == tup[1]):
            collided = True
            break
    if collided:
        return i
    else:
        return -1



# define a function for
# collision detection
def crash():
    # check conditions
    global score
    global gameOver
    global finalScoreStr
    retVal = gainedPts(tenPts)
    if retVal != -1:
        del tenPts[retVal]
        score += 10

    retVal = gainedPts(twentyPts)
    if retVal != -1:
        del twentyPts[retVal]
        score += 20

    retVal = gainedPts(fiftyPts)
    if retVal != -1:
        del fiftyPts[retVal]
        score += 50

    retVal = gainedPts(hundredPts)
    if retVal != -1:
        del hundredPts[retVal]
        score += 100

    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf = largeText.render('Score : ' + str(score), True, red)  # text_objects('Choose Player', largeText)
    TextRect = TextSurf.get_rect()
    TextRect.center = ((720 * 0.51), (20))
    screen.blit(TextSurf, TextRect)
    if score == totalScore and (time.time()-startTime) <= 45 and gameOver == False:
        finalScoreStr = 'Total score with Bonus : '+str(int((45/(time.time()-startTime))*score))
        TextSurf = largeText.render(finalScoreStr, True, red) #text_objects('Choose Player', largeText)
        TextRect = TextSurf.get_rect()
        TextRect.center = ((720 * 0.51),(40))
        screen.blit(TextSurf, TextRect)
        gameOver = True
    elif score == totalScore and (time.time()-startTime) > 45 and gameOver == False:
        finalScoreStr = 'Total score after penalty : '+str(int((45/(time.time()-startTime))*score))
        TextSurf = largeText.render(finalScoreStr, True, red) #text_objects('Choose Player', largeText)
        TextRect = TextSurf.get_rect()
        TextRect.center = ((720 * 0.51),(40))
        screen.blit(TextSurf, TextRect)
        gameOver = True
    elif gameOver == True:
        finalScoreStr = str(score)
        TextSurf = largeText.render(finalScoreStr, True, red) #text_objects('Choose Player', largeText)
        TextRect = TextSurf.get_rect()
        TextRect.center = ((720 * 0.51),(40))
        screen.blit(TextSurf, TextRect)

#Reload Bar
Charged = False
rbar_x , rbar_y = 745,400
# coordinates of reload bar image
rspeed = 0.5
#speed of reload , must be divisor of 200

def reload():
    global rbar_x,rbar_y,rspeed,Charged , speedc
    if rbar_y < 350:
        speedc = 2
    if rbar_y > 200:
        rbar_y -= rspeed
    else:
        Charged = True
    screen.blit(reloadtop, (720, 0))
    screen.blit(reloadBar,(rbar_x,rbar_y))
    screen.blit(reloadbottom,(720,400))


def super():
    global rbar_y,Charged , speedc
    speedc = 0
    Charged = False
    rbar_y = 400


# movement controls  and functions
def down():
    global char_y, c_y, char_x, c_x, speed
    c_y += speed
    #screen.blit(BG, (0, 0))
    #screen.blit(char, (c_x, c_y))


def up():
    global char_y, c_y, char_x, c_x, speed
    c_y -= speed
    #screen.blit(BG, (0, 0))
    #screen.blit(char, (c_x, c_y))


def left():
    global char_y, c_x, char_x, c_y, speed
    c_x -= speed
    #screen.blit(BG, (0, 0))
    #screen.blit(char, (c_x, c_y))


def right():
    global char_y, c_x, char_x, c_y, speed
    c_x += speed
    #screen.blit(BG, (0, 0))
    #screen.blit(char, (c_x, c_y))


def movechoice():
    global lastcall, lc, wx1, wy1, c_x, c_y, char_y, char_x
    if event.key == pygame.K_LEFT:
        if map[char_y][(char_x - 1) % 24] == 0 and ((char_x, char_y), (char_x - 1, char_y)) not in blocked:
            lastcall = True
            lc = left
        else:
            pass
    elif event.key == pygame.K_RIGHT:
        if map[char_y][(char_x + 1) % 24] == 0 and ((char_x, char_y), (char_x + 1, char_y)) not in blocked:
            lastcall = True
            lc = right
        else:
            pass
    elif event.key == pygame.K_DOWN:
        if map[(char_y + 1) % 20][char_x] == 0 and ((char_x, char_y), (char_x, char_y + 1)) not in blocked:
            lastcall = True
            lc = down
        else:
            pass
    elif event.key == pygame.K_UP:
        if map[(char_y - 1) % 20][char_x] == 0 and ((char_x, char_y), (char_x, char_y - 1)) not in blocked:
            lastcall = True
            lc = up
        else:
            pass
    wall1()
    wall2()
    wall3()


def move(lc):
    wall1()
    wall2()
    wall3()
    lc()


# speed variable , must be divisor of 30
speed = 3
speedc = 2 # speed of chaser
# gate , located at (7,7),(14,7),(11,14)
gateh = pygame.image.load("pics/Gate2h.png") # horizontal
gatev = pygame.image.load("pics/Gate2v.png") # vertical

blocked = [()] * 6

# function for wall 1
def wall1():
    global w1
    if w1 == 1:
        screen.blit(gatev, (210, 180))
        blocked[0:2] = [((6, 6), (7, 6)), ((7, 6), (6, 6))]
    elif w1 == 2:
        screen.blit(gateh, (180, 176))
        blocked[0:2] = [((6, 6), (6, 5)), ((6, 5), (6, 6))]
    elif w1 == 3:
        screen.blit(gateh, (180, 210))
        blocked[0:2] = [((6, 6), (6, 7)), ((6, 7), (6, 6))]
    else:
        screen.blit(gatev, (176, 180))
        blocked[0:2] = [((6, 6), (5, 6)), ((5, 6), (6, 6))]
w1 = random.randint(1, 4)
wall1()


# function for wall 2
def wall2():
    global w2
    if w2 == 1:
        screen.blit(gatev, (420, 180))
        blocked[2:4] = [((13, 6), (14, 6)), ((14, 6), (13, 6))]
    elif w2 == 2:
        screen.blit(gateh, (390, 176))
        blocked[2:4] = [((13, 6), (13, 5)), ((13, 5), (13, 6))]
    elif w2 == 3:
        screen.blit(gateh, (390, 210))
        blocked[2:4] = [((13, 6), (13, 7)), ((13, 7), (13, 6))]
    else:
        screen.blit(gatev, (386, 180))
        blocked[2:4] = [((13, 6), (12, 6)), ((12, 6), (13, 6))]
w2 = random.randint(1, 4)


# function for wall 3
def wall3():
    global w3
    if w3 == 1:
        screen.blit(gatev, (330, 390))
        blocked[4:] = [((10, 13), (11, 13)), ((11, 13), (10, 13))]
    elif w3 == 2:
        screen.blit(gateh, (300, 386))
        blocked[4:] = [((10, 13), (10, 12)), ((10, 12), (10, 13))]
    elif w3 == 3:
        screen.blit(gateh, (300, 420))
        blocked[4:] = [((10, 13), (10, 14)), ((10, 14), (10, 13))]
    else:
        screen.blit(gatev, (296, 390))
        blocked[4:] = [((10, 13), (9, 13)), ((9, 13), (10, 13))]
w3 = random.randint(1, 4)
t = 0


if character_selected=='Angry Cat   ':
    characterimage="pics/ANGRY CAT.png"
elif character_selected=="Yee Dinosaur":
    characterimage="pics/YEE.png"
elif character_selected=="Stonks Man":
    characterimage="pics/STONKS.png"


# Character basics
char = pygame.image.load(characterimage)
p10 = pygame.image.load("pics/10p(2).png")
p20 = pygame.image.load("pics/20p(2).png")
p50 = pygame.image.load("pics/50p(2).png")
p100 = pygame.image.load("pics/100p(2).png")

# char_x = characters x coordinate on matrix map
# char_y = characters y coordinate on matrix map
# c_x = actual coordinate of character in pygame screen
# c_y = actual coordinate of character in pygame screen
char_x, char_y = 4, 2
c_x, c_y = 120, 60
screen.blit(char, (c_x, c_y))

run, lastcall = 0, False
enteredLoop = False


#Chaser code
chaser = pygame.image.load('pics/GHOST.png')
chaser_x,chaser_y = 21,17
chas_x , chas_y = 21*30,17*30
screen.blit(chaser, (chas_x, chas_y))
runc = 0

def angle():
    global char_x,char_y,chaser_x,chaser_y
    dispx , dispy = (char_x - chaser_x),(char_y - chaser_y)
    #print(atan(-dispy/dispx))
    #print(dispx,dispy)
    theta = 0
    if dispx == 0 and dispy < 0:# straigh above
        theta = pi/2
    elif dispx == 0 and dispy > 0:# straight below
        theta = -1*pi/2
    elif dispx > 0 and dispy == 0:# exact right
        theta = 0
    elif dispx < 0 and dispy == 0:# exact left
        theta = -1*pi
    elif dispx > 0 and dispy < 0:# First quadrant
        theta = atan(-dispy / dispx)
    elif dispx < 0 and dispy < 0:# Second quadrant
        theta = atan(-dispy / dispx) + pi
    elif dispx < 0 and dispy > 0:# Third quadrant
        theta = atan(-dispy / dispx) - pi
    elif dispx > 0 and dispy > 0:# fourth quadrant
        theta = atan(-dispy / dispx)
    return theta

def downchaser():
    global chas_y, chas_x, speedc
    chas_y += speedc
    screen.blit(chaser, (chas_x, chas_y))


def upchaser():
    global chas_y,chas_x, speedc
    chas_y -= speedc
    screen.blit(chaser, (chas_x, chas_y))


def leftchaser():
    global chas_x, chas_y, speedc
    chas_x -= speedc
    screen.blit(chaser, (chas_x, chas_y))


def rightchaser():
    global  chas_x, chas_y, speedc
    chas_x += speedc
    screen.blit(chaser, (chas_x, chas_y))

def checkjunction():
    try:
        x1 = map[chaser_y+1][chaser_x]
    except:
        x1 = 1
    try:
        x2 = map[chaser_y-1][chaser_x]
    except:
        x2 = 1
    try:
        x3 = map[chaser_y][chaser_x+1]
    except:
        x3 = 1
    try:
        x4 = map[chaser_y][chaser_x-1]
    except:
        x4 = 1
    if  x1 + x2 + x3 + x4 <= 1 or (x1+x2+x3+x4 >= 2 and x1 != x2):
        returnval = [True]
        if x1 == 0:
            returnval.append('down')
        if x2 == 0:
            returnval.append('up')
        if x3 == 0:
            returnval.append('right')
        if x4 == 0:
            returnval.append('left')
        return returnval
    else:
        return [False]

lastcallchaser = None

def selectpath(returnval):
    thet = angle()
    #print(thet)
    minv = 10
    direction = None
    if 'down' in returnval:
        val = abs(thet + pi/2)
        if val < minv:
            minv = val
            direction = 'down'

    if 'up' in returnval:
        val = abs(thet - pi/2)
        if val < minv:
            minv = val
            direction = 'up'

    if 'right' in returnval:
        val = abs(thet)
        if val < minv:
            minv = val
            direction = 'right'

    if 'left' in returnval:
        val = min(abs(thet-pi),abs(thet+pi))
        if val < minv:
            minv = val
            direction = 'left'
    return direction





while running:
    screen.blit(BG, (0, 0))
    pygame.time.wait(5)

    if lastcall == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if lastcall == False and event.type == pygame.KEYDOWN:
                movechoice()
                if event.key == pygame.K_SPACE and Charged == True:
                    super()


    if time.perf_counter() - t > 3:
        t = time.perf_counter()
        w1 = random.randint(1, 4)
        w2 = random.randint(1, 4)
        w3 = random.randint(1, 4)
    wall1()
    wall2()
    wall3()
    c_x = c_x % 720
    c_y = c_y % 600
    char_x = char_x % 24
    char_y = char_y % 20
    screen.blit(char, (c_x, c_y))
    reload()

    loadPts(p10, tenPts)
    loadPts(p20, twentyPts)
    loadPts(p50, fiftyPts)
    loadPts(p100, hundredPts)
    crash()

    if lastcallchaser == 'left':
        leftchaser()
    elif lastcallchaser == 'right':
        rightchaser()
    elif lastcallchaser == 'down':
        downchaser()
    elif lastcallchaser == 'up':
        upchaser()
    runc += speedc
    if runc == 30:
        runc = 0
        if lastcallchaser == 'up':
            chaser_y -= 1
        elif lastcallchaser == 'down':
            chaser_y += 1
        elif lastcallchaser == 'right':
            chaser_x += 1
        elif lastcallchaser == 'left':
            chaser_x -= 1
        if checkjunction()[0] == True:
            lastcallchaser = selectpath(checkjunction()[1:])


    if lastcall == True:
        move(lc)
        run += speed
        if run >= 30:
            run = 0
            lastcall = False
            if lc == up:
                char_y -= 1
            elif lc == down:
                char_y += 1
            elif lc == right:
                char_x += 1
            elif lc == left:
                char_x -= 1

    pygame.display.update()
    if score == 420 or (char_x == chaser_x and char_y == chaser_y):
        fh = open('score.txt','w')
        fh.write(finalScoreStr)
        fh.close()
        import end
        #pygame.quit()
        #sys.exit()