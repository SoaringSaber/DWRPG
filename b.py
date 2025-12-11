# Text and Menus Handling - b

import time
import os
import sys
import c, d, f

# Text and menu selection will rely on this program.

# # Text Printing # #

def p(text):
    coloring = False
    getColor = ""
    for i in text:
        if i == "`" or coloring:
            coloring = True
            if i != "`":
                getColor += i
            if i == "m":
                coloring = False
                print(getColor, end="")
        else:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(c.ts)
    
def pln(text):
    coloring = False
    getColor = ""
    for i in text:
        if i == "`" or coloring:
            coloring = True
            if i != "`":
                getColor += i
            if i == "m":
                coloring = False
                print(getColor, end="")
        else:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(c.ts)
    print()

class col:						# Add a little bit of SPICE to the text.
    white			= '`\033[97m'
    b_gray			= '`\033[38;2;153;153;153m'
    gray			= '`\033[90m'
    d_gray			= '`\033[38;2;105;105;105m'
    black			= '`\033[30m'
    white			= '`\033[37m'
    
    d_red			= '`\033[38;2;139;0;0m'
    red				= '`\033[31m'
    b_red			= '`\033[91m'
    d_orange		= '`\033[38;2;255;69;0m'
    orange			= '`\033[38;2;255;165;0m'
    brown			= '`\033[38;2;150;75;0m'
    b_orange		= '`\033[38;2;255;140;0m'
    d_yellow		= '`\033[38;2;255;215;0m'
    yellow			= '`\033[38;2;255;255;0m'
    b_yellow		= '`\033[38;2;240;230;140m'
    d_green			= '`\033[38;2;34;139;34m'
    green			= '`\033[32m'
    b_green			= '`\033[92m'
    d_blue			= '`\033[34m'
    cyan			= '`\033[36m'
    blue			= '`\033[94m'
    b_blue			= '`\033[38;2;135;206;235m'
    b_cyan			= '`\033[96m'
    d_purple		= '`\033[38;2;128;0;128m'
    purple			= '`\033[38;2;147;112;219m'
    pink			= '`\033[38;2;221;160;221m'
    
    bold			= '`\033[1m' # Doesn't function in Command Prompt.
    ul				= '`\033[4m' # Underlines text.
    inverse			= '`\033[7m' # Makes the background of the text the foreground, and vice versa.
    reset			= '`\033[0m' # Resets color and style.
    
def printAllColor():
    os.system('cls')
    pln(col.d_red + "Dark Red")
    pln(col.red + "Red")
    pln(col.b_red + "Bright Red")
    pln(col.d_orange + "Dark Orange")
    pln(col.orange + "Orange")
    pln(col.brown + "Brown")
    pln(col.b_orange + "Bright Orange")
    pln(col.d_yellow + "Dark Yellow")
    pln(col.yellow + "Yellow")
    pln(col.b_yellow + "Bright Yellow")
    pln(col.d_green + "Dark Green")
    pln(col.green + "Green")
    pln(col.b_green + "Bright Green")
    pln(col.d_blue + "Dark Blue")
    pln(col.cyan + "Cyan")
    pln(col.blue + "Blue")
    pln(col.b_blue + "Bright Blue")
    pln(col.b_cyan + "Bright Cyan")
    pln(col.d_purple + "Dark Purple")
    pln(col.purple + "Purple")
    pln(col.pink + "Pink")
    pln(col.reset + "Reset Color")
    pln("")
    pln(col.white + "White")
    pln(col.b_gray + "Bright Gray")
    pln(col.gray + "Gray")
    pln(col.d_gray + "Dark Gray")
    pln(col.black + "Black")
    pln(col.reset)

def btRemover(text):
    unBackTicked = ""
    for i in str(text):
        if i != "`":
            unBackTicked += i
    return unBackTicked

# Recently, I revamped how stats were handled, so I made this to easily get the name value. It also serves as a nice btRemover.
# In addition, I made it able to remove the color from the Toon names.
def n(var, remBT=False):
    if c.doColorNames:
        if remBT:
            return btRemover(var["name"])
        else:
            return var["name"]
    else:
        return var["name-uc"]

def pHead(text, color='\033[0m'):
    print(" ", end="")			# Print the top underscores
    for i in range(0, 19):
        print("_", end="")
    for i in text:
        print("_", end="")
    print("\n/|@ - - << ", end=btRemover(color))	# Print the beginning of header indicator.
    coloring = False
    getColor = ""
    for i in text:				# Print the text.
        if i == "`" or coloring:
            coloring = True
            if i != "`":
                getColor += i
            if i == "m":
                coloring = False
                print(getColor, end="")
        else:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(c.ts)
    print('\033[0m' + " >> - - @")		# Print the ending of header indicator.
    
def pBody(text, color='\033[0m'):
    print("|| ", end=btRemover(color))		# Print body text indicator.
    coloring = False
    getColor = ""
    for i in text:				# Print the text.
        if i == "." or i == "!" or i == "?":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(.275 + c.ts)
        elif i == ",":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(.075 + c.ts)
        elif i == "`" or coloring:
            coloring = True
            if i != "`":
                getColor += i
            if i == "m":
                coloring = False
                print(getColor, end="")
        else:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(c.ts)
    print('\033[0m')

def pAction(text, color='\033[0m'):
    print("|* ", end=btRemover(color))		# Print body text indicator.
    coloring = False
    getColor = ""
    for i in text:				# Print the text.
        if i == "." or i == "!" or i == "?":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(.275 + c.ts)
        elif i == ",":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(.075 + c.ts)
        elif i == "`" or coloring:
            coloring = True
            if i != "`":
                getColor += i
            if i == "m":
                coloring = False
                print(getColor, end="")
        else:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(c.ts)
    f.kToContinue('\033[0m')

