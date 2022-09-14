from tkinter import *
from random import *
from math import *
from math import pi
from time import *
from random import*
from fractions import*
root = Tk()

#FILL IT IN AND SCRAMBLE
s = Canvas(root, width=500, height=700, background="white")

#SET THEM VALUES
def setInitialValues():
    global goodScreen, badScreen #THE END GAME WHEN YOU LOSE OR WIN
    goodScreen=PhotoImage(file="goodGame.gif")
    badScreen=PhotoImage(file="badGame.gif")

    global barn #BACKGROUND
    barn=PhotoImage(file="barn.gif")
    
    global roomNum, xMouse, yMouse #NAVIGATION AND KEEPING TRACK OF WHERE YOU ARE
    roomNum=1 #game screen
    xMouse=0
    yMouse=0
    
    global xSpeed, ySpeed, gameOver, status, got #SPEED OF ARM, WORDS THAT SHOW UP ON SCREEN, KEEPING SCORE AND CHECKING FOR GAME RUNNING
    global stop, verticalmovement, clicknum #HELP CHECK BOUNDARIES
    stop=True
    verticalmovement=False
    clicknum=0
    
    got=False
    xSpeed=0
    ySpeed=0
    gameOver=False
    status=0

    global numOnScreen, numInArrays #KEEPING TRACK OF THE NUMBER OF FRUIT ON SCREEN AND IN THE ARRAYS
    numOnScreen=20
    numInArrays=numOnScreen


    global xBush, yBush, size, x1Bush, y1Bush, sizeB, xTree,yTree #THIS IS SETTING UP THE TREE AND THE BUSH THAT THE FRUIT ARE ON
    xBush=[]
    yBush=[]
    size=35

    x1Bush=[]
    y1Bush=[]
    sizeB=45

    xTree=[]
    yTree=[]
    
    for i in range (15):#bushes
        xBush.append(randint(50,140))
        yBush.append(randint(435,495))
        x1Bush.append(randint(320,420))
        y1Bush.append(randint(500,550))
    for r in range (25):
        xTree.append(randint(175,325))
        yTree.append(randint(200,300))
    

    global xFruitsB,yFruitsB,xFruitsb,yFruitsb,xFruitsT,yFruitsT #VALUES OF PLACEING MY FRUITS
    global xFruit, yFruit, Fruit ,numFruit #THE TOTAL NUMBER OF FRUIT EVERYWHERE AND TRACKING THEM
    xFruitsB=[]
    yFruitsB=[]
    xFruitsb=[]
    yFruitsb=[]
    xFruitsT=[]
    yFruitsT=[]

    xFruit=[]
    yFruit=[]
    Fruit=[]
    numFruit=20


    #I MADE 2 FOR LOOPS FOR THE SHRUBS INSTEAD OF 1 BECAUSE THE FRUIT ARRAY NEEDS 20  ZEROS IN IT TO START WITH
    for i in range (5): #MAKE VALUES FOR THE FRUIT IN SHRUB 
        one = randint(50,140)
        xFruitsB.append(one)
        
        two=randint(435,495)
        yFruitsB.append(two)

        xFruit.append(one)
        yFruit.append(two)
        Fruit.append(0)

    for i in range (5):# MAKE VALUES FOR FRUIT IN OTHER SHRUB
        three=randint(320,420)
        xFruitsb.append(three)
        
        four=randint(500,550)
        yFruitsb.append(four)
        
        xFruit.append(three)
        yFruit.append(four)
        Fruit.append(0)
        
    for r in range (10): #MAKE VALUES FOR FRUIT IN TREE
        one= randint(175,325)
        xFruitsT.append(one)

        two =randint(200,300)
        yFruitsT.append(two)

        xFruit.append(one)
        yFruit.append(two)
        Fruit.append(0)
        

    #THESE ARE MY FRUITS AND THEIR DRAWINGS
    global Lemon, Apple, Orange, Cherries, Pear
    global fruitPick
    Pear=PhotoImage(file="Pear.gif")
    Apple=PhotoImage(file="Apple.gif")
    Orange=PhotoImage(file="Orange.gif")
    Lemon=PhotoImage(file="Lemon.gif")
    Cherries=PhotoImage(file="Cherries.gif")
    
    fruitPick=[Pear,Apple,Orange,Lemon,Cherries] #WE RANDOMLY ASSIGN WHERE THEY GO

    #KEEPING TRACK OF WHERE THE ARM IS AND THE DIMENTIONS
    global xCrane,yCrane,x1Crane, y1Crane,width
    xCrane=230
    x1Crane=270
    yCrane=25
    y1Crane=50
    width=10

    #SCORES
    global printScore, addScore, score
    printScore=0
    addScore=0
    score=0

    #THE TIMER TIME FOR EACH LEVEL SELECTED
    global Mode,Timer, timeStart, clockDisplay
    if Mode=="Easy":
        Timer=125
    elif Mode=="Medium":
        Timer=60
    else:
        Timer=45

    timeStart = time()  #sets time start to when this function is called
    clockDisplay = s.create_text(700,750,text = "0", font = "Times 48", fill = "white")  

    
