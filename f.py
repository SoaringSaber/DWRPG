# Keyboard Input Handling - f

from pynput import keyboard
import time

listener = None
readKey = ""

def getKey(key):
    try:
        global readKey
        global keyType
        readKey = key
        time.sleep(.025)
        readKey = str(readKey.char)
        keyType = "char"
        return False
    except AttributeError:
        readKey = key
        keyType = "special"
        return False
    
def startListener():
    global listener
    with keyboard.Listener(on_press=getKey, suppress=True) as keyGetter:
        keyGetter.join()

def k():
    global readKey
    reading = True
    while reading:
        startListener()
        if keyType == "char":
            if readKey == "p":
                input("|! Pausing kb suppression... press ENTER to continue.")
                return ""
            else:
                return readKey
        else:
            return readKey

def kMove():
    global readKey
    global keyType
    gettingKey = True
    while(gettingKey):
        startListener()
        if keyType == "special":
            readKey = str(readKey)
            if readKey == "Key.up" or readKey == "Key.down" or readKey == "Key.left" or readKey == "Key.right":
                return str(readKey)
        elif keyType == "char":
            if readKey == "z" or readKey == "x":
                return readKey
            elif readKey == "p":
                input("|! Pausing kb suppression... press ENTER to continue.")
                return "p"

def kToContinue(text):
    print(text)
    k()
    
def kNumber(text, rangeMin, rangeMax):
    if text != "":
        print(text)
    global readKey
    global keyType
    gettingNum = True
    while(gettingNum):
        startListener()
        if keyType == "char":
            try:
                num = int(readKey)
                if num >= rangeMin and num <= rangeMax:
                    return num
            except:
                pass

# print(kMove() + " pressed!!")
# kToContinue("HUHHHH")
# print(kNumber("GIVE ME A NUMBERRRRRRRRRR", 3, 5))