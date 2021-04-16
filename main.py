from player import player
from fct import *
from wordList import wordList
from Remplir_Tab import *


print('\n On la fait a deux...(Ren,Aba: RIP ) \n')
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
playerChar = giveChar(getChar)      

#fill p1 info
p1 = player(username1, playerChar)
print('You choosed ' + p1.perso)

# p2 enter his username
print('Player2, Choose your username : ')
username2 = str(input())

# Player1 will choose a character
print('\n' +
      username2 +
      ' choose your character : 1.Corentin 2.Juliette 3.Jean 4.Aurélie 5.Francis \nnote: Type the number of the player. For informations about the character type "?(number)"'
      )
getChar2 = str(input())

playerChar2 = giveChar(getChar2)

# Will fill p2's info
p2 = player(username2, playerChar2)

print('You choosed ' + p2.perso)

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
print('If your want to choose a word tap : 0 to 19 / If you want to stop you sentence tap : 20')
print('\n')

print(p1,'turn')
while (len(p1.selectedWord) < 10) :
      choose = sentence(p1.selectedWord,tab.mainTab)
      print('\n')
      if (choose == 20):
            break
      else:
            print(tab)
            print(p1, 'choose : ',p1.selectedWord)
            print('\n')


print(p2,'turn')
while (len(p2.selectedWord) < 10) :
      choose = sentence(p2.selectedWord,tab.mainTab)
      print('\n')
      if (choose == 20):
            break
      else:
            print(tab)
            print(p2 ,'choose : ',p2.selectedWord)
            print('\n')


print(tab)
scoreP1 = scoreCal(p1.selectedWord)
scoreP2 = scoreCal(p2.selectedWord)
# scoreFinalP1 = multiplicateur(p1.selectedWord, scoreP1)


print(p1, ': ',p1.selectedWord,'\n',p2, ': ',p2.selectedWord)
print('\n')
print(p1 ,'point :',scoreP1, 'and', p2,'point :',scoreP2)
print('\n')
if (scoreP1 > scoreP2):
      print(p1,'win')
else:
      print(p2,'win')

