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

#Will do the difference if player want info of character
#J'arrive pas a append putain
def infoChar(stre):
    perso1 = 'Corentin gets a bonus'
    sentence = ''
    for i in stre:
        if i == '?':
            continue
            if i == '1':
                sentence += perso1
    return sentence            
                
print(infoChar(getChar))     