#DTAWING THE GAME BACKGROUND
def drawGameBackground():
    global xBush, yBush, size, x1Bush, y1Bush, bigsize, xTree,yTree
    s.create_rectangle(0,350,500,700, fill="#46a310") #GRASS
    s.create_rectangle (0,0,500,350, fill="#87ceeb") #THE SKY
    drawClouds()
    drawBarn()
    s.create_polygon(200,400,300,400,250,200, fill="brown", outline="brown") #THE TREE STUMP
    
    for i in range (15):#CREATE MY BUSHES
        s.create_oval(xBush[i]-size,yBush[i]-size,xBush[i]+size, yBush[i]+size, fill="green", outline="green")
        s.create_oval(x1Bush[i]-sizeB,y1Bush[i]-sizeB,x1Bush[i]+sizeB, y1Bush[i]+sizeB, fill="green", outline="green")
        
    for r in range (25):#CREATE THE TREE
        s.create_oval(xTree[r]-sizeB,yTree[r]-sizeB,xTree[r]+sizeB, yTree[r]+sizeB, fill="green", outline="green")

    global scoreText, score #CREATE THE SCORE ON THE SCREEN
    scoreText= s.create_text(370,130,text="Score:", font= "system 20", fill="black")
    score=s.create_text(450,130, text=str(printScore), font="system 26", fill="black")
    

def drawBarn(): #THE SMALL BARN IN THE BACK
    s.create_image(50,350, image=barn)


def drawClouds():#THE CLOUDS IN THE SKY
    cloudx=[]
    cloudx1=[]
    cloudx2=[]
    
    cloudy=[]
    cloudy1=[]
    cloudy2=[]

    rad=25
    
    for i in range (40):#MAKE THE CLOUD VALUES
        x=randint(25,100)
        x1= randint(230,290)
        x2=randint(400,475)

        y=randint(25,75)
        y1=randint(150,200)
        y2=randint(250,300)

        cloudx1.append(x)
        cloudx.append(x1)
        cloudx2.append(x2)

        cloudy.append(y)
        cloudy2.append(y1)
        cloudy1.append(y2)
        
    for r in range (40):#MAKE THE CLOUDS
        s.create_oval(cloudx[r]-rad, cloudy[r]-rad,cloudx[r]+rad,cloudy[r]+rad, fill="white", outline="white")
        s.create_oval(cloudx1[r]-rad, cloudy1[r]-rad,cloudx1[r]+rad,cloudy1[r]+rad, fill="white", outline="white")
        s.create_oval(cloudx2[r]-rad, cloudy2[r]-rad,cloudx2[r]+rad,cloudy2[r]+rad, fill="white", outline="white")

    
def setFruits():#PUT THE FRUITS IN THEIR POSITIONS

    #There are 2 arrays for the bush as I wanted to add the fruits in separately so I don't get confused later
    #BUSH
    for i in range (5):
        fu=choice(fruitPick)#THE FRUIT THAT WILL BE PLACED
        f=s.create_image(xFruitsB[i], yFruitsB[i], image=fu)#PLACE THE FRUIT
        Fruit[i]=f #ADD THE FRUIT INTO THE ARRAY TO TRACK IT

    #BUSH    
    for i in range (5):
        fu=choice(fruitPick)
        f=s.create_image(xFruitsb[i], yFruitsb[i], image=fu)
        Fruit[i+5]=f

    #TREE    
    for r in range (10):
        fu=choice(fruitPick)
        f=s.create_image(xFruitsT[r], yFruitsT[r], image=fu)
        Fruit[r+10]=f


