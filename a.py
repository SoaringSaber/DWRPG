# Game Launcher - a

# # # # # # # # # # # # # # # # # # # # # | - Dandy's World - The Text-Based RPG Game
# Dandy's World, The Text-Based RPG     # | - Quelver, SoaringSaber
# Original game by Quelver, Made by     # | - 
# SoaringSaber.                         # | - EST: 11/21/2025 - Hello, World!
#                                       # | - Version: PUBLIC CANARY
# # # # # # # # # # # # # # # # # # # # # | -

# Well, hello there, traveller!
# This is an UNFINISHED BUILD of DWRPG, name in progress. If you'd like to help out with development, DM "soaringsaber"
# on DISCORD! It'd be awesome to get some assistance! Of course, you can also always choose to "fork" this build and
# work off of it, but please link it to me and the original game, per the Eclipse License.

# This game tries its best to stay non-hard-coded, so if you find something that could be changed to be too specific,
# let Soaring (that's me!) know so I can fix it up. I try my best to keep this code easily modifiable.

# In the case that someone needs specific instructions for how to use a script or function within the code,
# please let me know if there's too much ambiguity. I can add comments to make it a bit more easier on you!

import b, c

c.onLaunch()		# Clears the console and preps OS specific settings.
b.disclaim()		# Give a disclaimer to users about the game.
b.mainMenuText()	# Title!
playingGame = True
while playingGame:
    selected = b.selection("Dialouge Demo", "-", "Options", "Quit")
    if selected == 1:
        b.testingDialogue()
    elif selected == 2:
        # Not implemented.
        None
    elif selected == 3:
        # Not implemented.
        None
    elif selected == 4:
        b.clearConsole()
        playingGame = False
        print("Thanks for playing!!!")