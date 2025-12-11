# Map Manager / Navigator - e

import b, d, f

# Traveller, welcome to the old version of how maps are loaded.
# This code is outdated as hell, don't make maps here unless you want to port them later, but even then, the newer code would probably make things easier.

# Additionally, this code wasn't supposed to include colored text, the alpha0.6 version was made completely offline, so this code was released pretty late.
# Of course, if you want to yank this code for use to build maps early, go for it. It barely relies on b.py, d.py, and f.py anyways. That's mostly just for printing text.
# Also, since this is old code, this serves as a cool reminder that I didn't code this well at all, and working offline definitely slowed me down and helped me refine some stuff.

global playerPosX
global playerPosY
global loadedMap
global feedback

# # MAP DATA # #

# TUTORIAL MAPS #

def template():
    global mapID
    global mapSize
    global spawnPoint
    global wallPos
    global longWallPos
    global inaccessiblePos
    global potentialMachPos
    global forcedMachPos
    global interactablePos
    global objectivePos
    
    mapID = "template"
    mapSize = [4, 4]
    spawnPoint = [2, 2]
    wallPos = []
    longWallPos = []
    inaccessiblePos = []
    potentialMachPos = []
    # forcedMachPos = []
    # interactablePos = []
    # objectivePos = []

def testMapA():
    global mapID
    global mapSize
    global spawnPoint
    global wallPos
    global longWallPos
    global inaccessiblePos
    global potentialMachPos
    global forcedMachPos
    global interactablePos
    global objectivePos
    mapID = "test"
    mapSize = [4, 4]
    spawnPoint = [0, 0]
    wallPos = [0, 1]
    longWallPos = [4, 0, "up", 5]
    inaccessiblePos = [0, 4]
    potentialMachPos = [0, 2]
    forcedMachPos = [0, 3]
    interactablePos = [2, 4]
    objectivePos = [3, 4]

def tutorialLobby():			# May be reused as a "menu" of sorts.
    global mapID
    global mapSize
    global spawnPoint
    global wallPos
    global longWallPos
    global inaccessiblePos
    global potentialMachPos
    global forcedMachPos
    global interactablePos
    global objectivePos
    
    mapID = "t0-v1"				# Tutorial Lobby
    mapSize = [25, 29]			# 26x30 map area.
    spawnPoint = [11, 14]		# Spawn on "S"
    wallPos = [3, 3, 9, 6, 9, 0, 12, 0, 13, 0, 16, 0, 18, 2, 18, 3, 16, 6, 22, 3, 21, 14, 22, 14, 21, 13, 22, 13, 0, 19, 0, 20, 1, 19, 1, 20, 24, 19, 24, 20, 0, 27, 0, 26, 1, 27, 1, 26]
    longWallPos = [0, 0, "up", 12, 1, 0, "up", 4, 2, 0, "up", 4, 3, 0, "right", 4, 1, 4, "right", 5, 1, 5, "right", 9, 1, 9, "right", 8, 9, 8, "up", 10, 3, 10, "right", 6, 0, 15, "right", 9, 3, 11, "up", 4, 16, 8, "up", 10, 25, 0, "up", 21, 16, 5, "right", 9, 24, 0, "up", 5, 23, 0, "up", 5, 0, 18, "right", 5, 20, 4, "right", 3, 17, 9, "right", 8, 17, 15, "right", 6, 21, 12, "right", 4, 17, 17, "right", 8, 0, 16, "right", 9, 0, 17, "right", 9, 21, 18, "right", 4, 9, 20, "right", 8, 0, 29, "right", 9, 0, 28, "right", 6]
    inaccessiblePos = [7,0, 8, 0, 10, 0, 11, 0, 14, 0, 15, 0, 17, 0, 18, 0]
    potentialMachPos = []
    forcedMachPos = []
    interactablePos = [6, 2, 1, 8, 0, 13, 10, 12, 15, 13, 15, 16, 23, 8]
    objectivePos = []
    
# # MAP LOADER # #

