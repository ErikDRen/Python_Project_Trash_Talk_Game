from random import randint
from random import shuffle


def addSubject():
    selected = randint(0, len(subjecTab))
    while (len(mainTab) > 4):
        for i in range(0, len(subjecTab), 1):
            if (selected == i):
                mainTab.append(subjecTab[i])
    return mainTab


def addVerb():
    selected = randint(0, len(verbTab))
    while (len(mainTab) > 8):
        for i in range(0, len(verbTab)):
            if (selected == i):
                mainTab.append(verbTab[i])
    return mainTab


def addComplement():
    selected = randint(0, len(complementab))
    while (len(mainTab) > 12):
        for i in range(0, len(complementab)):
            if (selected == i):
                mainTab.append(complementab[i])
    return mainTab


def addEnd():
    selected = randint(0, len(endTab))
    while (len(mainTab) > 16):
        for i in range(0, len(endTab)):
            if (selected == i):
                mainTab.append(endTab[i])
    return mainTab


def addLink():
    selected = randint(0, len(linkTab))
    while (len(mainTab) > 20):
        for i in range(0, len(linkTab)):
            if (selected == i):
                mainTab.append(linkTab[i])
    return mainTab


# L = ['a','b','c','d','e','f']
# print(L)
# shuffle(L)
# print(L)
