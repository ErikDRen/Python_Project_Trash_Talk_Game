#Will give the selecter character to the player
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
        selectedChar +='Francis'

    return selectedChar  

#Will give characters' informations
def giveCharInfo(stre):

    informations = ''

    if stre == '1':
        informations += 'Corentin wins more points using words of subjectab'
    elif stre == '2':
        informations += 'Juliette wins more points using words of vertab'
    elif stre == '3':
        informations += 'Jean wins more points using words of complementab'
    elif stre == '4':
        informations  += 'Aurélie wins more points using words of endtab'       
    elif stre == '5':
        informations += 'Francis wins more points using words of linktab'         

    return informations    


#Will do the difference if player want info of character
#J'arrive pas a append putain
def detect(stre):

    selected = ''

    if len(stre) == 1:
        selected += giveChar(stre)
    elif len(stre) == 1:
        for i in stre:
            if i[0] == '?':
               selected += giveCharInfo(i[1])
    return selected