def readLongWall():					# Reads "longWallPos" and decompresses it into "wallPos"
    index = 0
    if len(longWallPos) % 4 != 0:	# Error handling.
        print("Critical error in mapmaking! Long walls are not correctly created. Stopping to prevent errors.")
        print("Walls created with \"longWallPos\" will not be added to the map.")
    else:
        reading = True
        while(reading):
            X = longWallPos[index]					# Gets the beginning X position.
            Y = longWallPos[index + 1]				# Gets the beginning Y position.
            toDirection = longWallPos[index + 2]	# Determines the direction to make the wall.
            lengthOfWall = longWallPos[index + 3]	# Determines the length of the wall.
            
            wallPos.append(X)
            wallPos.append(Y)
            for i in range(lengthOfWall - 1):		# Generates numbers from 0 to lengthOfWall-1
                                                    # For example, if we were loading the test map, then we would need to:
                                                    # - Subtract 1 from lengthOfWall (5 - 1) because we already marked one wall.
                                                    # - Iterate 4 more times (which is the sum of 5 - 1) to get desired length.
                if toDirection == "up":
                    Y += 1
                elif toDirection == "down":
                    Y -= 1
                elif toDirection == "left":
                    X -= 1
                elif toDirection == "right":
                    X += 1
                else:
                    print("Critical error in mapmaking! Long walls are not correctly created. Stopping to prevent errors.")
                    print("Walls created with \"longWallPos\" will not be added to the map.")
                    reading = False
                    break
                wallPos.append(X)
                wallPos.append(Y)
            index += 4
            if index > len(longWallPos)-1:
                reading = False

def stringifyWallCoords():
    index = 0
    global stringedWall
    stringedWall = []
    if len(wallPos) % 2 != 0 or len(wallPos) == 0:
        if(wallPos):
            print("Critical error in mapmaking! Walls are not properly created. Stopping to prevent errors.")
            print("Walls will not be added to the map.")
            reading = False
        else:
            reading = False
    else:
        reading = True
        while(reading):
            X = wallPos[index]
            Y = wallPos[index+1]
            stringedWall.append(str(X) + ", " + str(Y))
            index += 2
            if index > len(wallPos)-1:
                reading = False
                
def stringifyInaccessible():
    index = 0
    global stringedInaccessible
    stringedInaccessible = []
    if len(inaccessiblePos) % 2 != 0 or len(inaccessiblePos) == 0:
        if(inaccessiblePos):
            print("Critical error in mapmaking! Inaccessible areas are not properly created. Stopping to prevent errors.")
            print("Inaccessible areas will not be added to the map.")
            reading = False
        else:
            reading = False
    else:
        reading = True
        while(reading):
            X = inaccessiblePos[index]
            Y = inaccessiblePos[index+1]
            stringedInaccessible.append(str(X) + ", " + str(Y))
            index += 2
            if index > len(inaccessiblePos)-1:
                reading = False

def stringifyMachine():
    index = 0
    global stringedPotentialMach
    stringedPotentialMach = []
    if len(potentialMachPos) % 2 != 0 or len(potentialMachPos) == 0:
        if(potentialMachPos):
            print("Critical error in mapmaking! Potential machines are not properly created. Stopping to prevent errors.")
            print("Potential machines will not be added to the map.")
            reading = False
        else:
            reading = False
    else:
        reading = True
        while(reading):
            X = potentialMachPos[index]
            Y = potentialMachPos[index+1]
            stringedPotentialMach.append(str(X) + ", " + str(Y))
            index += 2
            if index > len(potentialMachPos)-1:
                reading = False
    ####################################################
    index = 0
    global stringedForcedMach
    stringedForcedMach = []
    if len(forcedMachPos) % 2 != 0 or len(forcedMachPos) == 0:
        if(forcedMachPos):
            print("Critical error in mapmaking! Forced machines are not properly created. Stopping to prevent errors.")
            print("Forced machines will not be added to the map.")
            reading = False
        else:
            reading = False
    else:
        reading = True
        while(reading):
            X = forcedMachPos[index]
            Y = forcedMachPos[index+1]
            stringedForcedMach.append(str(X) + ", " + str(Y))
            index += 2
            if index > len(forcedMachPos)-1:
                reading = False

def stringifyInterestPoints():
    index = 0
    global stringedInteractable
    stringedInteractable = []
    if len(interactablePos) % 2 != 0 or len(interactablePos) == 0:
        if(interactablePos):
            print("Critical error in mapmaking! Interactable areas are not properly created. Stopping to prevent errors.")
            print("Interactable areas will not be added to the map.")
            reading = False
        else:
            reading = False
    else:
        reading = True
        while(reading):
            X = interactablePos[index]
            Y = interactablePos[index+1]
            stringedInteractable.append(str(X) + ", " + str(Y))
            index += 2
            if index > len(interactablePos)-1:
                reading = False
    ####################################################
    index = 0
    global stringedObjective
    stringedObjective = []
    if len(objectivePos) % 2 != 0 or len(objectivePos) == 0:
        if(objectivePos):
            print("Critical error in mapmaking! Objectives are not properly created. Stopping to prevent errors.")
            print("Objectives will not be added to the map.")
            reading = False
        else:
            reading = False
    else:
        reading = True
        while(reading):
            X = objectivePos[index]
            Y = objectivePos[index+1]
            stringedObjective.append(str(X) + ", " + str(Y))
            index += 2
            if index > len(objectivePos)-1:
                reading = False

