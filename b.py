# Text and Menus Handling - b

import time
import os
import sys
import d, f

# Text and menu selection will rely on this program.
# 

# # Text Printing # #
    
def p(text):
    for i in text:
        sys.stdout.write(i)
        time.sleep(0.025)
        sys.stdout.flush()
    
def pln(text):
    for i in text:
        sys.stdout.write(i)
        time.sleep(0.025)
        sys.stdout.flush()
    print()
    
def pHead(text):
    print(" ", end="")			# Print the top underscores
    for i in range(0, 19):
        print("_", end="")
    for i in text:
        print("_", end="")
    print("\n/|@ - - << ", end="")	# Print the beginning of header indicator.
    for i in text:				# Print the text.
        sys.stdout.write(i)
        time.sleep(0.025)
        sys.stdout.flush()
    print(" >> - - @")		# Print the ending of header indicator.
    
def pBody(text):
    print("|| ", end="")		# Print body text indicator.
    for i in text:				# Print the text.
        if i == "." or i == "!" or i == "?":
            sys.stdout.write(i)
            time.sleep(.275 + 0.025)
            sys.stdout.flush()
        elif i == ",":
            sys.stdout.write(i)
            time.sleep(.075 + 0.025)
            sys.stdout.flush()
        else:
            sys.stdout.write(i)
            time.sleep(0.025)
            sys.stdout.flush()
    print()

def pAction(text):
    print("|* ", end="")		# Print body text indicator.
    for i in text:				# Print the text.
        if i == "." or i == "!" or i == "?":
            sys.stdout.write(i)
            time.sleep(.275 + 0.025)
            sys.stdout.flush()
        elif i == ",":
            sys.stdout.write(i)
            time.sleep(.075 + 0.025)
            sys.stdout.flush()
        else:
            sys.stdout.write(i)
            time.sleep(0.025)
            sys.stdout.flush()
    f.kToContinue("")

def pDialouge(name, text):
    print("|> [" + name + "]: \"", end="")		# Print body text indicator.
    for i in text:				# Print the text.
        if i == "." or i == "!" or i == "?":
            sys.stdout.write(i)
            time.sleep(.275 + 0.025)
            sys.stdout.flush()
        elif i == ",":
            sys.stdout.write(i)
            time.sleep(.075 + 0.025)
            sys.stdout.flush()
        else:
            sys.stdout.write(i)
            time.sleep(0.025)
            sys.stdout.flush()
    f.kToContinue("\"")

def pAlert(text):
    print("|< ", end="")		# Print alert indicator.
    for i in text:				# Print the text.
        sys.stdout.write(i)
        time.sleep(0.025)
        sys.stdout.flush()
    f.kToContinue(" >")
    
def pStats(slot):				# TAKES THE STATS
    print("|{ ", end="")		# Print indicator.
    text = "It's " + slot[0] + "'s turn! - HP: " + str(slot[1]) + " - STAMINA: " + str(slot[2])
    for i in text:				# Print the text.
        if i == "." or i == "!" or i == "?":
            sys.stdout.write(i)
            time.sleep(.275 + 0.025)
            sys.stdout.flush()
        elif i == "-":
            sys.stdout.write(i)
            time.sleep(.075 + 0.025)
            sys.stdout.flush()
        else:
            sys.stdout.write(i)
            time.sleep(0.025)
            sys.stdout.flush()
    print(" }")

# # Menu Navigation # #

def inputToCont():
    f.kInput("|!")
    
def clearConsole():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/macOS
        os.system('clear')
        
def selection(*options):
    count = 1
    for i in options:
        print("|" + str(count) + "). ", end="")		# Print indicator.
        for x in i:
            sys.stdout.write(x)
            time.sleep(0.025)
            sys.stdout.flush()
        print()
        count += 1
    invalidSelection = True
    while(invalidSelection):
        try:
            select = int(f.kNumber("||> ", 1, count-1))
        except:
            select = -1
        finally:
            if select <= 0:
                pln("|< Invalid input, try again. >")
            elif select > count-1:
                pln("|< Invalid input, try again. >")
            else:
                return select

# # Menu Texts # #

# Startup / Main Menu #

def disclaim():
    pHead("DISCLAIMER - PLEASE READ")
    pBody("This game suppresses your keyboard inputs to just this program, so")
    pBody("if you need to type somewhere else, you can STOP the program by closing it.")
    pBody("Alternatively, when viewing the map, you can press \'P\'.")
    time.sleep(1.5)
    pAlert("Press any key to continue.")
    clearConsole()
    
def mainMenuText():
    pHead("Dandy's World - The Text-Based RPG")
    pBody("Public Testing 0.5 - Have fun!")
    time.sleep(1)

# # Dialouge # #

def demo():
    clearConsole()
    pDialouge("SOARING", "Hello! This is a quick demo of the dialogue in my game!")
    pAction("\"Aw man, why's this a DEMO??\" you think to yourself...")
    pDialouge("SOARING", "Well, I don't want to spoil the tutorial build when I finish that!")
    pDialouge("SOARING", "It'd spoil all the fun!")
    pAction("Ah, that makes sense...")
    pDialouge("SOARING", "By the way, how are you liking the cool text?")
    pDialouge("SOARING", "Y'know, how it types itself out, and pauses at the periods..?")
    pDialouge("SOARING", "I'm proud of that. But you should also go check out the map, too!")
    pDialouge("SOARING", "Sadly, I had to just give you an unfinished version of the tutorial lobby.")
    pAction("BOOO! Unfinished things are such a bore!!")
    pDialouge("SOARING", "But I gave you noclip, so you can go out of bounds!")
    pDialouge("SOARING", "Just tap \'X\' to toggle it, you don't start with it.")
    pAction("Still lame, give me something great...")
    pDialouge("SOARING", "But, uhh... YEAH!")
    pDialouge("SOARING", "I'm working on a version two of the lobby, which may or may not serve as a menu or something.")
    pDialouge("SOARING", "Isn't that cool?")
    pAction("I guess so.")
    pDialouge("SOARING", "Anyways, this is the very early development of cool game that will probably never get popular.")
    pDialouge("SOARING", "But at least I had some fun! I can also put this on my resume muehehehe...")
    pDialouge("SOARING", "Thanks for trying this out!")
    clearConsole()

# # Dev Testing # #

def testingDialouge():
    pHead("Testing Menu - Dev Only")
    #pBody("Testing cause this is cool, ya know!")
    #pAction("This is an example of an actual sentence, one that, of course, will be spoken.")
    #pBody("..! .,a..,,aa...,,,aaa !!! ???")
    #pDialouge(d.dandy[0], "Hey, buddy... are you there, " + d.astro[0] + "?")
    #pAlert("You CAN interact with this alert! Press ENTER!! Press it!!!")
    #pBody("Thanks, pookie.")
    time.sleep(.5)
    d.s1 = d.updateSlotStats(1, d.dandy)
    pStats(d.s1)
    select = selection("Attack", "Defend", "Skip")
# testingDialouge()

def testingKeyboard():
    pAction("Test!")
# testingKeyboard()