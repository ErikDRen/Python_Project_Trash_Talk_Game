from random import randint
from wordList import *


def addSubject(subjecTab, mainTab):
    while (len(mainTab) < 4):
        for i in range(0, len(subjecTab), 1):
            selected = randint(0, len(subjecTab))
            if (selected == i):
                mainTab.append(subjecTab[i])
    return mainTab


def addVerb(verbTab, mainTab):
    while (len(mainTab) < 8):
        for i in range(0, len(verbTab),1):
            selected = randint(0, len(verbTab))
            if (selected == i):
                mainTab.append(verbTab[i])
    return mainTab


def addComplement(complementab, mainTab):
    while (len(mainTab) < 12):
        for i in range(0, len(complementab),1):
            selected = randint(0, len(complementab))
            if (selected == i):
                mainTab.append(complementab[i])
    return mainTab


def addEnd(endTab, mainTab):
    while (len(mainTab) < 16):
        for i in range(0, len(endTab),1):
            selected = randint(0, len(endTab))
            if (selected == i):
                mainTab.append(endTab[i])
    return mainTab


def addLink(linkTab, mainTab):
    while (len(mainTab) < 20):
        for i in range(0, len(linkTab),1):
            selected = randint(0, len(linkTab))
            if (selected == i):
                mainTab.append(linkTab[i])
    return mainTab
