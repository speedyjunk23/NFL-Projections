##########################
#112 Term Project Algorithms 
##########################

import DictCombine
import NCAADictCombine

NCAA = NCAADictCombine.dictCombine()

NFL, NCAA = DictCombine.dictCombine(NCAA)

def findSimilarPlayer(data):
    simScore = None
    simPlayer = ''
    conference = 'Non-Major'
    major = ['sec', 'acc', 'pac-10', 'big-ten', 'big-12']
    for player in range(len(NCAA[data.position])):
        if NCAA[data.position][player][1][3] in major:
            conference = 'Major'
        if NCAA[data.position][player][1][0].isdigit():
            if (data.round == NCAA[data.position][player][1][0] or 
            int(data.round) == int(NCAA[data.position][player][1][0])+1 or 
            int(data.round) == int(NCAA[data.position][player][1][0])-1):
                if int(data.prospectHeight) <= int(NCAA[data.position][player][1][1])+10:
                    if int(data.prospectHeight) >= int(NCAA[data.position][player][1][1])-10:
                        if int(data.prospectWeight) <= int(NCAA[data.position][player][1][2])+10:
                            if int(data.prospectWeight) >= int(NCAA[data.position][player][1][2])-10:
                                if (float(NCAA[data.position][player][1][-3])) == 0:
                                    score1 = 1*data.stat1Multiplier
                                else: 
                                    if data.position == 'QB':
                                        data.stat1 = float(data.stat1)/100
                                    score1 = (abs(1-(float(data.stat1))/
                                            (float(NCAA[data.position][player][1][-3])))
                                            *data.stat1Multiplier)
                                if (int(float(NCAA[data.position][player][1][-2]))) == 0:
                                    score2 = 1*data.stat2Multiplier
                                else:
                                    score2 = (abs(1-(float(data.stat2))/
                                            (float(NCAA[data.position][player][1][-2])))
                                            *data.stat2Multiplier)
                                if (int(float(NCAA[data.position][player][1][-1]))) == 0:
                                    score3 = 1*data.stat3Multiplier
                                else:
                                    score3 = (abs(1-(float(data.stat3))/
                                                (float(NCAA[data.position][player][1][-1])))
                                                *data.stat3Multiplier)
                                testScore = score1 + score2 + score3
                                if conference != data.conference:
                                    testScore = testScore*.95
                                if simScore == None:
                                    simScore = testScore
                                    simPlayer = NCAA[data.position][player][0]
                                elif testScore < simScore:
                                    simScore = testScore
                                    simPlayer = NCAA[data.position][player][0]
    return simPlayer
    
def findCelling(data):
    cellingScore = None
    cellingPlayer = ''
    for player in range(len(NFL[data.position])):
        if (float(NFL[data.position][player][1][-3])) == 0:
            score1 = 1*data.stat1Multiplier
        else:   
            score1 = (abs(1-((float(data.expectedStats[0]))*1.1)/
            (float(NFL[data.position][player][1][-3])))*data.stat1Multiplier)
        if (float(NFL[data.position][player][1][-2])) == 0:
            score2 = 1*data.stat2Multiplier
        else:
            score2 = (abs(1-((float(data.expectedStats[1]))*1.1)/
            (float(NFL[data.position][player][1][-2])))*data.stat2Multiplier)
        if (float(NFL[data.position][player][1][-1])) == 0:
            score3 = 1*data.stat3Multiplier
        else:
            score3 = (abs(1-((float(data.expectedStats[2]))*1.1)/
            (float(NFL[data.position][player][1][-1])))*data.stat3Multiplier)
        testScore = score1 + score2 + score3
        if cellingScore == None:
            cellingScore = testScore
            cellingPlayer = NFL[data.position][player][0]
        elif testScore < cellingScore:
            cellingScore = testScore
            cellingPlayer = NFL[data.position][player][0]
    return cellingPlayer
    
def findFloor(data):
    floorScore = None
    floorPlayer = ''
    for player in range(len(NFL[data.position])):
        if (float(NFL[data.position][player][1][-3])) == 0:
            score1 = 1*data.stat1Multiplier
        else:   
            score1 = (abs(1-((float(data.expectedStats[0]))*.9)/
            (float(NFL[data.position][player][1][-3])))*data.stat1Multiplier)
        if (float(NFL[data.position][player][1][-2])) == 0:
            score2 = 1*data.stat2Multiplier
        else:
            score2 = (abs(1-((float(data.expectedStats[1]))*.9)/
            (float(NFL[data.position][player][1][-2])))*data.stat2Multiplier)
        if (float(NFL[data.position][player][1][-1])) == 0:
            score3 = 1*data.stat3Multiplier
        else:
            score3 = (abs(1-((float(data.expectedStats[2]))*.9)/
            (float(NFL[data.position][player][1][-1])))*data.stat3Multiplier)
        testScore = score1 + score2 + score3
        if floorScore == None:
            floorScore = testScore
            floorPlayer = NFL[data.position][player][0]
        elif testScore < floorScore:
            floorScore = testScore
            floorPlayer = NFL[data.position][player][0]
    return floorPlayer
    
def grabNFL(comp):
    comp2 = comp + ' '
    for key in NFL:
        for player in NFL[key]:
            if comp in player or comp2 in player:
                return([player[1][0], player[1][1], player[1][2]])
                
def multiplyCheck(data):
    if data.position == 'QB':
        data.stat1Multiplier, data.stat2Multiplier, data.stat3Multiplier = .46,.05,.49
    if data.position == 'RB':
        data.stat1Multiplier, data.stat2Multiplier, data.stat3Multiplier = .46,.26,.28
    if data.position == 'WR':
        data.stat1Multiplier, data.stat2Multiplier, data.stat3Multiplier = .23,.47,.30
    if data.position == 'TE':
        data.stat1Multiplier, data.stat2Multiplier, data.stat3Multiplier = .47,.07,.46
    if data.position == 'DL':
        data.stat1Multiplier, data.stat2Multiplier, data.stat3Multiplier = .38,.39,.23
    if data.position == 'LB':
        data.stat1Multiplier, data.stat2Multiplier, data.stat3Multiplier = .45,.06,.49
    if data.position == 'DB':
        data.stat1Multiplier, data.stat2Multiplier, data.stat3Multiplier = .41,.10,.49
#QB - .46, .05, .49
#RB - .46, .26, .28
#WR - .23, .47, .3
#TE - .47, .07, .46
#DL - .38, .39, .23
#LB - .45, .06, .49
#DB - .41, .10, .49