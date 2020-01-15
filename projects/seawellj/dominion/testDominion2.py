# -*- coding: utf-8 -*-
"""

testDominion2

Created on 1/15/2020

@author: Jake Seawell (seawellj)

"""

import Dominion
import testUtility

#Enter/Edit names of players here
player_names = ["*Jake", "*Kenna", "*Ron", "*Debbie"]

num = 10

"""
This variable, playerNum, represents how many curses and vict cards
are in the deck, depending on how many players there are.

This playerNum gets passed as a parameter to InitializeGame(), which will use
the playerNum for "Curse/Victory" initialization

For the correct game implementation, playerNum = 2, but to introduce a game
bug, I have changed: num = 4
"""

playerNum = 4




#initialize game setup
supply_order, supply, players = testUtility.InitializeGame(player_names, num, playerNum)

#initialize the trash
trash = []

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
