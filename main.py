# Created by: Joshua Cutting
# Created on: 3/3/2022
# Purpose: To interpret data files created by scoring_engine.py and display them graphically...
#           It's a scoreboard!
# Temporarily only built for two teams competing!!

import os
from graphics import *
#class teamData:
#    teamdata = open("teamdata/routerICMP_output", "r")
#    teamName = ""
#    teamScore = 0
#   teamRouterICMPOn = False
#   team
#   def __init__(self):
def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def main():
    running = True
    print("Loading team data...")
    namedata = open('teamdata/name.data')
    lines = namedata.readlines()

    win = GraphWin("My Window", 1250, 750)
    win.setBackground('black')
    #pt1 = Point("250","250")
    #pt2 = Point("300", "300")
    #rect = Rectangle(pt1, pt2)
    #rect.setFill('blue')
    #ect.draw(win)

    # Title Text Anchor
    TitleAnchor = Point("625", "40")
    text = Text(TitleAnchor, "SUNY POLY HACKATHON")
    text.setSize(36)
    text.setFill('white')
    text.draw(win)
    # end

    # handler init
    itemlist = []
    persistlist = []
    firstPass = True


    while running:

        for i in range(0, len(itemlist)):
            itemlist[i].undraw()
            #itemlist[i].draw(win)

        itemlist.clear()

        for i in range(0, len(lines)):
            filepath = str.strip("teamdata/" + lines[i])
            teamdata = open(filepath, "r")
            teamLines = teamdata.readlines()
            newname = teamLines[0]
            newscore = int(teamLines[1])
            newRouterICMPOn = teamLines[5]
            newsshLoginOn = teamLines[6]
            newwww80On = teamLines[7]
            newwwwContentOn = teamLines[8]
            newdnsFwdOn = teamLines[9]
            newdnsRevOn = teamLines[10]

            anchorPoint = Point("150", "300")

            #controls distance text is away from eachother on x axis
            textXSlide = 330

            blueTeamBarInitAnchor = Point(anchorPoint.x + i*textXSlide + 150, 750)
            blueTeamBarInitAnchor2 = Point(blueTeamBarInitAnchor.x + 50, 750 - newscore)
            rect = Rectangle(blueTeamBarInitAnchor, blueTeamBarInitAnchor2)
            rect.setFill('blue')
            rect.setOutline('blue')
           # temp = Text(Point(anchorPoint.x+(250*(i+1)), anchorPoint.y), newname)
           # temp.setTextColor('white')
            itemlist.append(rect)
            temp = Text(Point(anchorPoint.x + i*textXSlide, anchorPoint.y + 50),newname)
            temp.setTextColor('white')
            itemlist.append(temp)
            temp = Text(Point(anchorPoint.x + i*textXSlide, anchorPoint.y + 100),"Score: "+str(newscore))
            temp.setTextColor('white')
            itemlist.append(temp)
            temp = Text(Point(anchorPoint.x + i*textXSlide, anchorPoint.y + 150),"Router ICMP: "+str(newRouterICMPOn))
            if(newRouterICMPOn == "Up\n"):
                temp.setTextColor('green')
            else:
                temp.setTextColor('red')
            itemlist.append(temp)
            temp = Text(Point(anchorPoint.x + i*textXSlide, anchorPoint.y + 200),"SSH Login: "+str(newsshLoginOn))
            if (newsshLoginOn == "Up\n"):
                temp.setTextColor('green')
            else:
                temp.setTextColor('red')
            itemlist.append(temp)
            temp = Text(Point(anchorPoint.x + i*textXSlide, anchorPoint.y + 250), "www80: " + str(newwww80On))
            if (newwww80On == "Up\n"):
                temp.setTextColor('green')
            else:
                temp.setTextColor('red')
            itemlist.append(temp)
            temp = Text(Point(anchorPoint.x + i*textXSlide, anchorPoint.y + 300),"www Content: "+str(newwwwContentOn))
            if (newwwwContentOn == "Up\n"):
                temp.setTextColor('green')
            else:
                temp.setTextColor('red')
            itemlist.append(temp)
            temp = Text(Point(anchorPoint.x + i*textXSlide, anchorPoint.y + 350),"External DNS Forward: "+str(newdnsFwdOn))
            if (newdnsFwdOn == "Up\n"):
                temp.setTextColor('green')
            else:
                temp.setTextColor('red')
            itemlist.append(temp)
            temp = Text(Point(anchorPoint.x + i*textXSlide, anchorPoint.y + 400), "External DNS Reverse: " + str(newdnsRevOn))
            if (newdnsRevOn == "Up\n"):
                temp.setTextColor('green')
            else:
                temp.setTextColor('red')
            itemlist.append(temp)

        for i in range(0, len(itemlist)):
            itemlist[i].draw(win)

        for i in range(0, len(persistlist)):
            persistlist[i].undraw()

        persistlist.clear()

        for item in itemlist:
            newitem = item.clone()
            persistlist.append(newitem)

        for i in range(0, len(persistlist)):
            persistlist[i].draw(win)


        #itemlist=[]


    win.getMouse()
    win.close()



#    while running:
#        for i in range(0, len(lines)):
#            filepath = str.strip("teamdata/"+lines[i])
#            teamdata = open(filepath, "r")
#            teamLines = teamdata.readlines()
#            newname = teamLines[0]
#            newscore = int(teamLines[1])
#            newRouterICMPOn = teamLines[5]
#            newsshLoginOn = teamLines[6]
#            newwww80On = teamLines[7]
#            newwwwContentOn = teamLines[8]
#            newdnsFwdOn = teamLines[9]
#            newdnsRevOn = teamLines[10]

#            blueTeamBarInitAnchor = Point(250*(i+1), 750)
#            blueTeamBarInitAnchor2 = Point(blueTeamBarInitAnchor.x+50, 750-newscore)
#            rect = Rectangle(blueTeamBarInitAnchor, blueTeamBarInitAnchor2)
#            rect.setFill('blue')
#            rect.draw(win)


   # win.getMouse()
   # win.close()







if __name__ == '__main__':
    main()

