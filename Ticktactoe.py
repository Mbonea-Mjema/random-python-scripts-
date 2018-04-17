"""
Game      : TickTacToe
Written by: Mbonea Mjema
Year      : 2017
"""
#importing all the important mmodules and fuctions
import pygame,sys
from pygame.locals import *
from pygame.draw import line as Line
from pygame.display import update as sUpdate
from pygame.draw import rect as Rec
from time import time as pr
#initailize game
pygame.init()
#width and height of the window
Width = 800
Height =800
WindowDim=(Width,Height)

#Board dimensions
cellSize =150
vGap = Width/4-25
hGap = Height/4-25
midY = Height/2
midX = Width/2
x=vGap
y=hGap

#create a display surface

Window=pygame.display.set_mode(WindowDim)
#set caption of the window
pygame.display.set_caption("TickTacToe")
#create colours
BLUE = (0 , 0 , 255)
RED = (255 , 0 , 0)
BLACK= (0 ,0, 0)
GREEN =(44,42,47)
WHITE=(255,255,255)

#checking coordinates making sure not out of bound
def checkCords(x,y):
    if y>Height-vGap-cellSize:
        y=vGap
    if y<vGap:
       y=Height-vGap-cellSize
    if x>Width-hGap-cellSize:
        x=hGap
    if x<hGap:
        x=Width-hGap-cellSize
    return x,y
 
#Game records
turn=0
location=(0,0)
content=""
RECORD={}

#Title
text="TickTack Toe"
Title = pygame.font.Font('ARCADE.TTF', 70)
Titletext = Title.render('TickTack Toe', True, RED,BLACK)
textRectObj = Titletext.get_rect()
textRectObj.center = (midX-cellSize/2-20,50)

#draw board
def drawBoard():
    Line(Window,BLUE,(hGap,midY-cellSize/2),(Width-hGap,midY-cellSize/2),2)
    Line(Window,BLUE,(hGap,midY+cellSize/2),(Width-hGap,midY+cellSize/2),2)
    Line(Window,BLUE,(midX-cellSize/2,Height-vGap),(midX-cellSize/2,hGap),2)
    Line(Window,BLUE,(midX+cellSize/2,Height-vGap),(midX+cellSize/2,hGap),2)
    
#draw "X" or "O"
def write(data):
    if type(data)==dict: 
       for Location in data:
            Xcord,Ycord=Location
            cont=data[Location]
            text=pygame.font.Font('ARCADE.TTF', 120)
            letter =text.render(cont, True, WHITE,None)
            textR=letter.get_rect()
            textR.center=(Xcord+cellSize/2,Ycord+cellSize/2)
            Window.blit(letter, textR)
    if type(data)==tuple:
        if(data[2]==None):
            size=40
        else:
            size=data[2]
        if(data[3]==None):
            colour=RED
        else:
            colour=data[3]
        text=pygame.font.Font('ARCADE.TTF', size)
        letter =text.render(data[0], True, colour,None)
        textR=letter.get_rect()
        textR.center=(data[1])
        Window.blit(letter, textR)


#returns the game state either win,lose or draw
def checkWinner(db):
    doneX=[]
    doneY=[]
    for keyX,keyY in db.keys():
        wink=[]
        key1=keyX,keyY
        Xcount=1
        Ycount=1
        pdiag=1
        ndiag=1
        value=db[key1]
        wink.append(str(key1)+" reffernce")
        for keyX2,keyY2 in db.keys():
            key2=keyX2,keyY2
            if key1== key2:
                continue
            if(keyX!=keyX2 and keyY!=keyY2 and  db[key1]==db[key2]):
                if keyX2!=325:
                    slope=(keyY-keyY2)/(keyX-keyX2)
                    if(slope==-1):
                        pdiag+=1
                        wink.append(key2)
                    elif(slope==1):
                        ndiag+=1
                        wink.append(key2)
            if ((not keyX in doneX) and db[key1]==db[key2]) and keyX==keyX2:
                Xcount+=1
            if ((not  keyY in doneY) and db[key1]==db[key2]) and keyY==keyY2:
                Ycount+=1
        if(Xcount==3 or  Ycount==3 or ndiag==3 or pdiag==3):
                return db[key1]
        doneX.append(keyX)
        doneY.append(keyY)
    return None


#end of the game
def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == QUIT:      #event is quit 
            Terminate()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:   #event is escape key
                Terminate()
            elif event.key == K_r:
                return event.key   #key found return with it
    # no quit or key events in queue so return None    
    return None               


#custom event handler 
def Events(x,y,turn,location):
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            d=1
            if event.key==K_ESCAPE:
                Terminate()
            if event.key==K_r:
                RECORD.clear()
            if event.key==K_RETURN:
                 location=x,y
                 if  location not in RECORD :
                    if turn==1:
                        content="X"
                        turn=0 
                    else:
                        content="O"
                        turn=1
                    RECORD.setdefault(location,content)    
            if event.key==K_RIGHT:
                x+=cellSize
            if event.key==K_LEFT:
                x-=cellSize
            if event.key==K_UP:
                y-=cellSize
            if event.key==K_DOWN:
                y+=cellSize
        if event.type==QUIT:
            print(RECORD)
            Terminate()
        x,y=checkCords(x,y)
    return(x,y,turn)

  
#create a terminate fuction
def Terminate():
    pygame.quit()
    sys.exit()
#create a cube function
def drawCube(x,y):
    if int(start-pr())%2==0 or  blink==1:
        Rec(Window,GREEN,(x,y,cellSize,cellSize))
blink=0
start=pr()
even=lambda n :n%2==0
#Game loop
while True:
    blink=0
    if(even(turn)):
         ref="O"
    else:
        ref="X"
    message4=(ref +"'s turn" ,(325,hGap-30),40,WHITE)
    write(message4)
    message2=("Press r to restart or escape to quit ",(325,Height-hGap+60),20,WHITE)
    write(message2)
    Window.blit(Titletext, textRectObj)
    drawBoard()
    drawCube(x,y)
    x,y,turn=Events(x,y,turn,location)
    write(RECORD)
    winner=checkWinner(RECORD)
    if(winner!=None):
        message=(winner +" Won!!",(325,Height-hGap+30),None,None)
        write(message)
        while True:
            sUpdate()
            if checkForKeyPress():
                RECORD={}
                break
    if len(RECORD)==9:
        if (checkWinner(RECORD)==None):
            message3=("Draw",(325,Height-hGap+30),None,None)
            write(message3)
    sUpdate()
    Window.fill(BLACK)
