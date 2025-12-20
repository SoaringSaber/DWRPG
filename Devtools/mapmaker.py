# DWRPG Mapmaker - Devtool

class col:
    white			= '\033[97m'
    b_gray			= '\033[38;2;153;153;153m'
    gray			= '\033[90m'
    d_gray			= '\033[38;2;105;105;105m'
    black			= '\033[30m'
    white			= '\033[37m'
    
    d_red			= '\033[38;2;139;0;0m'
    red				= '\033[31m'
    b_red			= '\033[91m'
    d_orange		= '\033[38;2;255;69;0m'
    orange			= '\033[38;2;255;165;0m'
    brown			= '\033[38;2;150;75;0m'
    b_orange		= '\033[38;2;255;140;0m'
    d_yellow		= '\033[38;2;255;215;0m'
    yellow			= '\033[38;2;255;255;0m'
    b_yellow		= '\033[38;2;240;230;140m'
    d_green			= '\033[38;2;34;139;34m'
    green			= '\033[32m'
    b_green			= '\033[92m'
    d_blue			= '\033[34m'
    cyan			= '\033[36m'
    blue			= '\033[94m'
    b_blue			= '\033[38;2;135;206;235m'
    b_cyan			= '\033[96m'
    d_purple		= '\033[38;2;128;0;128m'
    purple			= '\033[38;2;147;112;219m'
    pink			= '\033[38;2;221;160;221m'
    ul				= '\033[4m'
    inverse			= '\033[7m'
    reset			= '\033[0m'

toCreate = {
        "mapID": "make",
        "mapSize": [0, 0],
        "playerSpawn": [0, 0],
        "floorColor": "\033[38;2;186;140;99m",
        "wallColor": "\033[90m",
        }

def initBlankMap():
    yLen = int(toCreate["mapSize"][1]) + 1	# Add 1 to length of map, because "range()" stinks.
    xLen = int(toCreate["mapSize"][0]) + 1
    for y in range(yLen):								# Start at zero and go to the length of Y.
        for x in range(xLen):							# Start at zero and go to the length of X the amount of Y's there are.
            toCreate["mapData"][x][y] = {				# Assign the plot some blank default data.
                    "obstacle": " ",
                    "color": "\033[7m" + toCreate["floorColor"]
                    }
    # print(toCreate["mapData"])

def getPlotData(x, y, colored=True):
    if colored:
        return toCreate["mapData"][x][y]["color"] + toCreate["mapData"][x][y]["obstacle"] + "\033[0m"
    return toCreate["mapData"][x][y]["obstacle"]

def printWholeMap(colored=True):
    yLimit = int(toCreate["mapSize"][1])
    xLimit = int(toCreate["mapSize"][0])
    for y in reversed(range(yLimit + 1)):
        for x in range(xLimit + 1):
            # Pass coordinates directly to your data function
            print(getPlotData(x, y, colored), end="")
        print() # Move to the next line after finishing a row

# Map Creation Commands

# # createObstacle - Creates a type of obstacle at X and Y (for a specific length, if required).
# # # Available "wallType" methods.
    # "single"         - Creates a single wall.
    # "long"           - Creates a long wall heading towards "toDirection" for "length".

def createObstacle(obstacleType, X, Y, toDirection="up", length=1, color=None):
    if obstacleType == "single":
        if color == None:
            color = toCreate["wallColor"]
        toCreate["mapData"][X][Y] = {
                    "obstacle": "#",
                    "color": "\033[7m" + color
                    }
    elif obstacleType == "long":
        if color == None:
            color = toCreate["wallColor"]
        toCreate["mapData"][X][Y] = {
                    "obstacle": "#",
                    "color": "\033[7m" + color
                    }
        for i in range(length-1):
            if toDirection == "up" or toDirection == "u":
                Y += 1
            elif toDirection == "down" or toDirection == "d":
                Y -= 1
            elif toDirection == "left" or toDirection == "l":
                X -= 1
            elif toDirection == "right" or toDirection == "r":
                X += 1
            else:
                break
            toCreate["mapData"][X][Y] = {
                    "obstacle": "#",
                    "color": "\033[7m" + color
                    }
    elif obstacleType == "floorSingle":
        if color == None:
            color = toCreate["floorColor"]
        toCreate["mapData"][X][Y] = {
                    "obstacle": " ",
                    "color": "\033[7m" + color
                    }
    elif obstacleType == "floorLong":
        if color == None:
            color = toCreate["floorColor"]
        toCreate["mapData"][X][Y] = {
                    "obstacle": " ",
                    "color": "\033[7m" + color
                    }
        for i in range(length-1):
            if toDirection == "up" or toDirection == "u":
                Y += 1
            elif toDirection == "down" or toDirection == "d":
                Y -= 1
            elif toDirection == "left" or toDirection == "l":
                X -= 1
            elif toDirection == "right" or toDirection == "r":
                X += 1
            else:
                break
            toCreate["mapData"][X][Y] = {
                    "obstacle": " ",
                    "color": "\033[7m" + color
                    }
    elif obstacleType == "elevator":
        if color == None:
            color = "\033[36m"
        toCreate["mapData"][X][Y] = {
                    "obstacle": "E",
                    "color": "\033[7m" + color
                    }
        for i in range(length-1):
            if toDirection == "up" or toDirection == "u":
                Y += 1
            elif toDirection == "down" or toDirection == "d":
                Y -= 1
            elif toDirection == "left" or toDirection == "l":
                X -= 1
            elif toDirection == "right" or toDirection == "r":
                X += 1
            else:
                break
            toCreate["mapData"][X][Y] = {
                    "obstacle": "E",
                    "color": "\033[7m" + color
                    }
    else:
        print("Error.")
        
