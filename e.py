# Map Manager / Navigator - e

import b, d, f

# Map data is stored here. It's also loaded here.

# # MAP DATA # #

# TESTING MAPS #

# DEVELOPER'S NOTE:
# Now that I had a better way to deal with data, I should really work on having the same done to maps, huh?
# Definitely would make maps a whole lot easier to import, huh?

def testMapA():
    global mapID
    global mapSize
    global spawnPoint
    global randMachPos
    global machPos
    global mapData
    mapID = "testA"
    mapSize = [4, 4]
    spawnPoint = [0, 0]
    randMachPos = ['0, 2']
    machPos = ['0, 3']
    mapData = ['10002', '20002', '00002', '00002', '30452']
    
def testMapB():
    global mapID
    global mapSize
    global spawnPoint
    global randMachPos
    global machPos
    global mapData
    mapID = "testB"
    mapSize = [4, 4]
    spawnPoint = [2, 2]
    randMachPos = []
    machPos = []
    mapData = ['22000', '22000', '22100', '22000', '22000']
    
def tutorOld():
    global mapID
    global mapSize
    global spawnPoint
    global randMachPos
    global machPos
    global mapData
    mapID = "olTutor"
    mapSize = [25, 29]
    spawnPoint = [11, 14]
    randMachPos = []
    machPos = []
    mapData = ['22222223323322332330000222', '22200000000000000000000222', '22200040000000000020000222', '22220000000000000020002222', '22222200000000000000222222', '22222222220000002222222222', '20000000020000002000000002', '20000000000000000000000002', '24000000020000002000000402', '22222222220000002222222222', '20022222220000002000000002', '20020000020000002000000002', '00020000024000002000022222', '40020000020000042000022002', '00020000020100002000022002', '22222222220000002222222002', '22222222220000042000000002', '22222222220000002222222222', '22222000000000000000022222', '22000000000000000000000022', '22000000022222222000000022', '00000000000000000000000000', '00000000000000000000000000', '00000000000000000000000000', '00000000000000000000000000', '00000000000000000000000000', '22000000000000000000000000', '22000000000000000000000000', '22222200000000000000000000', '22222222200000000000000000']

# # MAP LOADER

def initLoadMap():
    global noclip
    noclip = False
    # Roll the machs.
    global completeMach
    completeMach = []
    global spawnPoint
    global valveTurn
    valveTurn = 0
    global playerPosX
    playerPosX = spawnPoint[0]
    global playerPosY
    playerPosY = spawnPoint[1]

# # MAP READER # #

def checkPosition(posX, posY):
    stringedCheck = str(posX) + ", " + str(posY)
    if posX < 0 or posY < 0:
        return "\033[90m#\033[0m"
    if posX > mapSize[0] or posY > mapSize[1]:
        return "\033[90m#\033[0m"
    widthFloorRead = mapData[posY]		# Get the y value, and read the index from the map. Put the string into a variable.
    position = widthFloorRead[posX]		# Get the x value, and read the index in the string. You got what's in that position, yay!
    global machPos
    global completeMach
    if stringedCheck in completeMach:
        return "\033[92mM\033[0m"		# complete mach   - Green
    elif stringedCheck in machPos:
        return "\033[91mM\033[0m"		# incomplete mach - Red
    else:
        if position == "1":
            return "\033[36mE\033[0m"
        elif position == "2":
            return "\033[90m#\033[0m"
        elif position == "3":
            return "\033[38;5;166mX\033[0m"
        elif position == "4":
            return "\033[95m?\033[0m"
        elif position == "5":
            return "\033[93m!\033[0m"
        else:
            return " "

def formatSlots(slot):
    if slot["isActive"]:
        print(" { " + b.n(slot, True) + " - HP: " + str(slot["health"]) + "/" + str(slot["maxHealth"]) + " - STAMINA: " + str(slot["stamina"]) + "/" + str(slot["maxStamina"]) + " }")
    else:
        print(" { E M P T Y  S L O T ! }")

