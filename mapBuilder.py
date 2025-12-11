# Map Creator

global playerPosX
global playerPosY
global loadedMap

# # MAP DATA # #

# TUTORIAL MAPS #

def template():
    global mapID					# Identifies the map for interactables and objectives to work.
    global mapSize					# Establishes a boundary.
                                    # There's no need to add walls to the borders, as the movement handler will block out-of-bounds access.
                                    # It is heavily reccommended to set the size to greater than 25x25 to accomodate lots of machine positions (caps at 20).
    global spawnPoint				# Sets the party's position to this place when loading map.
                                    # PLEASE READ!!! spawnPoint PLACES "ELEVATOR MARKERS" IN MAPBUILDER.
                                    # YOU NEED TO SET DEDICATED SPAWN POINTS IN THE ACTUAL GAME!
                                    # The spawn point would usually be outside of an elevator or at a special area for the Story mode.
    global wallPos					# Creates a block on the position. Values span 2 indexes, the x position, and the y position.
                                    # Printed as a gray "#". Signified as a 2 in mapData.
                                    # These are singular placements, which make an easy way to put obstacles/corners down.
    global longWallPos				# Creates a wall of blocks to four directions for a specified length, spans 4 indexes.
                                    # The first two indexes are the starting x and y positions.
                                    # The third index is a string that determines the direction. Valid inputs are "up"/"u", "down"/"d", "left"/"l", or "right"/"r".
                                    # The fourth index determines the length of the wall. It is recommended to use long walls for walls larger than 2 spaces.
    global inaccessiblePos			# Creates a block of inaccessible area.
                                    # Printed as an orange "X" Signified as a 3 in mapData.
                                    # The leading Toon will make a comment along the lines of: "I can't go over there, right now."
                                    # This is essentially acting as a fancy wall.
    global potentialMachPos			# Marks the coordinates for a potential machine to be placed.
                                    # Is not printed or shown in mapData.
                                    # This doesn't guaruntee a machine would spawn there, as the loader will shuffle and psuedo-randomly choose the capped amount.
                                    # There is a requirement of a minimum 20 positions to place machines because of the machine cap.
    global forcedMachPos			# Creates a machine at this position.
                                    # Printed as a red "M" until it is completed, in which case it will turn green. Not shown in mapData.
                                    # Guaruntees a machine will spawn at that position.
                                    # Not recommended unless being put to use for Story mode.
    global interactablePos			# Creates a marker to signify that something can be interactable at the position.
                                    # Printed as a purple "?". Signified as a 4 in mapData.
                                    # This does nothing becides be there.
                                    # In order to have the "?" be interactable, code something under the "interact()" function for the mapID and position.
    global objectivePos				# Creates a trigger area to do one thing, cannot be used for seperate things. (This may be altered in a future update.)
                                    # Printed as a yellow "!". Signified as a 5 in mapData.
                                    # Only for use in Story mode. Player cannot move into the objective.
                                    # In order for the objective to work, code something under the "objective()" function for the mapID.
    
    mapID = "template"
    mapSize = [6, 6]
    spawnPoint = [3, 3]
    wallPos = []
    longWallPos = []
    inaccessiblePos = []
    potentialMachPos = []
    forcedMachPos = []
    interactablePos = []
    objectivePos = []

def mapToBuild():
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
    mapID = "buildingMap"
    mapSize = [25, 45]
    spawnPoint = []
    wallPos = [3, 10, 4, 10, 9, 6, 12, 6, 13, 6, 16, 6, 10, 14, 15, 14, 3, 18, 2, 23]
    longWallPos = [0, 3, "r", 6, 20, 3, "r", 6, 0, 6, "r", 8, 18, 6, "r", 8, 0, 7, "r", 5, 20, 7, "r", 6, 16, 8, "u", 4, 20, 8, "r", 6, 0, 10, "u", 9, 1, 10, "u", 9, 2, 10, "u", 11, 20, 10, "r", 6, 19, 11, "r", 7, 18, 12, "r", 8, 3, 13, "r", 8, 3, 12, "r", 5, 3, 11, "r", 4, 15, 13, "r", 11, 10, 17, "u", 8, 15, 17, "u", 8, 5, 18, "r", 5, 6, 19, "u", 4, 2, 24, "r", 8, 16, 18, "r", 7]
    inaccessiblePos = [8, 6, 10, 6, 11, 6, 14, 6, 15, 6, 17, 6, 4, 8, 4, 9, 20, 9, 23, 14, 23, 15]
    potentialMachPos = []
    forcedMachPos = []
    interactablePos = [18, 8, 8, 10, 3, 14, 7, 14, 4, 17, 20, 17, 21, 17]
    objectivePos = []

