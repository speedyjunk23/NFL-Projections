##########################
#112 Term Project Webscrapping & Dict Set Up
##########################

import bs4

import requests

import string

import DictCombine

from bs4 import BeautifulSoup

NCAA = {'QB':[],'RB':[],'WR':[],'TE':[],'DL':[],'LB':[],'DB':[]}
NFL = NFL_Z = {'QB': [{'Roy Zimmerman': (0.42532005689900426, 0.6285714285714286, 84)}, {'Scott Zolak': (0.5, 1.1428571428571428, 55)}, {'Jim Zorn': (0.5300095268339156, 0.7872340425531915, 140)}], 'RB': [{'Amos Zereoue': (6.583333333333333, 3.864376130198915, 0.0)}], 'WR': [], 'TE': [{'Joe Zelenka': (0, 0, 0.0)}], 'DL': [{'Peppi Zellner': (1.202247191011236, 0.10112359550561797, 0.011235955056179775)}, {'Jeff Zgonina': (1.4018264840182648, 0.1187214611872146, 0.0136986301369863)}, {'Jack Zilly': (0, 0, 0)}, {'John Zook': (0, 0, 0)}, {'Chris Zorich': (3.380952380952381, 0.19047619047619047, 0.047619047619047616)}], 'LB': [{'Steve Zabel': (0, 0, 0)}, {'John Zamberlin': (0, 0.01282051282051282, 0)}, {'Carl Zander': (0, 0.07547169811320754, 0)}, {'Roger Zatkoff ': (0, 0, 0)}, {'Frank Zombo': (1.2380952380952381, 0.11428571428571428, 0.047619047619047616)}], 'DB': [{'Tom Zbikowski': (1.09375, 0.046875, 0.0)}, {'Bob Zeman': (0, 0.2073170731707317, 0)}, {'Mike Zordich': (3.1783783783783783, 0.10810810810810811, 0.032432432432432434)}]}
#####
#Shared Helper
#####
def numbers(linkSoup, positionText, GPNums):
    data = str(linkSoup.find_all('tfoot'))
    #try and except needed because website codes 0 as none 
    #which gives none type error
    if positionText == 'QB':
        try:
            Att = linkSoup.find_all('td', {'data-stat':'pass_att'})
            AttNums = []
            for i in Att:
                for j in i:
                    if isinstance(j, str):
                        AttNums.append(int(j))
                    else:
                        for k in j:
                            AttNums.append(int(k))
        except: AttNums = [0]
        try:
            Cmp = linkSoup.find_all('td', {'data-stat':'pass_cmp'})
            CmpNums = []
            for i in Cmp:
                for j in i:
                    if isinstance(j, str):
                        CmpNums.append(int(j))
                    else:
                        for k in j:
                            CmpNums.append(int(k))
        except: CmpNums = [0]
        try:
            TD = linkSoup.find_all('td', {'data-stat':'pass_td'})
            TDNums = []
            for i in TD:
                for j in i:
                    if isinstance(j, str):
                        TDNums.append(int(j))
                    else:
                        for k in j:
                            TDNums.append(int(k))
        except: TDNums = [0]
        try:
            INT = linkSoup.find_all('td', {'data-stat':'pass_int'})
            INTNums = []
            for i in INT:
                for j in i:
                    if isinstance(j, str):
                        INTNums.append(int(j))
                    else:
                        for k in j:
                            INTNums.append(int(k))
        except: 
            INTNums = [0]
        try: statOne = max(CmpNums)/max(AttNums)
        except: statOne = 0
        try: statTwo = max(TDNums)/max(INTNums)
        except: statTwo = 0
        statThree = max(GPNums)
        return (statOne, statTwo, statThree)
    elif positionText == 'RB':
        try:
            Car = linkSoup.find_all('td', {'data-stat':'rush_att'})
            CarNums = []
            for i in Car:
                for j in i:
                    if isinstance(j, str):
                        CarNums.append(int(j))
                    else:
                        for k in j:
                            CarNums.append(int(k))
        except: CarNums = [0]
        try: statOne = max(CarNums)/max(GPNums)
        except: statOne = 0
        try: 
            Yds = linkSoup.find_all('td', {'data-stat':'rush_yds'})
            YdsNums = []
            for i in Yds:
                for j in i:
                    if isinstance(j, str):
                        YdsNums.append(int(j))
                    else:
                        for k in j:
                            YdsNums.append(int(k))
        except: YdsNums = [0]
        try: statTwo = max(YdsNums)/max(CarNums)
        except: statTwo = 0
        try:
            TD = linkSoup.find('td', {'data-stat':'rush_td'})
            TDNums = []
            for i in TD:
                for j in i:
                    if isinstance(j, str):
                        TDNums.append(int(j))
                    else:
                        for k in j:
                            TDNums.append(int(k))
        except: TDNums = [0]
        try: statThree = max(TDNums)/max(GPNums)
        except: statThree = 0
        return (statOne, statTwo, statThree)
    elif positionText == 'WR' or positionText == 'TE':
        try:
            Rec = linkSoup.find_all('td', {'data-stat':'rec'})
            RecNums = []
            for i in Rec:
                for j in i:
                    if isinstance(j, str):
                        RecNums.append(int(j))
                    else:
                        for k in j:
                            RecNums.append(int(k))
        except: RecNums = [0]
        try: statOne = max(RecNums)/max(GPNums)
        except: statOne = 0
        Yds = linkSoup.find_all('td', {'data-stat':'rec_yds'})
        YdsNums = []
        try:
            for i in Yds:
                for j in i:
                    if isinstance(j, str):
                        YdsNums.append(int(j))
                    else:
                        for k in j:
                            YdsNums.append(int(k))
        except: YdsNums = [0]
        try: statTwo = max(YdsNums)/max(RecNums)
        except: statTwo = 0
        try:
            TD = linkSoup.find('td', {'data-stat':'rec_td'})
            TDNums = []
            for i in TD:
                for j in i:
                    if isinstance(j, str):
                        TDNums.append(int(j))
                    else:
                        for k in j:
                            TDNums.append(int(k))
        except: TDNums = [0]
        try: statThree = max(TDNums)/max(GPNums)
        except: statThree = 0
        return (statOne, statTwo, statThree)
    elif positionText == 'DL' or positionText == 'LB':
        try:
            Tkl = linkSoup.find_all('td', {'data-stat':'tackles_solo'})
            TklNums = []
            for i in Tkl:
                for j in i:
                    if isinstance(j, str):
                        TklNums.append(int(j))
                    else:
                        for k in j:
                            TklNums.append(int(k))
        except: TklNums=[0]
        try:
            Sacks = linkSoup.find_all('td', {'data-stat':'sacks'})
            SacksNums = []
            for i in Sacks:
                for j in i:
                    if isinstance(j, str):
                        SacksNums.append(int(float(j)))
                    else:
                        for k in j:
                            SacksNums.append(int(float(k)))
        except: SacksNums = [0]
        try:
            FF = linkSoup.find_all('td', {'data-stat':'fumbles_forced'})
            FFNums = []
            for i in FF:
                for j in i:
                    if isinstance(j, str):
                        FFNums.append(int(j))
                    else:
                        for k in j:
                            FFNums.append(int(k))
        except: FFNums = [0]
        try: statOne = max(TklNums)/max(GPNums)
        except: statOne = 0
        try: statTwo = max(SacksNums)/max(GPNums)
        except: statTwo = 0
        try: statThree = max(FFNums)/max(GPNums)
        except: statThree = 0
        return (statOne, statTwo, statThree)
    elif positionText == 'DB':
        try:
            Tkl = linkSoup.find_all('td', {'data-stat':'tackles_solo'})
            TklNums = []
            for i in Tkl:
                for j in i:
                    if isinstance(j, str):
                        TklNums.append(int(j))
                    else:
                        for k in j:
                            TklNums.append(int(k))
        except: TklNums = [0]
        try:
            INT = linkSoup.find_all('td', {'data-stat':'def_int'})
            INTNums = []
            for i in INT:
                for j in i:
                    if isinstance(j, str):
                        INTNums.append(int(j))
                    else:
                        for k in j:
                            INTNums.append(int(k))
        except: INTNums = [0]
        try:
            FF = linkSoup.find_all('td', {'data-stat':'fumbles_forced'})
            FFNums = []
            for i in FF:
                for j in i:
                    if isinstance(j, str):
                        FFNums.append(int(j))
                    else:
                        for k in j:
                            FFNums.append(int(k))
        except: FFNums = [0]
        try: statOne = max(TklNums)/max(GPNums)
        except: statOne = 0
        try: statTwo = max(INTNums)/max(GPNums)
        except: statTwo = 0
        try: statThree = max(FFNums)/max(GPNums)
        except: statThree = 0
        return (statOne, statTwo, statThree)

