import random as rand

availableSpaces = []

def pickSpace001(list):
    if spaceTL in list:
        availableSpaces.append(spaceTL)
    if spaceTR in list:
        availableSpaces.append(spaceTR)
    if spaceBL in list:
        availableSpaces.append(spaceBL)
    if spaceBR in list:
        availableSpaces.append(spaceBR)
    currChoice = rand.choice(availableSpaces)
    availableSpaces.clear()
    