#DRAWING THE ARM
def setCrane():
    drawCrane()

def drawCrane():
    global claw, Line
    claw=s.create_polygon(xCrane,yCrane,x1Crane,yCrane,x1Crane,y1Crane,x1Crane-15,y1Crane,x1Crane-15,y1Crane-10,x1Crane-25,y1Crane-10,
                     x1Crane-25,y1Crane,xCrane,y1Crane, fill="black")
    Line=s.create_line(((xCrane+x1Crane)/2), 0, ((xCrane+x1Crane)/2),yCrane,fill="black", width=width)


#update the crane postion and also the boundary checker  
def updateCranePosition():
    global xCrane, x1Crane, yCrane, y1Crane, xSpeed, ySpeed, stop, verticalmovement
    
    if yCrane>25:#if it's bigger than the starting value
        verticalmovement=True #it's moving vertically
        xSpeed=0 #there should be no horizontal movement
        stop=True #we should stop before it as it comes up

    if clicknum>0:#i've pressed an arrow key before
        if interrupt==True: #interrupt is true when the arm is bigger than the starting place and a key has been pressed
            verticalmovement=True
            xSpeed=0
            stop=True
    
    if yCrane<=25 and verticalmovement==True: #if my arm is smaller than the starting and it was moving vertically
        ySpeed=0
    
    if stop==False:
        ySpeed=ySpeed

    #updating the positions
    xCrane=xCrane+xSpeed
    x1Crane=x1Crane+xSpeed
    yCrane=yCrane+ySpeed
    y1Crane=y1Crane+ySpeed


#updating the Score
def updateScore():
    global score, printScore, xFruit, yFruit
    global status
    
    s.delete(score)#delete the old score
    
    if got==True:#if you got a fruit 
        status=s.create_text((xCrane),(yCrane), text="+5", font = "system 20", fill="black")#briefly show +5
        printScore=printScore+(5*GotNum)#sometimes you can get more than 1 fruit, so we update accordingly
        
    else:#if you didn't get a fruit
        status=s.create_text(xCrane,yCrane+10, text="Miss!", font = "system 20", fill="black")#tell the player that they missed

    #drawing the score
    score=s.create_text(450,130,text=str(printScore), font="system 24", fill="black")


#here is the space and the arrow keys
def keyPressDetector( event ):
    global xSpeed, ySpeed, interrupt, stop, verticalmovement, clicknum, roomNum

    #room num 1 is the game screen so these things only happen when you are playing the game
    if roomNum==1:#game screen
        stop=False
        verticalmovement=False#setting the values 
        interrupt=False
        clicknum=clicknum+1 #each time you press a key we add one
        
        if event.keysym=="Left": #if you pressed left
            
            if yCrane<=25:#if the arm is still in it's beginning place
                ySpeed=0
                
                if xCrane<=0:#if it's not on the screen
                    xSpeed=0
                    
                else:#if it's on the screen
                    xSpeed=-2
                    
            else:#if you pressed a key and it's not in the beginning stage you've interrupted it's rising back up
                interrupt=True
            

        elif event.keysym=="Right":#same as the left, but with right
            
            if yCrane<=25:
                ySpeed=0
                
                if x1Crane>=500:
                    xSpeed=0 
                else:
                    xSpeed=2
                    
            else: interrupt=True

        #if the down key is pressed            
        elif event.keysym=="Down":
            
            verticalMovement=True #the arm is moving vertically
            xSpeed=0 # we can't move horizontally
            
            if y1Crane>=700: #the arm should be on the screen if not this is what happens
                ySpeed=0
            else:
                ySpeed=5

                
        elif event.keysym=="space": #this is what happens when you press space
            if yCrane>=25:
                interrupt=True
                judgement()#pass judgement on weather or not a fruit has been picked

