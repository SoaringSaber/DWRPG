# Battle System - g

import b, d
import random

def identSlot(fromNum):
    if fromNum == 1:
        return d.s1
    elif fromNum == 2:
        return d.s2
    elif fromNum == 3:
        return d.s3
    elif fromNum == 4:
        return d.s4
    elif fromNum == 5:
        return d.t1
    elif fromNum == 6:
        return d.t2
    elif fromNum == 7:
        return d.t3
    elif fromNum == 8:
        return d.t4

def updateTurnOrder():
    global sortedSlotsSpeed
    slots = [{"slot": d.s1, "value": d.s1["speed"] + d.s1["speedMod"]}, {"slot": d.s2, "value": d.s2["speed"] + d.s2["speedMod"]}, {"slot": d.s3, "value": d.s3["speed"] + d.s3["speedMod"]}, {"slot": d.s4, "value": d.s4["speed"] + d.s4["speedMod"]}, {"slot": d.t1, "value": d.t1["speed"] + d.t1["speedMod"]}, {"slot": d.t2, "value": d.t2["speed"] + d.t2["speedMod"]}, {"slot": d.t3, "value": d.t3["speed"] + d.t3["speedMod"]}, {"slot": d.t4, "value": d.t4["speed"] + d.t4["speedMod"]}]
    sortedSlotsSpeed = sorted(slots, key=lambda item: item["value"], reverse=True)
    # print(sortedSlotsSpeed)
    
def updateStealth():
    global sortedSlotsStealth
    slots = [{"slot": d.s1, "value": d.s1["stealth"] + d.s1["stealthMod"]}, {"slot": d.s2, "value": d.s2["stealth"] + d.s2["stealthMod"]}, {"slot": d.s3, "value": d.s3["stealth"] + d.s3["stealthMod"]}, {"slot": d.s4, "value": d.s4["stealth"] + d.s4["stealthMod"]}]
    sortedSlotsStealth = sorted(slots, key=lambda item: item["value"], reverse=False)
    # print(sortedSlotsStealth)

def checkIfDead(checking):
    if slotAttacked["health"] <= 0:
        print(b.n(checking) + " was downed.")

def calcDamage(slotAttacker, slotAttacked, guarunteedHit=False):
    strength = slotAttacker["strength"]
    hitChance = slotAttacker["skill"]
    roll = random.randint(1, 100)
    print("Roll: " + str(roll) + "/" + str(hitChance))
    if roll > int(hitChance) or guarunteedHit:
        print("it hit " + b.btRemover(slotAttacked["name"]))
        damage = strength * (roll / 100)
        # if it's a twisted, include the modifier for extra damage
        print("Damage: " + str(round(damage)))
        # slotAttacked["health"] = slotAttacked["health"] - damage
        # checkIfDead(slotAttacked)
    else:
        print("it missed")
        # nothing happens, loser.

def testDmg(slot, guaruntee=False):
    d.updateSlotStats(slot, 1, True)
    calcDamage(d.s1, d.oneStar, guaruntee)
    calcDamage(d.s1, d.oneStar, guaruntee)
    calcDamage(d.s1, d.oneStar, guaruntee)
    calcDamage(d.s1, d.oneStar, guaruntee)

# Player actions are defined here.
def doAction(slot, action):
    if action[0] == -2:
        print(b.btRemover(slot["name"]) + " skipped their turn.")
    elif action[0] == 0:
        print(b.btRemover(slot["name"]) + " did something to " + b.btRemover(identSlot(action[1])["name"]))
        calcDamage(slot, identSlot(action[1]))
    elif action[0] == 1:
        print(b.btRemover(slot["name"]) + slot["attackMethod"] + b.btRemover(identSlot(action[1])["name"]))
        calcDamage(slot, identSlot(action[1]))

def determineAttackTarget():
    global sortedSlotsStealth
    roll = random.randint(1, 100)
    if roll <= 75:
        if roll < 38:
            target = sortedSlotsStealth[0]
            return target["slot"]
        else:
            target = sortedSlotsStealth[1]
            return target["slot"]
    else:
        if roll < 90:
            target = sortedSlotsStealth[2]
            return target["slot"]
        else:
            target = sortedSlotsStealth[3]
            return target["slot"]

# yaaay algorithm
def doTwistedAction(slot):
    global sortedSlotsStealth
    # print("AI SUCKS, EMBRACE ALGORITHM")
    determinedAction = 0
    if determinedAction == 0:
        targeted = determineAttackTarget()
        print(b.btRemover(slot["name"]) + " did something to " + b.n(targeted, True))
        calcDamage(slot, targeted)
    elif determinedAction == 1:
        targeted = determineAttackTarget()
        print(b.btRemover(slot["name"]) + " swung at " + b.n(targeted, True))
        calcDamage(slot, targeted)

# Player and Twisted actions are called in turn order.
def commitToActions():
    global sortedSlotsSpeed
    for i in range(8):
        turn = sortedSlotsSpeed[i]										# Go through the sorted speed.
        if turn["slot"]["isActive"]:									# Check if the slot is even active, usually meant for not full parties/enemy combos.
            if not turn["slot"]["slotID"] > 4:							# Check if the slot is not a Twisted.
                doAction(turn["slot"], turn["slot"]["action"])			# Do the player action done in "cycleThroughSlots".
            else:
                doTwistedAction(turn["slot"])							# Run the algorithm for Twisted behavior.