def buildMapFromStrings():
    Y = 0
    stringToAppend = ""
    building = True
    while(building):
        for i in range(mapSize[0] + 1):
            check = str(i) + ", " + str(Y)
            if check == str(spawnPoint[0]) + ", " + str(spawnPoint[1]):
                stringToAppend += "1"
            elif check in stringedWall:
                stringToAppend += "2"
            elif check in stringedInaccessible:
                stringToAppend += "3"
            elif check in stringedForcedMach:
                stringToAppend += "4"
            elif check in stringedInteractable:
                stringToAppend += "5"
            elif check in stringedObjective:
                stringToAppend += "6"
            else:
                stringToAppend += "0"
        loadedMap.append(stringToAppend)
        stringToAppend = ""
        Y += 1
        if(Y > mapSize[1]):
            building = False
            
            

def initLoadedMap():
    global loadedMap
    global noclip
    loadedMap = []
    noclip = False
    #############################################################
    readLongWall()
    stringifyWallCoords()
    stringifyInaccessible()
    stringifyMachine()
    stringifyInterestPoints()
    buildMapFromStrings()
    global playerPosX
    playerPosX = spawnPoint[0]
    global playerPosY
    playerPosY = spawnPoint[1]    


# # MAP READER # #

def convertRawMap(x, y): # THIS IS NEWER CODE, NOT OLD!
    if x < 0 or y < 0:
        return "\033[90m#\033[0m"
    if x > mapSize[0] or y > mapSize[1]:
        return "\033[90m#\033[0m"
    widthFloorRead = loadedMap[y]
    position = widthFloorRead[x]
    if position == "1":
            return "\033[36mE\033[0m"
    elif position == "2":
        return "\033[90m#\033[0m"
    elif position == "3":
        return "\033[38;5;166mX\033[0m"
    elif position == "4":
        return "\033[91mM\033[0m"
    elif position == "5":
        return "\033[95m?\033[0m"
    elif position == "6":
        return "\033[93m!\033[0m"
    else:
        return " "

def formatSlots(isFilled, slot):
    if isFilled:
        print(" { " + slot[1] + " - HP: " + str(slot[2]) + " - STAMINA: " + str(slot[3]) + " }")
    else:
        print(" { E M P T Y  S L O T ! }")

def printMapInterface():
    posX = playerPosX
    posY = playerPosY
    print("_________________________________________________________________")
    print("|(| " + convertRawMap(posX - 3, posY + 3) + " | " + convertRawMap(posX - 2, posY + 3) + " | " + convertRawMap(posX - 1, posY + 3) + " | " 	+ convertRawMap(posX, posY + 3) + " | " + convertRawMap(posX + 1, posY + 3) + " | " + convertRawMap(posX + 2, posY + 3) + " | " + convertRawMap(posX + 3, posY + 3) + " |)|      @ - < | Party | > - @      ")
    print("|(| - + - + - + - + - + - + - |)|")
    print("|(| " + convertRawMap(posX - 3, posY + 2) + " | " + convertRawMap(posX - 2, posY + 2) + " | " + convertRawMap(posX - 1, posY + 2) + " | " 	+ convertRawMap(posX, posY + 2) + " | " + convertRawMap(posX + 1, posY + 2) + " | " + convertRawMap(posX + 2, posY + 2) + " | " + convertRawMap(posX + 3, posY + 2) + " |)|", end="")
    formatSlots(d.s1[0], d.s1)
    print("|(| - + - + - + - + - + - + - |)|")
    print("|(| " + convertRawMap(posX - 3, posY + 1) + " | " + convertRawMap(posX - 2, posY + 1) + " | " + convertRawMap(posX - 1, posY + 1) + " | " 	+ convertRawMap(posX, posY + 1) + " | " + convertRawMap(posX + 1, posY + 1) + " | " + convertRawMap(posX + 2, posY + 1) + " | " + convertRawMap(posX + 3, posY + 1) + " |)|", end="")
    formatSlots(d.s2[0], d.s2)
    print("|(| - + - + - + - + - + - + - |)|")
    print("|(| " + convertRawMap(posX - 3, posY) + " | " + convertRawMap(posX - 2, posY) + " | " + convertRawMap(posX - 1, posY) + 									" | ^ | " 					+ convertRawMap(posX + 1, posY) + " | " + convertRawMap(posX + 2, posY) + " | " + convertRawMap(posX + 3, posY) + " |)|", end="")
    formatSlots(d.s3[0], d.s3)
    print("|(| - + - + - + - + - + - + - |)|")
    print("|(| " + convertRawMap(posX - 3, posY - 1) + " | " + convertRawMap(posX - 2, posY - 1) + " | " + convertRawMap(posX - 1, posY - 1) + " | " 	+ convertRawMap(posX, posY - 1) + " | " + convertRawMap(posX + 1, posY - 1) + " | " + convertRawMap(posX + 2, posY - 1) + " | " + convertRawMap(posX + 3, posY - 1) + " |)|", end="")
    formatSlots(d.s4[0], d.s4)
    print("|(| - + - + - + - + - + - + - |)|")
    print("|(| " + convertRawMap(posX - 3, posY - 2) + " | " + convertRawMap(posX - 2, posY - 2) + " | " + convertRawMap(posX - 1, posY - 2) + " | " 	+ convertRawMap(posX, posY - 2) + " | " + convertRawMap(posX + 1, posY - 2) + " | " + convertRawMap(posX + 2, posY - 2) + " | " + convertRawMap(posX + 3, posY - 2) + " |)|")
    print("|(| - + - + - + - + - + - + - |)|")
    print("|(| " + convertRawMap(posX - 3, posY - 3) + " | " + convertRawMap(posX - 2, posY - 3) + " | " + convertRawMap(posX - 1, posY - 3) + " | " 	+ convertRawMap(posX, posY - 3) + " | " + convertRawMap(posX + 1, posY - 3) + " | " + convertRawMap(posX + 2, posY - 3) + " | " + convertRawMap(posX + 3, posY - 3) + " |)|")
    