#judging if a fruit has been picked and how many
def judgement():
    global got, numOnScreen, numInArrays, xFruit, yFruit, Fruit, GotNum
    
    GotNum=0 #number of fruit picked
    got=False #no fruit has been picked  yet
    valBeforeLast=0 #things get complicate when more than 1 is picked
    iVal=[] #storing the i value so we know which to delete
    
    for i in range (numInArrays): #going through the number for fruit in the arrays
        
        if xCrane>=(xFruit[i]-40) and x1Crane<=(xFruit[i]+40) and yCrane>=(yFruit[i]-30) and y1Crane<=(yFruit[i]+50): #if the crane hand is around the area of a fruit
            got=True #we have a fruit
            s.delete(Fruit[i]) #delete the image of the fruit
            iVal.append(i) #the fruit that has been deleted
            GotNum=GotNum+1 #the number of fruit got in this one click
            numOnScreen=numOnScreen-1 #the number of fruit on the screen

    #if the number of fruit got is more than 1
    if len(iVal)>0:
        usedIVal=iVal[::-1] #reverse the array of iVal because things get complicated if you don't
        
        for r in range (len(iVal)): #going though and deleting all the ones that have been removed from screen
            numInArrays=numInArrays-1
            Fruit.remove(Fruit[usedIVal[r]])
            xFruit.remove(xFruit[usedIVal[r]])
            yFruit.remove(yFruit[usedIVal[r]])

    #update the score        
    updateScore()


#when a key is released
def keyUpHandler(event):
    global xSpeed, ySpeed, verticalmovement, roomNum

    #if we are on the game screen
    if roomNum==1:
        if event.keysym=="Down":
            verticalmovement=True
            xSpeed = 0
            ySpeed= -3 #auto bring the arm back up
            
        elif event.keysym=="Left" :
            xSpeed=0
            if interrupt==False:
                ySpeed=0
            else:
                ySpeed=-3
                
        elif event.keysym=="Right":
            xSpeed=0
            if interrupt==False:
                ySpeed=0
            else:
                ySpeed=-3
                
        elif event.keysym=="space":
            verticalmovement=True


#DRAWING MY TIMER THAT'S IN THE TOP RIGHT CORNER           
def drawGameClock(c):
    global clockDisplay, Clock

    s.delete(clockDisplay)
    timeleft=s.create_text(350, 75, text="Time left:", font="Times 24", fill="black")
    clockDisplay = s.create_text(450,75,text = str(round(Timer,1)) + " " + str(c), font = "Times 24", fill = "black")


#RUNNING THE GAME
def runGame():
    global gameOver, timeStart,timeNow, Timer
    easyButton.destroy()  #gets rid of all the buttons
    mediumButton.destroy()
    hardButton.destroy()
    instructionButton.destroy()

    #STARTING LEGIT GAME
    setInitialValues()
    drawGameBackground()
    setFruits()
    
    while gameOver==False:
        drawCrane()
        updateCranePosition()
        s.update()
        sleep(0.01)
        s.delete(status)
        s.delete(claw,Line)
        if numOnScreen==0 and numInArrays==0:
            gameOver=True
            GameOver()

        timeNow = time()  
        timeElaspedSinceLastCheck = timeNow-timeStart
        if timeElaspedSinceLastCheck >= 1:  #if 1 second has passed
            Timer = Timer -1  #the clock subtracts 1 for the count down
            drawGameClock("")  #draws the game clock count down
            timeStart = time()

        if Timer == 0:  #when the countdown clock reaches 0
            s.delete(all)
            gameOver = True
            GameOver()
    s.delete(all)
    GameOver()#PUT THIS TWICE BECAUSE IN THE UPDATE SCORE IT AUTO KICKS-OUT OF THE WHILE LOOP, SO I NEED TO PUT IT THERE TO CATCH THAT


#THIS IS FOR THE GAME OVER SCREEN TO PRESS ON THE OPTIONS
def mouseClickHandler(event):
    global xMouse, yMouse
    if roomNum==3:
        xMouse=event.x
        yMouse=event.y
        if xMouse<400 and xMouse>100 and yMouse<400 and yMouse>=50:
            playAgainButtonPressed()
        elif xMouse<=310 and xMouse>=190 and yMouse<=475 and yMouse>=425:
            quitButtonPressed()


#THIS IS WHAT HAPPENS WHEN YOU RUN OUT OF TIME OR FINISH GETTING ALL THE FRUIT    
def GameOver():
    global badScreen, goodScreen
    global roomNum
    roomNum=3
    
    if numOnScreen==0 and numInArrays==0:
       s.create_image(250,350, image=goodScreen)
    else:
        s.create_image(250,350, image=badScreen)
    

