# Settings and Misc - c

# Temporary memory and setting values is stored here.
# String variables are stored into "stringmem", int variables are stored into "intmem", and double/float values are "decimem".
# All are put into an array, returns index, even if you don't need it.

# # Setting Variables # #

userName = "PLAYER"			# The player's name.
ichor = "ichor"				# The Toon's blood, or the stuff Machines run on.
ts = .025					# The text's scrolling speed.
doColorNames = True

def onLaunch():
    import os
    if os.name == 'nt':		# For Windows
        os.system('cls')
        # DO STUFF FOR WINDOWS PLAYERS IDK
    else:					# For Linux/macOS
        os.system('clear')
        # DO STUFF FOR AMAZING PEOPLE IDK

def changeTextSpeed(speed):
    textSpeed = speed