def printSlotStatus(slot):
    print("|-------------------------------------")
    print("|> " + b.btRemover(slot["name"]) + " - HP: " + str(slot["health"]) + "/" + str(slot["maxHealth"]) + " - STAMINA: " + str(slot["stamina"]) + "/" + str(slot["maxStamina"]))

# List of actions to take
#
#-2 - Skip Turn
#-1 - Back in Menus
# 0 - Something
# 1 - Fight
# 2 - Ability A
# 3 - Ability B
# 4 - Retreat

def chooseTwistedTarget(actionNum):
    targetting = True
    while targetting:
        
        # target = b.selection(d.t1["name"], d.t2["name"], d.t3["name"], d.t4["name"], "Back")
        if target == 1:
            print(d.t1["isActive"])
            if d.t1["isActive"]:
                move = [actionNum, 5]
                targetting = False
        elif target == 2:
            if d.t2["isActive"]:
                move = [actionNum, 6]
                targetting = False
        elif target == 3:
            if d.t3["isActive"]:
                move = [actionNum, 7]
                targetting = False
        elif target == 4:
            if d.t4["isActive"]:
                move = [actionNum, 8]
                targetting = False
        elif target == 5:
            move = [-1, "none"]
        return move

def cycleThroughSlots():
    # Bad code, redoing this with a while loop.
    if d.s1["isActive"]:
        b.pln("It's " + b.n(d.s1) + "'s turn!")
        choosingAction = True
        while choosingAction:
            printSlotStatus(d.s1)
            decision = b.selection("Attack", "Ability", "Run", "Skip")
            if decision == 1:
                b.pln(" - Attack who?")
                d.s1["action"] = chooseTwistedTarget(1)
                if d.s1["action"][0] != -1:
                    choosingAction = False
            if decision == 2:
                None
            if decision == 3:
                None
            if decision == 4:
                s1["action"] = [-2, ""]
                choosingAction = False
            b.clearConsole()
    if d.s2["isActive"]:
        b.pln("It's " + b.n(d.s2) + "'s turn!")
        choosingAction = True
        while choosingAction:
            printSlotStatus(d.s2)
            decision = b.selection("Attack", "Ability", "Run", "Skip")
            if decision == 1:
                b.pln("Attack who?")
                d.s2["action"] = chooseTwistedTarget(0)
                if d.s2["action"][0] != -1:
                    choosingAction = False
            if decision == 2:
                None
            if decision == 3:
                None
            if decision == 4:
                d.s2["action"] = [-2, ""]
                choosingAction = False
            b.clearConsole()
    if d.s3["isActive"]:
        b.pln("It's " + b.n(d.s3) + "'s turn!")
        choosingAction = True
        while choosingAction:
            printSlotStatus(d.s3)
            decision = b.selection("Attack", "Ability", "Run", "Skip")
            if decision == 1:
                b.pln("Attack who?")
                d.s3["action"] = chooseTwistedTarget(0)
                if d.s3["action"][0] != -1:
                    choosingAction = False
            if decision == 2:
                None
            if decision == 3:
                None
            if decision == 4:
                d.s3["action"] = [-2, ""]
                choosingAction = False
            b.clearConsole()
    if d.s4["isActive"]:
        b.pln("It's " + b.n(d.s4) + "'s turn!")
        choosingAction = True
        while choosingAction:
            printSlotStatus(d.s4)
            decision = b.selection("Attack", "Ability", "Run", "Skip")
            if decision == 1:
                b.pln("Attack who?")
                d.s4["action"] = chooseTwistedTarget(0)
                if d.s4["action"] != -1:
                    choosingAction = False
            if decision == 2:
                None
            if decision == 3:
                None
            if decision == 4:
                d.s4["action"] = [-2, ""]
                choosingAction = False
            b.clearConsole()

def testFight():
    d.updateSlotStats(d.cayde, 1, True)
    d.updateSlotStats(d.dexter, 2, True)
    d.updateSlotStats(d.strawbi, 3, True)
    d.updateSlotStats(d.mimosa, 4, True)
    d.convertToTwisted(d.drBlayde, 1, True)
    d.convertToTwisted(d.delila, 2, True)
    d.convertToTwisted(d.tixie, 3, True)
    d.convertToTwisted(d.mareelyn, 4, True)
    battleLoop = True
    #if enemyStats[0] == "normal":
    #    b.pAlert("An enemy approaches!")
    #elif enemyStats[0] == "special":
    #    b.pAlert("A special enemy approaches!")
    #else:
    #    b.pAlert("A MAIN TWISTED IS APPROACHING!!")
    # b.clearConsole()
    # print(" _______________________________________________")
    # print("/|@ - - << ! ! >> It's a battle! << ! ! >> - - @")
    # d.printActiveSlots()
    while battleLoop:
        cycleThroughSlots()
        updateTurnOrder()
        updateStealth()
        commitToActions()

def simulateDmg():
    testDmg(d.oneStar)
    print()
    testDmg(d.twoStar)
    print()
    testDmg(d.thrStar)
    print()
    testDmg(d.fouStar)
    print()
    testDmg(d.fivStar)
    print()
    testDmg(d.sixStar)