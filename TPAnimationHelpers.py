##########################
#112 Term Project Animation Helpers 
##########################

def drawStage1(canvas, data):
    canvas.create_text(data.width//2, data.height//5*2, 
    text = 'Select a Position:', font = 'COMICSANS 25', fill = 'white')
    canvas.create_text(data.width//7*2, data.height//8*5, 
                        text = 'QB', fill = 'white', font = 'COMICSANS 25')
    canvas.create_text(data.width//7*3, data.height//8*5, 
                        text = 'RB', fill = 'white', font = 'COMICSANS 25')
    canvas.create_text(data.width//7*4, data.height//8*5, 
                        text = 'WR', fill = 'white', font = 'COMICSANS 25')
    canvas.create_text(data.width//7*5, data.height//8*5, 
                        text = 'TE', fill = 'white', font = 'COMICSANS 25')
    canvas.create_text(data.width//6*2, data.height//8*6, 
                        text = 'DL', fill = 'white', font = 'COMICSANS 25')
    canvas.create_text(data.width//6*3, data.height//8*6, 
                        text = 'LB', fill = 'white', font = 'COMICSANS 25')
    canvas.create_text(data.width//6*4, data.height//8*6, 
                        text = 'DB', fill = 'white', font = 'COMICSANS 25')
 