# # MAP COMPILING # #

def readLongWall():					# Reads "longWallPos" and decompresses it into "wallPos"
    index = 0
    if len(longWallPos) % 4 != 0:	# Error handling.
        print("Critical error in mapmaking! Long walls are not correctly created. Stopping to prevent errors.")
        print("Walls created with \"longWallPos\" will not be added to the map.")
    else:
        if longWallPos == []:
            reading = False
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
                if toDirection == "up" or toDirection == "u":
                    Y += 1
                elif toDirection == "down" or toDirection == "d":
                    Y -= 1
                elif toDirection == "left" or toDirection == "l":
                    X -= 1
                elif toDirection == "right" or toDirection == "r":
                    X += 1
                else:
                    print("Critical error in mapmaking! Long walls are not correctly created. Stopping to prevent errors.")
                    print("Walls created with \"longWallPos\" will not be added to the map.")
                    reading = False
                    break
                wallPos.append(X)					# Append X first
                wallPos.append(Y)					# then append Y.
            None									# Ignore, this is a marker for end of "for" loop.
            index += 4								# Move to next long wall placement.
            if index > len(longWallPos)-1:			# Check if the index is going out of bounds, first.
                reading = False						# If it is, we're done.
        None										# Ignore, this is a marker for end of "while" loop.

def stringifyElevator():
    index = 0
    global stringedElevator
    stringedElevator = []
    if len(spawnPoint) % 2 != 0 or len(spawnPoint) == 0:						# Error handling.
        if(spawnPoint):
            print("Critical error in mapmaking! Inaccessible areas are not properly created. Stopping to prevent errors.")
            print("Inaccessible areas will not be added to the map.")
            reading = False
        else:
            reading = False
    else:
        reading = True
        while(reading):
            X = spawnPoint[index]
            Y = spawnPoint[index+1]
            stringedElevator.append(str(X) + ", " + str(Y))
            index += 2
            if index > len(spawnPoint)-1:
                reading = False

def stringifyWallCoords():							# Turns the two indexes of X and Y inside of "wallPos" into one string.
                                                    # The reason I'm doing this is because it'll make putting everything into the
                                                    # final map array pretty easy because they'll check for the string from here.
    index = 0
    global stringedWall
    stringedWall = []
    if len(wallPos) % 2 != 0 or len(wallPos) == 0:						# Error handling.
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
    if len(inaccessiblePos) % 2 != 0 or len(inaccessiblePos) == 0:						# Error handling.
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
    if len(potentialMachPos) % 2 != 0 or len(potentialMachPos) == 0:						# Error handling.
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
    if len(forcedMachPos) % 2 != 0 or len(forcedMachPos) == 0:						# Error handling.
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
    if len(interactablePos) % 2 != 0 or len(interactablePos) == 0:						# Error handling.
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
    if len(objectivePos) % 2 != 0 or len(objectivePos) == 0:						# Error handling.
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
        for i in range(mapSize[0] + 1):				# Generates numbers from 0 to X value of mapSize.
            check = str(i) + ", " + str(Y)
            if check in stringedElevator:
                stringToAppend += "1"
            elif check in stringedWall:
                stringToAppend += "2"
            elif check in stringedInaccessible:
                stringToAppend += "3"
            elif check in stringedInteractable:
                stringToAppend += "4"
            elif check in stringedObjective:
                stringToAppend += "5"
            else:
                stringToAppend += "0"
        loadedMap.append(stringToAppend)
        stringToAppend = ""
        Y += 1
        if(Y > mapSize[1]):
            building = False

def buildMap():
    global loadedMap
    loadedMap = []
    readLongWall()
    stringifyElevator()
    stringifyWallCoords()
    stringifyInaccessible()
    stringifyMachine()
    # rollMachs()
    stringifyInterestPoints()
    buildMapFromStrings()

# # # # # # # # # # # # # # # # # # # # # # # # #

def printRawMap():
    index = len(loadedMap) - 1
    while(index >= 0):
        print(loadedMap[index])
        index -= 1

# Builds map and prints the cool map data. Saves space in actual project by doing this.

mapToBuild()
buildMap()
print("Here's your map's ID:")
print(mapID)
print("Copy this to your mapData variable:")
print(loadedMap)
print("Copy this to your randMachPos variable:")
print(stringedPotentialMach)
print("Copy this to your forcedMachPos variable:")
print(stringedForcedMach)
print()
print()
print("Your map in data form:")
print("________________________")
printRawMap()