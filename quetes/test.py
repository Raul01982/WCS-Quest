
from random import *

playerList = [
    {
        'id': 1,
        'name': "Lebron James",
        'position': -1,
    },
    {
        'id': 2,
        'name': "Stephen Curry",
        'position': -1,
    },
    {
        'id': 3,
        'name': "Kevin Durant",
        'position': -1,
    },
    {
        'id': 4,
        'name': "Kawhi Leonard",
        'position': -1,
    },
    {
        'id': 5,
        'name': "James Harden",
        'position': -1,
    },
]


def selectNbDices():
    nbDices = int(input('Choisissez le nombre de dés à lancer:'))

    if nbDices > 5:
        print('Le nombre de dés ne peut pas être supérieur à 5.')
        return selectNbDices()

    return nbDices

def rollDices(n):

    listDices = []

    for loop in range(n):
        dice = randrange(1,7)
        listDices.append(dice)

    return listDices


def orderPlayer():
        playerListOrdered = sorted(playerList,
                            key=lambda player:player['position'])
        return playerListOrdered




nbr_player = len(playerList)

list_dice = []

for index in range(nbr_player):
    jet = rollDices(1)
    list_dice.append({'id':playerList[index]['id'], 'jet': jet})


orderedList = sorted(list_dice, key=lambda d: d['jet'])[::-1]

longueur = len(orderedList)

for index in range(longueur):

    for player in playerList:
        if orderedList[index]['id'] == player['id']:
            player['position'] = index

orderPlayer()