#####
#NFL Scrap
#####

def getNFL():
    NFL_URL = 'https://www.pro-football-reference.com/players/'
    NFL_r = requests.get(NFL_URL)
    NFL_soup = BeautifulSoup(NFL_r.content, "html.parser")
    NFL_names = NFL_soup.find_all('a')
    for letter in NFL_names:
        if (letter.get('href').find('players') != -1 
        and len(letter.get('href')) == 11):
            letterURL = ('https://www.pro-football-reference.com'+
                                            str(letter.get('href')))
            letterR = requests.get(letterURL)
            letterSoup = BeautifulSoup(letterR.content, 'html.parser')
            statNFL(letterSoup)
    print(NFL)
    return NFL
        
def statNFL(letterSoup):
    checked = set()
    letterPlayers = letterSoup.find_all('a')
    for link in letterPlayers:
        if (link.get('href').find('players/Z') != -1 
            and len(link.get('href')) >= 21):
            if link.get('href') not in checked:
                checked.add(link.get('href'))
                dictionaryNFL(link)

def dictionaryNFL(link):
    link = ('https://www.pro-football-reference.com'+ str(link.get('href')))
    Positions = ['QB', 'RB', 'FB', 'WR', 'TE', 'DE', 'DT', 'DL', 'LB', 
                     'CB', 'S ', 'FS', 'SS', 'DB']
    QB = ['QB']
    RB = ['RB', 'FB']
    WR = ['WR']
    TE = ['TE']
    DL = ['DE', 'DT', 'DL']
    LB = ['LB']
    DB = ['S ', 'FS', 'SS', 'DB', 'CB']
    linkR = requests.get(link)
    linkSoup = BeautifulSoup(linkR.content, 'html.parser')
    positionText = linkSoup.find_all('p')[1].text
    positionText+=(' ')
    positionText = positionText[11:13]
    GP = linkSoup.find_all('td', {'data-stat':'g'})
    GPNums = []
    for i in GP:
        for j in i:
            GPNums.append(int(j))
    if GPNums != [] and max(GPNums) >= 50 and positionText in Positions:
        if positionText in QB: positionGroup = 'QB'
        if positionText in RB: positionGroup = 'RB'
        if positionText in WR: positionGroup = 'WR'
        if positionText in TE: positionGroup = 'TE'
        if positionText in DL: positionGroup = 'DL'
        if positionText in LB: positionGroup = 'LB'
        if positionText in DB: positionGroup = 'DB'
        name = linkSoup.find('h1').text
        print(name)
        statOne, statTwo, statThree=numbers(linkSoup, positionGroup, GPNums) 
        tmpDict = dict({name:(statOne, statTwo, statThree)})
        NFL[positionGroup].append(tmpDict)