def renderPlayer(posX, posY):
    onPlayer = checkPosition(posX, posY)
    if "E" in onPlayer:
        return "\033[36m^\033[0m"
    elif "?" in onPlayer:
        return "\033[95m^\033[0m"
    elif "\033[92mM\033[0m" == onPlayer:
        return "\033[92m^\033[0m"
    elif "\033[91mM\033[0m" == onPlayer:
        return "\033[91m^\033[0m"
    else:
        return "^"

def printMapInterface():
    posX = playerPosX
    posY = playerPosY
    print("_________________________________________________________________")
    print("|(| " + checkPosition(posX - 3, posY + 3) + " | " + checkPosition(posX - 2, posY + 3) + " | " + checkPosition(posX - 1, posY + 3) + " | " 	+ checkPosition(posX, posY + 3) + " | " + checkPosition(posX + 1, posY + 3) + " | " + checkPosition(posX + 2, posY + 3) + " | " + checkPosition(posX + 3, posY + 3) + " |)|      @ - < | Party | > - @      ")
    print("|(| - + - + - + - + - + - + - |)|")
    print("|(| " + checkPosition(posX - 3, posY + 2) + " | " + checkPosition(posX - 2, posY + 2) + " | " + checkPosition(posX - 1, posY + 2) + " | " 	+ checkPosition(posX, posY + 2) + " | " + checkPosition(posX + 1, posY + 2) + " | " + checkPosition(posX + 2, posY + 2) + " | " + checkPosition(posX + 3, posY + 2) + " |)|", end="")
    formatSlots(d.s1)
    print("|(| - + - + - + - + - + - + - |)|")
    print("|(| " + checkPosition(posX - 3, posY + 1) + " | " + checkPosition(posX - 2, posY + 1) + " | " + checkPosition(posX - 1, posY + 1) + " | " 	+ checkPosition(posX, posY + 1) + " | " + checkPosition(posX + 1, posY + 1) + " | " + checkPosition(posX + 2, posY + 1) + " | " + checkPosition(posX + 3, posY + 1) + " |)|", end="")
    formatSlots(d.s2)
    print("|(| - + - + - + - + - + - + - |)|")
    print("|(| " + checkPosition(posX - 3, posY) + " | " + checkPosition(posX - 2, posY) + " | " + checkPosition(posX - 1, posY) + 					" | " + renderPlayer(posX, posY) + " | " 		+ checkPosition(posX + 1, posY) + " | " + checkPosition(posX + 2, posY) + " | " + checkPosition(posX + 3, posY) + " |)|", end="")
    formatSlots(d.s3)
    print("|(| - + - + - + - + - + - + - |)|")
    print("|(| " + checkPosition(posX - 3, posY - 1) + " | " + checkPosition(posX - 2, posY - 1) + " | " + checkPosition(posX - 1, posY - 1) + " | " 	+ checkPosition(posX, posY - 1) + " | " + checkPosition(posX + 1, posY - 1) + " | " + checkPosition(posX + 2, posY - 1) + " | " + checkPosition(posX + 3, posY - 1) + " |)|", end="")
    formatSlots(d.s4)
    print("|(| - + - + - + - + - + - + - |)|")
    print("|(| " + checkPosition(posX - 3, posY - 2) + " | " + checkPosition(posX - 2, posY - 2) + " | " + checkPosition(posX - 1, posY - 2) + " | " 	+ checkPosition(posX, posY - 2) + " | " + checkPosition(posX + 1, posY - 2) + " | " + checkPosition(posX + 2, posY - 2) + " | " + checkPosition(posX + 3, posY - 2) + " |)|")
    print("|(| - + - + - + - + - + - + - |)|")
    print("|(| " + checkPosition(posX - 3, posY - 3) + " | " + checkPosition(posX - 2, posY - 3) + " | " + checkPosition(posX - 1, posY - 3) + " | " 	+ checkPosition(posX, posY - 3) + " | " + checkPosition(posX + 1, posY - 3) + " | " + checkPosition(posX + 2, posY - 3) + " | " + checkPosition(posX + 3, posY - 3) + " |)|")
    
