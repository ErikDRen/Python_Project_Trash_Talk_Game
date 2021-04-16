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


# p2 enter his username
print('Player2, Choose your username : ')
username2 = str(input())

# Player1 will choose a character
print('\n' +
      username2 +
      ' choose your character : 1.Corentin 2.Juliette 3.Jean 4.Aurélie 5.Francis \nnote: Type the number of the player. For informations about the character type "?(number)"'
      )
getChar2 = str(input())

char = giveChar(getChar)

# Will fill p1's info
p1 = player(username1, char)

# Will fill p2's info
p2 = player(username2,char)

tab = wordList()
tab.fillMainTab()

print('\n')
print(p1.name + ' VS ' + p2.name + ' FIGHT !')
print('\n')

addSubject(tab.subjecTab,tab.mainTab)
addVerb(tab.verbTab,tab.mainTab)
addComplement(tab.complementab,tab.mainTab)
addEnd(tab.endTab,tab.mainTab)
addLink(tab.linkTab,tab.mainTab)
mixTab(tab.mainTab)
print(tab)
print('\n')



while (len(tab.mainTab) > 10 ) :
 
      choose = sentence(p1.selectedWord,tab.mainTab)
      print('p1 choose : ',p1.selectedWord)
      print('\n')
      print(tab)
      print('\n')

      choose = sentence(p2.selectedWord,tab.mainTab)
      print('p2 choose : ',p2.selectedWord)
      print('\n')
      print(tab)
      print('\n')


scoreP1 = scoreCal(p1.selectedWord)
scoreP2 = scoreCal(p2.selectedWord)

print('p1 : ',p1.selectedWord,'\n','p2 : ',p2.selectedWord)
print('p1 point :',scoreP1, 'and p2 point :',scoreP2)