def createInteractable(interactableType, X, Y, interactID=-1, triggerID=-1, color=None):
    if interactableType == "interact":
        if color == None:
            color = "\033[95m"
        toCreate["mapData"][X][Y] = {
                        "obstacle": "?",
                        "interactID": interactID,
                        "color": "\033[7m" + color
                                    }
        if triggerID != -1:
            toCreate["mapData"][X][Y]["triggerID"] = triggerID	# If you want to psyche out the player by making the interactable point an objective one, go ahead lmao.
    elif interactableType == "objective":						# Interactable, upon touching, will trigger from triggerID.
        if color == None:
            color = "\033[93m"
        toCreate["mapData"][X][Y] = {
                        "obstacle": "!",
                        # interactIDs won't be able to be used for objective points, as touching them triggers the triggerID.
                        "triggerID": triggerID,					# triggerID is required for objective points.
                        "color": "\033[7m" + color
                        }
    elif interactableType == "inaccessable":					# Fancy walls, but interactIDs trigger when bumped into.
        if color == None:
            color = "\033[38;5;166m"
        toCreate["mapData"][X][Y] = {
                    "obstacle": "X",				# Change this value to change what "inaccessable" plots look like.
                    "triggerID": triggerID,
                    "color": "\033[7m" + color
                    }

def createCustomObstacle(obStr, X, Y, interactID=-1, triggerID=-1, color=""):
    # TODO: Make script to create custom 1-character obstacles.
    None

def templateMap():
    # # # Map Properties # # #
    toCreate["mapID"]       = "template"				# Set the map's name. Make this unique and immutable!
    toCreate["mapSize"]     = [58, 58]					# Set the map's size. Smaller maps will be SUPER cramped for the player.
    toCreate["playerSpawn"] = [0, 0]					# If the speed will remain a static "2", do not make any value odd.
    toCreate["floorColor"]  = "\033[38;2;186;140;99m"	# Set the default floor color.
    toCreate["wallColor"]   = "\033[90m"				# Set the default wall color.
    toCreate["mapData"] = [[None for y in range(toCreate["mapSize"][1] + 1)] for x in range(toCreate["mapSize"][0] + 1)]
    # # # Map Setup # # #
    initBlankMap()
    # # # Map Building # # #
    
    # Your building starts here!
    
    createObstacle("long", 1, 1, "up", 5)						# To create a long wall:
                                                        # Define the obstacle type as "long".
                                                        # Define the starting X and Y value.
                                                        # Define which direction the wall will go. ("u", "d", "l", "r").
                                                        # Define the length of the wall.
                                                        # Optionally, you can define a custom color of the wall.
                                                            # To do this, just add "color=<your-color>" to the arguments.
                                                            # Excluding this argument gives a default color to the point, which is gray.
    createObstacle("single", 1, 7)								# To create a singular piece of wall:
                                                        # Define the obstacle type as "single".
                                                        # Define the X and Y value.
                                                        # Optionally, you can define a custom color of the wall.
                                                            # To do this, just add "color=<your-color>" to the arguments.
                                                            # Excluding this argument gives a default color to the point, which is gray.
    createObstacle("floorLong", 2, 1, "up", 5, col.red)			# To create a strip of a different colored floor:
                                                        # Define the obstacle type as "floorLong".
                                                        # Define the starting X and Y value.
                                                        # Define which direction the "floor strip" will go. ("u", "d", "l", "r").
                                                        # Define the length of the strip.
                                                        # Define a color.
    createObstacle("floorSingle", 2, 7, color=col.red)			# To change a single piece of flooring:
                                                        # Define the obstacle type as "floorSingle".
                                                        # Define the X and Y value.
                                                        # Define a color.
    createInteractable("interact", 3, 1, 0)						# To add an interactable point on the map:
                                                        # Define the type as "interact".
                                                        # Define the X and Y value.
                                                        # Define the interactID that will trigger an event when interacted with.
                                                        # Optionally, you can define a custom color of the interactable point.
                                                            # To do this, just add "color=<your-color>" to the arguments.
                                                            # Excluding this argument gives a default color to the point, which is purple.
    createInteractable("objective", 3, 2, triggerID=0)			# To add an objective point/trigger on the map:
                                                        # Define the type as "objective".
                                                        # Define the X and Y value.
                                                        # Define the triggerID that will trigger an event when player moves into it.
                                                        # Optionally, you can define a custom color of the objective.
                                                            # To do this, just add "color=<your-color>" to the arguments.
                                                            # Excluding this argument gives a default color to the point, which is yellow.
    createInteractable("inaccessable", 3, 3, triggerID=0)		# To add an inaccessable area (such as a locked door) to the map:
                                                        # Define the type as "inaccessable".
                                                        # Define the X and Y value.
                                                        # Define the triggerID that correlates with that "door".
                                                            # Note that the trigger, if the "inaccessable" area is passable, would need to move the player itself past the 
    createObstacle("elevator", 4, 1, "up", 5)					# To add an elevator line to the map:
                                                        # Define the type as "elevator".
                                                        # Define the X and Y value.
                                                        # Define which direction the "elevator line" will go. ("u", "d", "l", "r").
                                                        # Define the length of the line.
                                                        # Optionally, you can define a custom color of the elevator.
                                                            # To do this, just add "color=<your-color>" to the arguments.
                                                            # Excluding this argument gives a default color to the point, which is cyan.
    createObstacle("elevator", 4, 7, length=1)					# You cannot make single elevators, but if you must, make "length=1" and ignore direction.
    # # # Display Final Product # # #
    printWholeMap()										# Print the whole map. This might be a bit laggy in some IDEs.
    print(toCreate["mapID"] + " = " + str(toCreate))	# Print the entire variable to paste to e.py - This might crash your IDE if you try pasting a huge map into it, so try it through a text editor?
    
templateMap()