"""
Created on 1/15/2020
@author: Jake Seawell (seawellj)

"""

# Test Utility file for dominion

import Dominion
import random
from collections import defaultdict

#function to initialize game setup
#this function runs all the functions below
def InitializeGame(player_names, num, playerNum):

	# Get # of curse and victory card
	nV, nC = GetNumCurseVictory(player_names, playerNum)

	# initialize boxes
	box = GetBoxes(nV, num)

	supply_order = GetSupplyOrder()

	# initialize supply
	supply = GetSupply(nC, nV, box, player_names)

	# initialize the trash
	trash = []

	players = GetPlayers(player_names)
	return supply_order, supply, players



# INITIALIZATION FUNCTIONS:

def GetNumCurseVictory(player_names, playerNum):
	#number of curses and victory cards
	#replace playerNum with 2
	if len(player_names)>playerNum:
		nV=12
	else:
		nV=8
	nC = -10 + 10 * len(player_names)
	return nV, nC

def GetBoxes(nV, num):
	#Define box
	box = {}
	box["Woodcutter"]=[Dominion.Woodcutter()]*num
	box["Smithy"]=[Dominion.Smithy()]*num
	box["Laboratory"]=[Dominion.Laboratory()]*num
	box["Village"]=[Dominion.Village()]*num
	box["Festival"]=[Dominion.Festival()]*num
	box["Market"]=[Dominion.Market()]*num
	box["Chancellor"]=[Dominion.Chancellor()]*num
	box["Workshop"]=[Dominion.Workshop()]*num
	box["Moneylender"]=[Dominion.Moneylender()]*num
	box["Chapel"]=[Dominion.Chapel()]*num
	box["Cellar"]=[Dominion.Cellar()]*num
	box["Remodel"]=[Dominion.Remodel()]*num
	box["Adventurer"]=[Dominion.Adventurer()]*num
	box["Feast"]=[Dominion.Feast()]*num
	box["Mine"]=[Dominion.Mine()]*num
	box["Library"]=[Dominion.Library()]*num
	box["Gardens"]=[Dominion.Gardens()]*nV
	box["Moat"]=[Dominion.Moat()]*num
	box["Council Room"]=[Dominion.Council_Room()]*num
	box["Witch"]=[Dominion.Witch()]*num
	box["Bureaucrat"]=[Dominion.Bureaucrat()]*num
	box["Militia"]=[Dominion.Militia()]*num
	box["Spy"]=[Dominion.Spy()]*num
	box["Thief"]=[Dominion.Thief()]*num
	box["Throne Room"]=[Dominion.Throne_Room()]*num
	return box

def GetSupplyOrder():
	supply_order = {0: ['Curse', 'Copper'], 2: ['Estate', 'Cellar', 'Chapel', 'Moat'],
					3: ['Silver', 'Chancellor', 'Village', 'Woodcutter', 'Workshop'],
					4: ['Gardens', 'Bureaucrat', 'Feast', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief',
						'Throne Room'],
					5: ['Duchy', 'Market', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Mine', 'Witch'],
					6: ['Gold', 'Adventurer'], 8: ['Province']}
	return supply_order

def GetSupply(nC, nV, box, player_names):

	#Pick 10 cards from box to be in the supply.
	boxlist = [k for k in box]
	random.shuffle(boxlist)
	random10 = boxlist[:10]
	supply = defaultdict(list,[(k,box[k]) for k in random10])


	#The supply always has these cards
	supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
	supply["Silver"]=[Dominion.Silver()]*40
	supply["Gold"]=[Dominion.Gold()]*30
	supply["Estate"]=[Dominion.Estate()]*nV
	supply["Duchy"]=[Dominion.Duchy()]*nV
	supply["Province"]=[Dominion.Province()]*nV
	supply["Curse"]=[Dominion.Curse()]*nC
	return supply

def GetPlayers(player_names):
    #Costruct the Player objects
    players = []
    for name in player_names:
        if name[0]=="*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0]=="^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))
    return players
