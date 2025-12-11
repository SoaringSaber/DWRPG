# Keyboard Input Handling - f

from pynput import keyboard
import os
import time

listener = None
readKey = ""

def getKey(key):
    try:
        global readKey
        readKey = key
        time.sleep(.1)
        return False
    except AttributeError:
        pass
    
def startListener():
    global listener
    with keyboard.Listener(on_press=getKey, suppress=True) as keyGetter:
        keyGetter.join()

def k():
    global readKey
    startListener()
    return readKey

def kMove():
    global readKey
    gettingKey = True
    while(gettingKey):
        startListener()
        try:
            moveKey = str(readKey)
            if moveKey == "Key.up" or moveKey == "Key.down" or moveKey == "Key.left" or moveKey == "Key.right":
                return moveKey
            interactKey = readKey.char
            if interactKey == "p" or interactKey == "z" or interactKey == "x":
                return interactKey
        except:
            pass
    return readKey

def kToContinue(text):
    print(text)
    k()
    
def kNumber(text, rangeMin, rangeMax):
    print(text)
    global readKey
    gettingKey = True
    while(gettingKey):
        startListener()
        try:        
            int(readKey.char) + int(readKey.char)	# intentionally try to cause an error here muehehe
            global numKey
            numKey = int(readKey.char)
            if numKey < rangeMin:
                None
            elif numKey > rangeMax:
                None
            else:
                return numKey
        except AttributeError:
            pass
        except ValueError:
            pass

# print(kMove() + " pressed!!")
# kToContinue("HUHHHH")
# print(kNumber("GIVE ME A NUMBERRRRRRRRRR", 3, 5))