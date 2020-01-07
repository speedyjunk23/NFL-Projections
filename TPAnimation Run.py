##########################
#112 Term Project Animation Code 
##########################

import TPAnimationHelpers
import TPAlgorithms

# Updated Animation Starter Code from 112 website

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.stage = 1
    data.prospectHeight = ''
    data.prospectWeight = ''
    data.stat1 = ''
    data.stat2 = ''
    data.stat3 = ''
    data.digits = ['1','2','3','4','5','6','7','8','9','0','.']
    data.position = ''
    data.floor = ''
    data.expected = ''
    data.celling = ''
    data.round = ''
    data.conference = ''
    data.run = False
    data.expectedStats = None
    data.floorStats = None
    data.cellingStats = None
    data.stat1Multiplier = .33
    data.stat2Multiplier = .33
    data.stat3Multiplier = .33
    

def mousePressed(event, data):
    if data.stage != 1 and data.stage != 9:
        if (event.x <= data.width//8 and event.y <= data.height//10
            and event.x>0 and event.y>0):
            data.stage-=1
    if (data.stage == 3 or data.stage == 4 or data.stage == 6 
                        or data.stage == 7 or data.stage == 8):
        if (event.x >= data.width//2-data.width//10 and 
            event.x <= data.width//2+data.width//10 and 
            event.y >= data.height//10*9):
            data.stage += 1
    if data.stage == 9:
        if event.x <= data.width//8 and event.y <= data.height//10:
            data.stage=1
    if data.stage == 1: TPAnimationHelpers.stage1Mouse(event, data)
    if data.stage == 2: TPAnimationHelpers.stage2Mouse(event, data)
    if data.stage == 5: TPAnimationHelpers.stage5Mouse(event, data)
    
def keyPressed(event, data):
    if event.keysym == 'n':
        data.stage+=1
    if data.stage == 3:
        if str(event.char) in data.digits:
            data.prospectHeight+=(str(event.char))
        if event.keysym == 'BackSpace' and len(data.prospectHeight) != 0:
            data.prospectHeight=(
                            data.prospectHeight[0:len(data.prospectHeight)-1])
    if data.stage == 4:
        if str(event.char) in data.digits:
            data.prospectWeight+=(str(event.char))
        if event.keysym == 'BackSpace' and len(data.prospectWeight) != 0:
            data.prospectWeight=(
                            data.prospectWeight[0:len(data.prospectWeight)-1])
    if data.stage == 6:
        if str(event.char) in data.digits:
            data.stat1+=(str(event.char))
        if event.keysym == 'BackSpace' and len(data.stat1) != 0:
            data.stat1=(data.stat1[0:len(data.stat1)-1])
    if data.stage == 7:
        if str(event.char) in data.digits:
            data.stat2+=(str(event.char))
        if event.keysym == 'BackSpace' and len(data.stat2) != 0:
            data.stat2=(data.stat2[0:len(data.stat2)-1])
    if data.stage == 8:
        if str(event.char) in data.digits:
            data.stat3+=(str(event.char))
        if event.keysym == 'BackSpace' and len(data.stat3) != 0:
            data.stat3=(data.stat3[0:len(data.stat3)-1])

def timerFired(data):
    pass

def redrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height, fill = 'blue')
    canvas.create_text(data.width//2, data.height//5, 
    text = 'The NFL Draft: \n What Can You Expect?', font = 'COMICSANS 30',
    fill = 'red')
    if data.stage == 1:
        data.position = ''
        data.floor = ''
        data.expected = ''
        data.celling = ''
        data.round = ''
        data.conference = ''
        data.expectedStats = None
        data.floorStats = None
        data.cellingStats = None
        data.prospectHeight = ''
        data.prospectWeight = ''
        data.stat1 = ''
        data.stat2 = ''
        data.stat3 = ''
        TPAnimationHelpers.drawStage1(canvas, data)
    if data.stage == 2:
        TPAnimationHelpers.drawStage2(canvas, data)
    if data.stage == 3:
        TPAnimationHelpers.drawStage3(canvas, data)
    if data.stage == 4:
        TPAnimationHelpers.drawStage4(canvas, data)
    if data.stage == 5:
        TPAnimationHelpers.drawStage5(canvas, data)
    if data.stage == 6:
        TPAnimationHelpers.drawStage6(canvas, data)
    if data.stage == 7:
        TPAnimationHelpers.drawStage7(canvas, data)
    if data.stage == 8:
        TPAnimationHelpers.drawStage8(canvas, data)
        TPAlgorithms.multiplyCheck(data)
        data.run = True
    if data.stage == 9:
        if data.run == True:
            data.expected = TPAlgorithms.findSimilarPlayer(data)
            try:
                data.expectedStats = TPAlgorithms.grabNFL(data.expected)
                data.celling = TPAlgorithms.findCelling(data)
                data.cellingStats = TPAlgorithms.grabNFL(data.celling)
                data.floor = TPAlgorithms.findFloor(data)
                data.floorStats = TPAlgorithms.grabNFL(data.floor)
            except:
                pass
            data.run = False
            data.stat1Multiplier = .33
            data.stat2Multiplier = .33
            data.stat3Multiplier = .33
        TPAnimationHelpers.drawStage9(canvas, data)
        

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(750, 500)