#####
#NCAA Scrap
#####

def getNCAA():
    players = []
    subject = []
    for position in NFL:
        for name in NFL[position]:
            name = str(name).split(' ')
            players.append(name)
    for i in players:
        for j in i:
            for k in j:
                if not k.isalpha():
                    j=j.replace(k,'')
            subject.append(j)
        while '' in subject:
            subject.pop(subject.index(''))
        statNCAA(subject)
    print(NCAA)
    return NCAA

def statNCAA(player):
    iteration = 0
    count = 1
    for i in player:
        player [iteration] = i.lower()
        iteration +=1
    URL = ('https://www.sports-reference.com/cfb/players/' + player [0] +
                        '-' + player[1] + '-' + str(count) + '.html')
    while len(player) >= 1: 
        player.pop(0)
    dictionaryNCAA(URL)
    
def dictionaryNCAA(link):
    Positions = ['QB', 'RB', 'FB', 'WR', 'TE', 'DE', 'DT', 'DL', 'LB', 
                     'CB', 'S ', 'FS', 'SS', 'DB']
    QB = ['QB']
    RB = ['RB', 'FB']
    WR = ['WR']
    TE = ['TE']
    DL = ['DE', 'DT', 'DL']
    LB = ['LB']
    DB = ['S ', 'FS', 'SS', 'DB', 'CB']
    linkR = requests.get(link)
    linkSoup = BeautifulSoup(linkR.content, 'html.parser')
    try:
        positionText = linkSoup.find_all('p')[1].text
        positionText+=(' ')
        positionText = positionText[11:13]
        name = linkSoup.find('h1').text
        if name[name.index(' ')+1:name.index(' ')+2] == 'Z':
            print(name)
            GP = linkSoup.find_all('td', {'data-stat':'g'})
            GPNums = []
            for i in GP:
                for j in i:
                    GPNums.append(int(j))
            GPNums = [sum(GPNums)]
            if GPNums != [] and GPNums[0] >= 15 and positionText in Positions:
                for i in NFL:
                    for j in NFL[i]:
                        if name in j or (name+' ') in j:
                            if positionText in QB: positionGroup = 'QB'
                            if positionText in RB: positionGroup = 'RB'
                            if positionText in WR: positionGroup = 'WR'
                            if positionText in TE: positionGroup = 'TE'
                            if positionText in DL: positionGroup = 'DL'
                            if positionText in LB: positionGroup = 'LB'
                            if positionText in DB: positionGroup = 'DB'
                            if not name in NCAA[positionGroup]:
                                statOne, statTwo, statThree = numbers(linkSoup, positionGroup, GPNums)
                                try:
                                    phyInfo = []
                                    H_W = linkSoup.find_all('p')
                                    for i in H_W[2]:
                                        phyInfo.append(i)
                                    phyInfo = phyInfo[-1].split(',')
                                    count = 0
                                    for i in phyInfo:
                                        for j in i:
                                            if not j.isdigit():
                                                i = i.replace(j, '')
                                                phyInfo[count] = i
                                        count+=1
                                    height, weight = phyInfo[0], phyInfo[1]
                                except:
                                    #if there's no h/w given average for 
                                    #current D1 by position are used
                                    if positionGroup == 'QB':
                                        height, weight = 188, 94
                                    if positionGroup == 'RB':
                                        height, weight = 178, 92
                                    if positionGroup == 'WR':
                                        height, weight = 183, 86
                                    if positionGroup == 'TE':
                                        height, weight = 193, 109
                                    if positionGroup == 'DL':
                                        height, weight = 191, 122
                                    if positionGroup == 'LB':
                                        height, weight = 185, 101
                                    if positionGroup == 'DB':
                                        height, weight = 180, 86
                                conferenceData = linkSoup.find_all('a')
                                conference = (str(conferenceData)
                                    [str(conferenceData).find('conferences'):
                                    str(conferenceData).find('conferences')+20])
                                conference = conference.split('/')
                                conference = conference[1]
                                roundData = linkSoup.find_all('p')
                                round = (str(roundData)
                                        [str(roundData).find('round')-4:
                                        str(roundData).find('round')])
                                round = round[0:1]
                                tmpDict = dict({name:[round, height, weight, conference, 
                                                    statOne, statTwo, statThree]})
                                NCAA[positionGroup].append(tmpDict)
                                #print(NCAA)
        else:
            pass
    except: 
    #some of the older players that they have NFL data for don't have 
    #recorded college stats so this takes care of that
        pass
####
#Run Calls
####
#getNFL()
NCAA = getNCAA()