#WHEN THE QUIT OPTION IS PRESSED
def quitButtonPressed():
    global roomNum
    roomNum=4

    #CREATES THE LAST SCREEN YOU WILL SEE IF FOR THE GAME
    s.create_rectangle(0,0,500,700, fill="black")
    s.create_text(250,325, text="Thanks for Playing!", font ="Times 24", fill="white")
    s.create_text(250, 375, text="Bye!", font="Times 24", fill="white")

    s.update()
    sleep(3)#LETS YOU STARE FOR A BIT LONGER
    root.destroy()#CLOSES THE GAME


#WHEN THE PLAY AGAIN OPTION IS PRESSED
def playAgainButtonPressed():
    global gameOver
    gameOver = False
    
    introScreen()  #goes back to the intro screen


#STARTING SCREEN    
def introScreen():
    global Background, easyButton, mediumButton, hardButton, instructionButton, introductScreen
    global roomNum
    roomNum=0
        
    Background = PhotoImage(file = "Intro.gif")
    introductScreen=s.create_image(250,350,image=Background)

    #CREATE EASY BUTTON
    easyButton = Button(root,text = "Easy", font = "Times 24", command = easyButtonPressed, anchor = CENTER)  #button for easy mode
    easyButton.pack()
    easyButton.place(x = 190, y = 300, width = 150 , height = 50 )

    #CREATE MEDIUM BUTTON
    mediumButton = Button(root,text = "Medium", font = "Times 24", command = mediumButtonPressed, anchor = CENTER)  #button for normal mode
    mediumButton.pack()
    mediumButton.place(x = 190, y = 400, width = 150 , height = 50 )

    #CREATE HARD BUTTON
    hardButton = Button(root,text = "Hard", font = "Times 24", command = hardButtonPressed, anchor = CENTER)  #button for hard mode
    hardButton.pack()
    hardButton.place(x = 190, y = 500, width = 150 , height = 50 )

    #CREATE INSTRUCTION BUTTON
    instructionButton = Button(root,text = "Instructions", font = "Times 24", command = instructions, anchor = CENTER)  #button for instructions screen
    instructionButton.pack()
    instructionButton.place(x = 190, y = 600, width = 150 , height = 50 )


#WHEN THE EASY BUTTON IS PRESSED
def easyButtonPressed():
    global Mode
    Mode = "Easy" 
    runGame()


#WHEN THE NORMAL BUTTON IS PRESSED
def mediumButtonPressed():
    global Mode
    Mode = "Medium"
    runGame()


#WHEN THE HARD BUTTON IS PRESSED
def hardButtonPressed():
    global Mode
    Mode = "Hard"
    runGame()


#FUNCTION FOR INSTRUCTIONS SCREEN (WHEN THE INSTRUCTIONS BUTTON IS PRESSED)
def instructions():
    global Instructions, introScreenButton, instructScreen
    global roomNum
    roomNum=2 #SCREEN NUMBER
    
    s.delete(introductScreen)
    easyButton.destroy()  #gets rid of previous screen's buttons
    mediumButton.destroy()
    hardButton.destroy()
    instructionButton.destroy()
    
    Instructions = PhotoImage(file = "Instructions.gif")#GET THE CUREENT SCREEN'S STUFF
    instructScreen=s.create_image(250,350,image=Instructions)
                                    
    introScreenButton = Button(root,text = "Back", font = "Times 24", command = introScreenButtonClicked, anchor = CENTER)  #creates button to go back to the introscreen
    introScreenButton.pack()
    introScreenButton.place(x = 215, y = 550, width = 100 , height = 50)


#FUNCTION FOR GOING BACK TO THE INTRO SCREEN FROM THE INSTRUCTIONS SCREEN
def introScreenButtonClicked():
    introScreenButton.destroy()  #this is done so that a loop can be maintained while deleting the previous screen's button
    introScreen()

  
#STARTS AT INTROSCREEN THEN GOES TO RUNGAME
root.after(0, introScreen)


#BINDING MY KEYS AND MOUSE        
s.bind( "<Key>", keyPressDetector )
s.bind( "<KeyRelease>", keyUpHandler)
s.bind("<Button-1>", mouseClickHandler)


s.focus_set()   #Makes Python pay attention to mouse clicks & keystrokes that happen onscreen
s.pack()          #Puts the screen together
root.mainloop()    
