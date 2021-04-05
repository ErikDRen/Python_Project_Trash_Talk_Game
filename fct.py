from random import shuffle

# Will give the selecter character to the player
def giveChar(stre):

    selectedChar = ''

    if stre == '1':
        selectedChar += 'Corentin'
    elif stre == '2':
        selectedChar += 'Juliette'
    elif stre == '3':
        selectedChar += 'Jean'
    elif stre == '4':
        selectedChar += 'Aurélie'
    elif stre == '5':
        selectedChar += 'Francis'

    return selectedChar

# Will give characters' informations


def giveCharInfo(stre):

    informations = ''

    if stre[1] == '1':
        informations += 'Corentin wins more points using words of subjectab'
    elif stre[1] == '2':
        informations += 'Juliette wins more points using words of vertab'
    elif stre[1] == '3':
        informations += 'Jean wins more points using words of complementab'
    elif stre[1] == '4':
        informations += 'Aurélie wins more points using words of endtab'
    elif stre[1] == '5':
        informations += 'Francis wins more points using words of linktab'

    return informations

# FULL RECURSIVITE
# Will do the difference if player want info of character


def infoChoose(stre):

    selected = ''

    if len(stre) == 2:
        selected += giveCharInfo(stre)
        getChar = str(input())

    if len(stre) == 1:
        selected += giveChar(stre)

    return selected

# error if the player do not enter a valid command choosing character


def errChar(getChar):
    if len(getChar) == 1:
        while getChar != '1' and getChar != '2' and getChar != '3' and getChar != '4' and getChar != '5':
            print('Error: You have to choose a right number')
            getChar = str(input())
    elif len(getChar) == 2:
# error if player do not enter a "?" for informations
        while getChar[0] != '?':
            print('Error: Missing "?"')
            getChar = str(input())
# error if player enter a "?" but NAN
    if getChar[0] == '?':
        next
        if getChar[1] != '1' and getChar[1] != '2' and getChar[1] != '3' and getChar[1] != '4' and getChar[1] != '5':
            print('Error: You have to choose a right number')
            getChar = str(input())
# if player enter len > 2
    elif len(getChar) > 2:
        while len(getChar) <= 2:
            print('Error: not understandable')
            getChar = str(input())
    return getChar


def mixTab(mainTab):
    shuffle(mainTab)
    return mainTab
# L = ['a','b','c','d','e','f']
# print(L)
# shuffle(L)
# print(L)

# create a sentence for  P1
def sentencePOne(mainTab, wordPOne):
    chooseOne == input()
    for i in range(0, len(mainTab), 1)
       if (mainTab[i] == chooseOne):
            wordPOne.append(mainTab[i])
        else:
            print('out of range, choose another number pls')
            chooseOne = int(input())
    return wordPOne


def sentencePTwo(mainTab, wordPTwo):
    chooseOne = int(input())
    for i in range(0, len(mainTab), 1)
       if (mainTab[i] == chooseOne):
            wordPTwo.append(mainTab[i])
        else:
            print('out of range, choose another number pls')
            chooseOne = int(input())
    return wordPTwo