# # Map Interaction # #

def triggerCheck(checking): # THIS IS NEWER CODE, NOT OLD!
    # Check for walls.
    if "#" in checking:
        if noclip == False:
            return "wall"
        else:
            return "ok"
    elif "X" in checking:
        if noclip == False:
            return "noaccess"
        else:
            return "ok"
    elif "!" in checking:
        return "objective"
    elif "E" in checking:
        return "elevator"
    else:
        return "ok"

def move(dir):
    global playerPosX
    global playerPosY
    
    if dir == "Key.up":
        check = triggerCheck(convertRawMap(playerPosX, playerPosY + 1))
        if check == "ok":
            playerPosY += 1
        elif check == "wall":
            None
        elif check == "noaccess":
            None
            # handle "can't enter" dialouge
        elif check == "objective":
            None
            # handle objective trigger per map
        elif check == "elevator":
            # if panic == "true":
                # handle floor end
            # else:
            playerPosY += 1
    elif dir == "Key.down":
        check = triggerCheck(convertRawMap(playerPosX, playerPosY - 1))
        if check == "ok":
            playerPosY -= 1
        elif check == "noaccess":
            None
        elif check == "objective":
            None
            # handle objective trigger per map
        elif check == "elevator":
            # if panic == "true":
                # handle floor end
            # else:
            playerPosY -= 1
    elif dir == "Key.left":
        check = triggerCheck(convertRawMap(playerPosX - 1, playerPosY))
        if check == "ok":
            playerPosX -= 1
        elif check == "noaccess":
            None
        elif check == "objective":
            None
            # handle objective trigger per map
        elif check == "elevator":
            # if panic == "true":
                # handle floor end
            # else:
            playerPosX -= 1
    elif dir == "Key.right":
        check = triggerCheck(convertRawMap(playerPosX + 1, playerPosY))
        if check == "ok":
            playerPosX += 1
        elif check == "noaccess":
            None
        elif check == "objective":
            None
            # handle objective trigger per map
        elif check == "elevator":
            # if panic == "true":
                # handle floor end
            # else:
            playerPosX += 1

# # DEV TESTING!!!!!!!!!! # #

def mapRetrievingTesting(x, y):
    widthFloorRead = loadedMap[y]
    position = widthFloorRead[x]
    return position

def moveInMap():
    moving = True
    global noclip
    feedback = ""
    while moving:
        printMapInterface()
        print("|| ", end="")
        b.p(feedback)
        movement = f.kMove()
        if movement == "p":
            moving = False
        if movement == "z":
            b.p("interact!! ")
        if movement == "x":
            noclip = not noclip
            print()
            b.pAlert("noclip toggled! press key to continue.")
        else:
            move(movement)
        print()
        b.clearConsole()
        
def printRawMap():
    index = len(loadedMap) - 1
    while(index >= 0):
        print(loadedMap[index])
        index -= 1
        


def mapTesting():
    b.clearConsole()
    tutorialLobby()
    initLoadedMap()
    d.s1[0] = True
    d.s2[0] = True
    d.s3[0] = True
    d.s4[0] = True
    global noclip
    noclip = False
    printRawMap()
    print("! ! ! USE P TO EXIT THE PROGRAM ! ! !")
    moveInMap()