def printMapBlackout():
    posX = playerPosX
    posY = playerPosY
    print("_________________________________________________________________")
    print("|(\033[7m\033[90m| + | + | + | + | + | + | + |\033[0m)|      @ - < | Party | > - @      ")
    print("|(\033[7m\033[90m| - + - + - + - + - + - + - |\033[0m)|")
    print("|(\033[7m\033[90m| + |\033[0m " + checkPosition(posX - 2, posY + 2) + " | " + checkPosition(posX - 1, posY + 2) + " | " 	+ checkPosition(posX, posY + 2) + " | " + checkPosition(posX + 1, posY + 2) + " | " + checkPosition(posX + 2, posY + 2) + " \033[7m\033[90m| + |\033[0m)|", end="")
    formatSlots(d.s1)
    print("|(\033[7m\033[90m| - +\033[0m - + - + - + - + - \033[7m\033[90m+ - |\033[0m)|")
    print("|(\033[7m\033[90m| + |\033[0m " + checkPosition(posX - 2, posY + 1) + " | " + checkPosition(posX - 1, posY + 1) + " | " 	+ checkPosition(posX, posY + 1) + " | " + checkPosition(posX + 1, posY + 1) + " | " + checkPosition(posX + 2, posY + 1) + " \033[7m\033[90m| + |\033[0m)|", end="")
    formatSlots(d.s2)
    print("|(\033[7m\033[90m| - +\033[0m - + - + - + - + - \033[7m\033[90m+ - |\033[0m)|")
    print("|(\033[7m\033[90m| + |\033[0m " + checkPosition(posX - 2, posY) + " | " + checkPosition(posX - 1, posY) + 									" | ^ | " 					+ checkPosition(posX + 1, posY) + " | " + checkPosition(posX + 2, posY) + " \033[7m\033[90m| + |\033[0m)|", end="")
    formatSlots(d.s3)
    print("|(\033[7m\033[90m| - +\033[0m - + - + - + - + - \033[7m\033[90m+ - |\033[0m)|")
    print("|(\033[7m\033[90m| + |\033[0m " + checkPosition(posX - 2, posY - 1) + " | " + checkPosition(posX - 1, posY - 1) + " | " 	+ checkPosition(posX, posY - 1) + " | " + checkPosition(posX + 1, posY - 1) + " | " + checkPosition(posX + 2, posY - 1) + " \033[7m\033[90m| + |\033[0m)|", end="")
    formatSlots(d.s4)
    print("|(\033[7m\033[90m| - +\033[0m - + - + - + - + - \033[7m\033[90m+ - |\033[0m)|")
    print("|(\033[7m\033[90m| + |\033[0m " + checkPosition(posX - 2, posY - 2) + " | " + checkPosition(posX - 1, posY - 2) + " | " 	+ checkPosition(posX, posY - 2) + " | " + checkPosition(posX + 1, posY - 2) + " | " + checkPosition(posX + 2, posY - 2) + " \033[7m\033[90m| + |\033[0m)|")
    print("|(\033[7m\033[90m| - + - + - + - + - + - + - |\033[0m)|")
    print("|(\033[7m\033[90m| + | + | + | + | + | + | + |\033[0m)|")
    
# # Map Interaction # #

def moveToPos(posX, posY):
    global playerPosX
    global playerPosY
    playerPosX = posX
    playerPosY = posY

def triggerCheck(checking):
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
            