def drawBack(canvas, data): 
    canvas.create_rectangle(0,0,data.width//8,data.height//10, fill = 'white')
    canvas.create_text(data.width//16,data.height//20, 
                        text = 'Back', font = 'COMICSANS 20')
    
def drawTry(canvas, data): 
    canvas.create_rectangle(0,0,data.width//8,data.height//10, fill = 'white')
    canvas.create_text(data.width//16,data.height//20, 
                        text = 'Try Again?', font = 'COMICSANS 15')
                        
def drawNext(canvas, data):
    canvas.create_rectangle(data.width//2-data.width//10,data.height//10*9,
                    data.width//2+data.width//10,data.height, fill = 'white')
    canvas.create_text(data.width//2,data.height//20*19, 
                        text = 'Next', font = 'COMICSANS 20')
                        
def drawStage2(canvas, data):
    drawBack(canvas, data)
    canvas.create_text(data.width//2, data.height//5*2, fill = 'white',
                    text = 'What Is The Projected Round?', 
                    font = 'COMICSANS 25')
    canvas.create_text(data.width//14*4, data.height//16*11, text = '1', 
                        font = 'COMICSANS 25')
    canvas.create_text(data.width//14*5, data.height//16*11, text = '2', 
                        font = 'COMICSANS 25')
    canvas.create_text(data.width//14*6, data.height//16*11, text = '3', 
                        font = 'COMICSANS 25')
    canvas.create_text(data.width//14*7, data.height//16*11, text = '4', 
                        font = 'COMICSANS 25')
    canvas.create_text(data.width//14*8, data.height//16*11, text = '5', 
                        font = 'COMICSANS 25')
    canvas.create_text(data.width//14*9, data.height//16*11, text = '6', 
                        font = 'COMICSANS 25')
    canvas.create_text(data.width//14*10, data.height//16*11, text = '7', 
                        font = 'COMICSANS 25')
    
def drawStage3(canvas, data):
    drawBack(canvas, data)
    drawNext(canvas, data)
    canvas.create_text(data.width//2, data.height//5*2, fill = 'white',
    text = 'Please Enter Height: \n               (cm)\n          (just type!)',
     font = 'COMICSANS 25')
    canvas.create_text(data.width//2, data.height//16*11, 
    text = data.prospectHeight, font = 'COMICSANS 25', fill = 'white')
    
def drawStage4(canvas, data):
    drawBack(canvas, data)
    drawNext(canvas, data)
    canvas.create_text(data.width//2, data.height//5*2, fill = 'white',
                    text = 'Please Enter Weight: \n               (kg)', 
                    font = 'COMICSANS 25')
    canvas.create_text(data.width//2, data.height//16*11, 
    text = data.prospectWeight, font = 'COMICSANS 25', fill = 'white')
    
def drawStage5(canvas, data):
    drawBack(canvas, data)
    canvas.create_text(data.width//2, data.height//5*2, fill = 'white',
                    text = 'Conference:', font = 'COMICSANS 25')
    canvas.create_text(data.width//6*2, data.height//16*11, text = 'Major', 
                        font = 'COMICSANS 25')
    canvas.create_text(data.width//6*4, data.height//16*11, text = 'Non-Major', 
                        font = 'COMICSANS 25')
    
def drawStage6(canvas, data):
    if data.position == 'QB': 
        stat1 = 'Cmp %'
    if data.position == 'RB': 
        stat1 = 'Carries/Games'
    if data.position == 'WR' or  data.position == 'TE': 
        stat1 = 'Rec/Game'
    if data.position == 'DL' or data.position == 'LB' or data.position == 'DB':
        stat1 = 'Tackles/Game'
    drawBack(canvas, data)
    drawNext(canvas, data)
    canvas.create_text(data.width//2, data.height//5*2, fill = 'white',
                    text = 'Please Enter \n' + stat1, font = 'COMICSANS 25')
    canvas.create_text(data.width//2, data.height//16*11, 
    text = data.stat1, font = 'COMICSANS 25', fill = 'white')
    
def drawStage7(canvas, data):
    if data.position == 'QB': 
        stat2 = 'TD:INT Ratio'
    if data.position == 'RB': 
        stat2 = 'Yards/Carry'
    if data.position == 'WR' or data.position == 'TE': 
        stat2 = 'Yards/Rec'
    if data.position == 'DL' or data.position == 'LB': 
        stat2 = 'Sacks/Game'
    if data.position == 'DB': 
        stat2 = 'INTs/Game'
    drawBack(canvas, data)
    drawNext(canvas, data)
    canvas.create_text(data.width//2, data.height//5*2, fill = 'white',
                    text = 'Please Enter \n' + stat2, font = 'COMICSANS 25')
    canvas.create_text(data.width//2, data.height//16*11, 
    text = data.stat2, font = 'COMICSANS 25', fill = 'white')
    
def drawStage8(canvas, data):
    if data.position == 'QB': 
        stat3 = 'Games Played'
    if data.position == 'RB': 
        stat3 = 'TDs/Carry'
    if data.position == 'WR' or data.position == 'TE': 
        stat3 = 'TDs/Rec'
    if data.position == 'DL' or data.position == 'LB' or data.position == 'DB': 
        stat3 = 'Forced Fumbles/Game'
    drawBack(canvas, data)
    drawNext(canvas, data)
    canvas.create_text(data.width//2, data.height//5*2, fill = 'white',
                    text = 'Please Enter \n' + stat3, font = 'COMICSANS 25')
    canvas.create_text(data.width//2, data.height//16*11, 
    text = data.stat3, font = 'COMICSANS 25', fill = 'white')
    
    
def drawStage9(canvas, data):
    drawTry(canvas, data)
    if data.expected != '':
        if data.position == 'QB': 
            stat1, stat2, stat3 = 'Cmp %', 'TD:INT', 'GP'
        if data.position == 'RB': 
            stat1, stat2, stat3 = 'CPG', 'YPC', 'TDPC'
        if data.position == 'WR' or data.position == 'TE': 
            stat1, stat2, stat3 = 'RPG', 'YPR', 'TDPR'
        if data.position == 'DL' or data.position == 'LB': 
            stat1, stat2, stat3 = 'TPG', 'SPG', 'FFPG'
        if data.position == 'DB': 
            stat1, stat2, stat3 = 'TPG', 'INTPG', 'FFPG'
        canvas.create_text(data.width//16*1, data.height//5*3, fill = 'white',
                        text = ''+'\n'+''+'\n'+stat1+'\n'+stat2+'\n'+stat3, 
                        font = 'COMICSANS 25')
        canvas.create_text(data.width//8*2, data.height//5*3, fill = 'white',
                        text = 'Floor\n' + data.floor + '\n' + 
                        statRound(data.floorStats[0])+ '\n' + 
                        statRound(data.floorStats[1])+ '\n' + 
                        statRound(data.floorStats[2]), font = 'COMICSANS 25')
        canvas.create_text(data.width//8*4, data.height//5*3, fill = 'white',
                        text = 'Expected\n' + data.expected + '\n' + 
                        statRound(data.expectedStats[0])+ '\n' + 
                        statRound(data.expectedStats[1])+ '\n' + 
                        statRound(data.expectedStats[2]), font = 'COMICSANS 25')
        canvas.create_text(data.width//8*6, data.height//5*3, fill = 'white',
                        text = 'Celling\n' + data.celling + '\n' + 
                        statRound(data.cellingStats[0])+ '\n' + 
                        statRound(data.cellingStats[1])+ '\n' + 
                        statRound(data.cellingStats[2]), font = 'COMICSANS 25')
    else:
        canvas.create_text(data.width//2, data.height//5*3, fill = 'white',
                    text = """Sorry, we haven't seen a player with a similar 
                    position, round, height, and weight.""" , 
                    font = 'COMICSANS 25')
        canvas.create_text(data.width//2, data.height//5*4, fill = 'white',
                    text = """Feel free to try again! (Top Left Corner)""" , 
                    font = 'COMICSANS 25')
                    
def statRound(int):
    int = int*1000
    int = int//1
    int = int/1000
    return str(int)
    
def stage1Mouse(event, data):
    if (event.x >= data.width//7*2-8 and event.x <= data.width//7*2+8 
    and event.y<=data.height//8*5+10 and event.y >= data.height//8*5-10):
        data.stage +=1
        data.position = 'QB'
    if (event.x >= data.width//7*3-8 and event.x <= data.width//7*3+8 
    and event.y<=data.height//8*5+10 and event.y >= data.height//8*5-10):
        data.stage +=1
        data.position = 'RB'
    if (event.x >= data.width//7*4-8 and event.x <= data.width//7*4+8 
    and event.y<=data.height//8*5+10 and event.y >= data.height//8*5-10):
        data.stage +=1
        data.position = 'WR'
    if (event.x >= data.width//7*5-8 and event.x <= data.width//7*5+8 
    and event.y<=data.height//8*5+10 and event.y >= data.height//8*5-10):
        data.stage +=1
        data.position = 'TE'
    if (event.x >= data.width//6*2-8 and event.x <= data.width//6*2+8 
    and event.y<=data.height//8*6+10 and event.y >= data.height//8*6-10):
        data.stage +=1
        data.position = 'DL'
    if (event.x >= data.width//6*3-8 and event.x <= data.width//6*3+8 
    and event.y<=data.height//8*6+10 and event.y >= data.height//8*6-10):
        data.stage +=1
        data.position = 'LB'
    if (event.x >= data.width//6*4-8 and event.x <= data.width//6*4+8 
    and event.y<=data.height//8*6+10 and event.y >= data.height//8*6-10):
        data.stage +=1
        data.position = 'DB'
        
def stage2Mouse(event, data):
    if (event.x >= data.width//14*4-10 and event.x <= data.width//14*4+10 
    and event.y<=data.height//16*11+10 and event.y >= data.height//16*11-10):
        data.stage +=1
        data.round = '1'
    if (event.x >= data.width//14*5-10 and event.x <= data.width//14*5+10 
    and event.y<=data.height//16*11+10 and event.y >= data.height//16*11-10):
        data.stage +=1
        data.round = '2'
    if (event.x >= data.width//14*6-10 and event.x <= data.width//14*6+10 
    and event.y<=data.height//16*11+10 and event.y >= data.height//16*11-10):
        data.stage +=1
        data.round = '3'
    if (event.x >= data.width//14*7-10 and event.x <= data.width//14*7+10 
    and event.y<=data.height//16*11+10 and event.y >= data.height//16*11-10):
        data.stage +=1
        data.round = '4'
    if (event.x >= data.width//14*8-10 and event.x <= data.width//14*8+10 
    and event.y<=data.height//16*11+10 and event.y >= data.height//16*11-10):
        data.stage +=1
        data.round = '5'
    if (event.x >= data.width//14*9-10 and event.x <= data.width//14*9+10 
    and event.y<=data.height//16*11+10 and event.y >= data.height//16*11-10):
        data.stage +=1
        data.round = '6'
    if (event.x >= data.width//14*10-10 and event.x <= data.width//14*10+10 
    and event.y<=data.height//16*11+10 and event.y >= data.height//16*11-10):
        data.stage +=1
        data.round = '7'
        
def stage5Mouse(event, data):
    if (event.x >= data.width//6*2-25 and event.x <= data.width//6*2+25 
    and event.y<=data.height//16*11+10 and event.y >= data.height//16*11-10):
        data.stage +=1
        data.conference = 'Major'
    if (event.x >= data.width//6*4-40 and event.x <= data.width//6*4+40 
    and event.y<=data.height//16*11+10 and event.y >= data.height//16*11-10):
        data.stage +=1
        data.conference = 'Non-Major'
            

    