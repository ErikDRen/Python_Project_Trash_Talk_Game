from player import player
from fct import *
from wordList import wordList
from Remplir_Tab import *

# --- REGISTER TIME ---

# Player1 will enter his username
print('Player 1, Choose your username : ')
username1 = str(input())

# Player1 will choose a character
print('\n' +
      username1 +
      ' choose your character : 1.Corentin 2.Juliette 3.Jean 4.Aurélie 5.Francis \nnote: Type the number of the player. For informations about the character type "?(number)"'
      )
getChar = str(input())

# error if the player do not enter a valid command
print(errChar(getChar))

# print(detect(getChar))


# Will fill p1's info
p1 = player(username1, giveChar(getChar),[],[])

tab = wordList()
tab.fillMainTab()
# p2 enter his username
print('Player2, Choose your username : ')
username2 = str(input())

# Player1 will choose a character
print('\n' +
      username2 +
      ' choose your character : 1.Corentin 2.Juliette 3.Jean 4.Aurélie 5.Francis \nnote: Type the number of the player. For informations about the character type "?(number)"'
      )
getChar2 = str(input())

# Will fill p2's info
p2 = player(username2, giveChar(getChar2),[],[])


print(p1.name + ' VS ' + p2.name + ' FIGHT !')



addSubject(tab.subjecTab,tab.mainTab)
addVerb(tab.verbTab,tab.mainTab)
addComplement(tab.complementab,tab.mainTab)
addEnd(tab.endTab,tab.mainTab)
addLink(tab.linkTab,tab.mainTab)
mixTab(tab.mainTab)
print(tab)