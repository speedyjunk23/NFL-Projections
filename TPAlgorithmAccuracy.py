import NCAADictCombine
import DictCombine
import TPAlgorithms

NCAA = NCAADictCombine.dictCombine()
NFL, NCAA = DictCombine.dictCombine(NCAA)

def findAccuracy(NFL, NCAA):
    count = 0
    stat1m, stat2m, stat3m = 0,0,0
    position = 'DB'
    for i in range(1,50):
        print(i)
        for j in range (1,50):
            for k in range (1,50):
                tmpCount = 0
                if i+j+k == 100:
                    s1m, s2m, s3m = i/100, j/100, k/100
                    for playerlist in NCAA[position]:
                        try:
                            simPlayer = check(playerlist, position, s1m, s2m, s3m)
                            realStats = grabNFL(playerlist[0])
                            cellingStats = grabNFL(findCelling(simPlayer, position, s1m, s2m, s3m))
                            floorStats = grabNFL(findFloor(simPlayer, position, s1m, s2m, s3m))
                            try:
                                if cellingStats[0]>realStats[0]>floorStats[0]:
                                    tmpCount+=1
                                if cellingStats[1]>realStats[1]>floorStats[1]:
                                    tmpCount+=1
                                if cellingStats[2]>realStats[2]>floorStats[2]:
                                    tmpCount+=1
                            except:
                                pass
                        except:
                            pass
                        if tmpCount>count:
                            count = tmpCount
                            stat1m, stat2m, stat3m = s1m, s2m, s3m
    print(stat1m, stat2m, stat3m)
    return (stat1m, stat2m, stat3m)



def check(playerlist, position, s1m, s2m, s3m):
    simScore = None
    simPlayer = ''
    for player in range(len(NCAA[position])):
        if NCAA[position][player][0] != playerlist[0]:
            if (playerlist[1][0] == NCAA[position][player][1][0] or 
            int(playerlist[1][0]) == int(NCAA[position][player][1][0])+1 or 
            int(playerlist[1][0]) == int(NCAA[position][player][1][0])-1):
                if int(playerlist[1][1]) <= int(NCAA[position][player][1][1])+10:
                    if int(playerlist[1][1]) >= int(NCAA[position][player][1][1])-10:
                        if int(playerlist[1][2]) <= int(NCAA[position][player][1][2])+10:
                            if int(playerlist[1][2]) >= int(NCAA[position][player][1][2])-10:
                                if (float(NCAA[position][player][1][-3])) == 0:
                                    score1 = 1*s1m
                                else:   
                                    score1 = (abs(1-(float(playerlist[1][4]))/
                                            (float(NCAA[position][player][1][-3])))
                                            *s1m)
                                if (int(float(NCAA[position][player][1][-2]))) == 0:
                                    score2 = 1*s2m
                                else:
                                    score2 = (abs(1-(float(playerlist[1][5]))/
                                            (float(NCAA[position][player][1][-2])))
                                            *s2m)
                                if (int(float(NCAA[position][player][1][-1]))) == 0:
                                    score3 = 1*s3m
                                else:
                                    score3 = (abs(1-(float(playerlist[1][6]))/
                                                (float(NCAA[position][player][1][-1])))
                                                *s3m)
                                testScore = score1 + score2 + score3
                                if simScore == None:
                                    simScore = testScore
                                    simPlayer = NCAA[position][player][0]
                                elif testScore < simScore:
                                    simScore = testScore
                                    simPlayer = NCAA[position][player][0]
    return simPlayer
    
def findCelling(simPlayer, position, s1m, s2m, s3m):
    expectedStats = grabNFL(simPlayer)
    cellingScore = None
    cellingPlayer = ''
    for player in range(len(NFL[position])):
        if (float(NFL[position][player][1][-3])) == 0:
            score1 = 1*s1m
        else:   
            score1 = (abs(1-((float(expectedStats[0]))*1.1)/
            (float(NFL[position][player][1][-3])))*s1m)
        if (float(NFL[position][player][1][-2])) == 0:
            score2 = 1*s2m
        else:
            score2 = (abs(1-((float(expectedStats[1]))*1.1)/
            (float(NFL[position][player][1][-2])))*s2m)
        if (float(NFL[position][player][1][-1])) == 0:
            score3 = 1*s3m
        else:
            score3 = (abs(1-((float(expectedStats[2]))*1.1)/
            (float(NFL[position][player][1][-1])))*s3m)
        testScore = score1 + score2 + score3
        if cellingScore == None:
            cellingScore = testScore
            cellingPlayer = NFL[position][player][0]
        elif testScore < cellingScore:
            cellingScore = testScore
            cellingPlayer = NFL[position][player][0]
    return cellingPlayer
    
def findFloor(simPlayer, position, s1m, s2m, s3m):
    expectedStats = grabNFL(simPlayer)
    floorScore = None
    floorPlayer = ''
    for player in range(len(NFL[position])):
        if (float(NFL[position][player][1][-3])) == 0:
            score1 = 1*s1m
        else:   
            score1 = (abs(1-((float(expectedStats[0]))*.9)/
            (float(NFL[position][player][1][-3])))*s1m)
        if (float(NFL[position][player][1][-2])) == 0:
            score2 = 1*s2m
        else:
            score2 = (abs(1-((float(expectedStats[1]))*.9)/
            (float(NFL[position][player][1][-2])))*s2m)
        if (float(NFL[position][player][1][-1])) == 0:
            score3 = 1*s3m
        else:
            score3 = (abs(1-((float(expectedStats[2]))*.9)/
            (float(NFL[position][player][1][-1])))*s3m)
        testScore = score1 + score2 + score3
        if floorScore == None:
            floorScore = testScore
            floorPlayer = NFL[position][player][0]
        elif testScore < floorScore:
            floorScore = testScore
            floorPlayer = NFL[position][player][0]
    return floorPlayer
    
def grabNFL(comp):
    comp2 = comp + ' '
    for key in NFL:
        for player in NFL[key]:
            if comp in player or comp2 in player:
                return([player[1][0], player[1][1], player[1][2]])
    
#findAccuracy(NFL, NCAA)

#QB - .46, .05, .49
#RB - .46, .26, .28
#WR - .23, .47, .3
#TE - .47, .07, .46
#DL - .38, .39, .23
#LB - .45, .06, .49
#DB - .41, .10, .49