def pDialouge(name, text, color='\033[0m'):
    print("|> [" + n(name, True) + "]: \"", end=btRemover(color))		# Print body text indicator.
    coloring = False
    getColor = ""
    for i in text:				# Print the text.
        if i == "." or i == "!" or i == "?":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(.275 + c.ts)
        elif i == ",":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(.075 + c.ts)
        elif i == "`" or coloring:
            coloring = True
            if i != "`":
                getColor += i
            if i == "m":
                coloring = False
                print(getColor, end="")
        else:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(c.ts)
    f.kToContinue("\033[0m\"")

def pAlert(text, color='\033[0m'):
    print("|< " + btRemover(color), end="")		# Print alert indicator.
    coloring = False
    getColor = ""
    for i in text:				# Print the text.
        if i == "`" or coloring:
            coloring = True
            if i != "`":
                getColor += i
            if i == "m":
                coloring = False
                print(getColor, end="")
        else:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(c.ts)
    f.kToContinue("\033[0m >")
    
def pStats(slot):				# TAKES THE STATS
    print("|{ ", end="")		# Print indicator.
    text = "It's " + slot[0] + "'s turn! - HP: " + str(slot[1]) + " - STAMINA: " + str(slot[2])
    for i in text:				# Print the text.
        if i == "." or i == "!" or i == "?":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(.275 + c.ts)
        elif i == "-":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(.075 + c.ts)
        else:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(c.ts)
    print(" }")

# # Menu Navigation # #

def inputToCont():
    f.kInput("|!")
    
def clearConsole():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/macOS
        os.system('clear')
        
def selection(*options, textSpeed=c.ts):
    count = 1
    for i in options:
        print("|" + str(count) + "). ", end="")		# Print indicator.
        pln(i)
        time.sleep(.05)
        count += 1
    invalidSelection = True
    while(invalidSelection):
        select = int(f.kNumber("", 1, count-1))
        return select

def yesOrNo(prompt):
    print("|> ", end="")
    pln(prompt)
    return selection("Yes", "No")

# # Menu Texts # #

# Startup / Main Menu #

def disclaim():
    temp = c.ts
    c.ts = 0.005
    pHead("DISCLAIMER - PLEASE READ")
    pBody("This game presents heavy topics like death, grief, and many more.")
    pBody("If you're uncomfortable with that, please stop playing. Also,")
    pBody("this game suppresses your keyboard inputs to just this program, so")
    pBody("if you need to type somewhere else, you can pause the game with P and")
    pBody("use ENTER to unpause. With all of that out of the way... ENJOY!!")
    pBody("")
    pBody("Thank you for playing the game!!!")
    pAlert("Press any key to continue.")
    c.ts = temp
    clearConsole()
    
def mainMenuText():
    pHead("Dandy's World - The Text-Based RPG")
    pBody("A game by SoaringSaber, inspired by Quelver.")
    time.sleep(.75)

# # Dev Testing # #

def testingDialogue():
    clearConsole()
    pDialouge(d.dandy, "Attention, all Toons!!")
    pDialouge(d.dandy, "We're going to be in a pretty nice GAME soon!")
    pDialouge(d.shelly, "Woah! A game?! That's so cool!")
    pDialouge(d.vee, "Eh, not too optimistic about it.")
    pDialouge(d.vee, "Probably just a weird gameshow.")
    pDialouge(d.dandy, "Oh, don't get your mic all tangled, it's none of that!")
    pDialouge(d.astro, "Then... what is it...")
    pDialouge(d.shelly, "Yeah, " + n(d.dandy) + "! Tell us!! Tell us!!")
    pDialouge(d.dandy, "It's a role-playing game!")
    pDialouge(d.vee, "So, a gameshow...")
    pDialouge(d.dandy, "No, " + n(d.vee) + ". It's not a gameshow.")
    pDialouge(d.sprout, "Okay, so it's gotta be something about roleplay..?")
    pDialouge(d.shelly, "OOOH! I can be the dinosaur!")
    pDialouge(d.dandy, "Sorry, " + n(d.shelly) + ". It's also not just roleplay.")
    pDialouge(d.dandy, "Although your roles DO matter in the long run, this game genre focuses on fighting against an enemy.")
    pDialouge(d.astro, "An enemy? Fighting?")
    pDialouge(d.dandy, "Oh! Did I say fighting? I meant befriending!!")
    pDialouge(d.shelly, "Phew, that's good.")
    pDialouge(d.astro, "But, uh... who's the enemy, here?")
    pDialouge(d.vee, "Probably just " + n(d.dandy) + ".")
    pDialouge(d.dandy, "Shut it, " + n(d.vee) + ".")
    pDialouge(d.dandy, "I don't know who this enemy even is!")
    pDialouge(d.dandy, "That's something you'll need to figure out yourself.")
    pDialouge(d.sprout, "Hmm, sounds interesting...")
    pDialouge(d.pebble, "Arf! Arf! (Maybe it'll get me a treat!)")
    pDialouge(d.sprout, "You already get a lot of treats, " + n(d.pebble) + "...")
    pDialouge(d.pebble, "Grrr...")
    pDialouge(d.dandy, "Anyways, I suspect that this game would probably come out in late 2026.")
    pDialouge(d.shelly, "WHAT?? That's going to take forever!")
    pDialouge(d.shelly, "I'd be extinct by then...")
    pDialouge(d.astro, "Don't worry, it'll definitely come soon... hopefully.")
    pDialouge(d.dandy, "Yep! We'll have so much fun!")
    pDialouge(d.dandy, "...")
    clearConsole()
    pAction("Won't we?")