def interact(posX, posY):
    
    # Machine Interactions
    stringedCheck = str(posX) + ", " + str(posY)
    if stringedCheck in machPos and stringedCheck not in completeMach:
        global valveTurn
        global feedback
        valveTurn += 1
        if valveTurn == 5:
            completeMach.append(stringedCheck)
            feedback[0] = True
            feedback[1] = "You turn the valve once more, the machine fills up with a DING!"
            return True
        else:
            feedback[0] = True
            feedback[1] = "You turn the valve. ( " + str(valveTurn) + " / 5 )"
            return True
    elif stringedCheck in completeMach:
        feedback[0] = True
        feedback[1] = "This machine is already done."
        return True
    
    # Interactable Interactions
    global mapID
    if mapID == "testA":
        if posX == 2 and posY == 4:
            b.testingKeyboard()
            global blackout
            blackout = not blackout
            return True
        if posX == 3 and posY == 0:
            b.pAlert("Whoosh!")
            tutorOld()
            global spawnPoint
            moveToPos(spawnPoint[0], spawnPoint[1])
            return True
        if posX == 2 and posY == 0:
            if b.yesOrNo("Hey, wanna die?") == 1:
                b.pAction("TAKE THIS YOU FILTHY SCUM!!!!!!!")
                print(999999999/0)
            else:
                b.pAction("Suit yourself...")
                return True
    elif mapID == "olTutor":
        if posX == 10 and posY == 12:
            b.pDialouge("SOARING", "Hey, bud. How are you doing?")
            b.pDialouge(d.dandy, "It could be going better.")
            b.pDialouge("SOARING", "That's fair. Love ya.")
            b.pDialouge("SOARING", "Wishing you were actually real...")
            return True
        if posX == 15 and posY == 13:
            b.pAction("It's DYLE's little room.")
            b.pAction("Something small in a vast facility.")
            b.pAction("This dreary place will never see the light of day, anyways.")
            return True
    return False

def objective():
    global mapID
    if mapID == "testA":
        b.pAlert("You found me!")
        global playerPosX
        global playerPosY
        playerPosX = 0
        playerPosY = 0

def noEntryFeedback():
    b.pAlert("I can't go in there.")

def move(dir):
    global playerPosX
    global playerPosY
    global doClearConsole
    global noclip
    global valveTurn
    
    if not noclip:
        if dir == "Key.up":
            check = triggerCheck(checkPosition(playerPosX, playerPosY + 1))
        elif dir == "Key.down":
            check = triggerCheck(checkPosition(playerPosX, playerPosY - 1))
        elif dir == "Key.left":
            check = triggerCheck(checkPosition(playerPosX - 1, playerPosY))
        elif dir == "Key.right":
            check = triggerCheck(checkPosition(playerPosX + 1, playerPosY))
        else:
            check = ""
    else:
        check = "ok"
        
    if check == "wall":
        doClearConsole = False
    elif check == "noaccess":
        noEntryFeedback()
        doClearConsole = True
    elif check == "objective":
        objective()
        doClearConsole = True
    elif check == "elevator":
        check = "ok"
        doClearConsole = True
    if check == "ok":
        valveTurn = 0
        if dir == "Key.up":
            playerPosY += 1
        elif dir == "Key.down":
            playerPosY -= 1
        elif dir == "Key.left":
            playerPosX -= 1
        elif dir == "Key.right":
            playerPosX += 1
        doClearConsole = True

# # DEV TESTING # #

def moveInMap():
    # extremely bad code made only for testing maps and establishing how functions will run, will revamp later.
    moving = True
    global feedback
    feedback = [False, "text"]
    global doClearConsole
    doClearConsole = True
    global blackout
    blackout = False
    global noclip
    noclip = False
    global playerPosX
    global playerPosY
    while moving:
        if doClearConsole:
            b.clearConsole()
            doClearConsole = False
            print()
            if not blackout:
                printMapInterface()
            else:
                printMapBlackout()
        if(feedback[0] == True):
            print("|* ", end="")
            b.pln(feedback[1])
            feedback[0] = False
        movement = f.kMove()
        if movement == "p":
            b.pAlert("Unpaused.")
            doClearConsole = True
        if movement == "z":
            doClearConsole = interact(playerPosX, playerPosY)
        else:
            move(movement)
        
def printRawMap():
    index = len(mapData) - 1
    while(index >= 0):
        print(mapData[index])
        index -= 1

def mapTesting():
    tutorNew()
    global spawnPoint
    print(spawnPoint)
    initLoadMap()
    d.updateSlotStats(d.astro, 1, isActive=True)
    d.s2[0] = True
    d.s3[0] = True
    d.s4[0] = True
    global noclip
    noclip = False
    global completeMach
    completeMach = []
    moveInMap()