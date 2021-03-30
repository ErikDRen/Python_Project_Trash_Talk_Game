from player import player
from fct import *

#Player1 will enter his username 
print('Player 1, Choose your username : ')
username1 = str(input())

#Player1 will choose a character
print('\n' +
    username1 + 
    ' choose your character : 1.Corentin 2.Juliette 3.Jean 4.Aurélie 5.Francis \nnote: Type the number of the player. For informations about the character type "?(number)"'
)
getChar = str(input())

#Will give the selected character to the player
p1 = player(username1, giveChar(getChar))           

print('Player2, Choose your username : ')
username2 = str(input())
p2 = player(username2)
print(p1.name + ' VS ' + p2.name + ' FIGHT !')

Turnp1 = 'Player 1, your turn.'
Turnp2 = 'Player 2, your turn.'
# 1. choose subject
# 2. Choose verb
# 3. Choose situation
# 4. Choose end

