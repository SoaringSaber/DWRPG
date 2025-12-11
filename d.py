# Character Manager / Statistics - d

# <Insert explanation here.>

# Stamina Values per Star:
# 50, 75, 100, 150, 200, 225

# Ability List:
# 0SP   - Intimidate - Dev Only - To Target - Lowers hit chance for target.
# 0SP   - Berserk - Dev Only - Usable Buff - Adds 3 stars to strength and skill check, at the cost of 50 HP.
# 30SP  - Rest - To Target - Regenerates STAMINA by 75% of the Toon's maximum.
# 75SP  - Catch Breath - To Team - Regenerates the Team's STAMINA fully.
# 25SP  - Bark - Usable Buff? - Lowers the Toon's Stealth by 3 stars for the turn.
# 100SP - Rush - Usable Buff - Increases Toon's speed for the next 5 turns.
# 10SP  - Encourage - To Target - Increases target's Skill Check by 2 stars for the turn.
# 50SP  - Roar - Usable Buff - Adds 3 stars to the Toon's Strength for the turn.
# 100SP - Bake - To Target - Heals a targeted Toon for 50 HP.
# 75SP  - Protect - To Target - Provides protection to the targeted toon, preventing one hit before breaking.
# 10SP  - Mic Check - To Team - Increases the Team's Skill Check by 3 stars for the turn.
# 15SP  - Disorient - To Target - Decreases targeted Toon/Twisted's Skill Check by 3 stars for 1 turn.

# Fan-Made Ability List:
# 50SP  - Rescue              - To Target         - Same affect as "Protect", protection lasts after one hit. Negates 80% damage (decreasing by 10% subsequently).
# 75SP  - Evasion UP          - Usable Buff       - Prevents lethal damage from downing the Toon. Used once per encounter.
# 0SP   - Identify            - <Not doing this one, sorry>
# 15SP  - Backslash           - To Target         - Attacks, on non-critical hit, do 75% less damage, on critical, do triple damage.
# 25SP  - Recharge            - Usable Buff       - Recover all HP.
# 50SP  - Charge Shot         - To Target         - Charges an attack, on every turn Skipped, this move does 25 more damage.
# 99SP  - Wild Magic          - <No.>
# 60SP  - The Chair           - To Target         - Deal 150 damage to target.
# 25SP  - Flash               - To Target         - Same effect as "Disorient"
# 50SP  - Continuous Action   - To Target         - Attack an opponent with an 80% (and decreasing by 5% every hit) chance to hit again. Max hits are 5.
# 25SP  - Copy Ability        - To Target         - Replaces ability with target's (randomly chosen if more than one). Wears off after encounter.
# 100SP - Abduction           - To Target         - Silence an enemy for a max of 5 turns or until the enemy rolls higher than the Toon.
# X SP  - Get Yourself a Treat- Passive Buff      - All items have 75% more effect.
# X SP  - Retake              - Passive Buff      - Upon missing for the first time in an encounter, do a critical hit.
# X SP  - Calm Under Pressure - Passive Buff      - The Toon cannot be affected by debuffs from enemies. Buffs have less of an effect.
# 50SP  - Energetic Aura      - To Team           - Heals everyone in the Team for 25 HP.
# X SP  - Energy Recovery     - Passive Team Buff - Increases STAMINA regen by 50% for the whole Team, including the Toon itself.

# Toon and Slot Stats
global s1
global s2
global s3
global s4

# s1 = [False, "PLACEHOLDER A", 0, 0, 0, 0, 0, 0, "Placeholder Ability A", "Placeholder Ability B"]
s1 = {
    "slotID": 1,
    "isActive": False,
    "name": "PLACEHOLDER A",
    "name-uc": "UNCOLORED A",
    "health": 0,
    "maxHealth": 0,
    "healthHearts": 0,
    "skill": 0,
    "skillMod": 0,
    "skillStars": 0,
    "speed": 0,
    "speedMod": 0,
    "speedStars": 0,
    "stamina": 0,
    "maxStamina": 0,
    "staminaStars": 0,
    "stealth": 0,
    "stealthMod": 0,
    "strength": 0,
    "strengthMod": 0,
    "strengthStars": 0,
    "abilities": ["Placeholder Ability A", "Placeholder Ability B"],
    "effects": [],
    "action": [],
    "attackMethod": " did something to "
    }
s2 = {
    "slotID": 2,
    "isActive": False,
    "name": "PLACEHOLDER B",
    "name-uc": "UNCOLORED B",
    "health": 0,
    "maxHealth": 0,
    "healthHearts": 0,
    "skill": 0,
    "skillMod": 0,
    "skillStars": 0,
    "speed": 0,
    "speedMod": 0,
    "speedStars": 0,
    "stamina": 0,
    "maxStamina": 0,
    "staminaStars": 0,
    "stealth": 0,
    "stealthMod": 0,
    "strength": 0,
    "strengthMod": 0,
    "strengthStars": 0,
    "abilities": ["Placeholder Ability A", "Placeholder Ability B"],
    "effects": [],
    "action": [],
    "attackMethod": " did something to "
    }
s3 = {
    "slotID": 3,
    "isActive": False,
    "name": "PLACEHOLDER C",
    "name-uc": "UNCOLORED C",
    "health": 0,
    "maxHealth": 0,
    "healthHearts": 0,
    "skill": 0,
    "skillMod": 0,
    "skillStars": 0,
    "speed": 0,
    "speedMod": 0,
    "speedStars": 0,
    "stamina": 0,
    "maxStamina": 0,
    "staminaStars": 0,
    "stealth": 0,
    "stealthMod": 0,
    "strength": 0,
    "strengthMod": 0,
    "strengthStars": 0,
    "abilities": ["Placeholder Ability A", "Placeholder Ability B"],
    "effects": [],
    "action": [],
    "attackMethod": " did something to "
    }
s4 = {
    "slotID": 4,
    "isActive": False,
    "name": "PLACEHOLDER D",
    "name-uc": "UNCOLORED D",
    "health": 0,
    "maxHealth": 0,
    "healthHearts": 0,
    "skill": 0,
    "skillMod": 0,
    "skillStars": 0,
    "speed": 0,
    "speedMod": 0,
    "speedStars": 0,
    "stamina": 0,
    "maxStamina": 0,
    "staminaStars": 0,
    "stealth": 0,
    "stealthMod": 0,
    "strength": 0,
    "strengthMod": 0,
    "strengthStars": 0,
    "abilities": ["Placeholder Ability A", "Placeholder Ability B"],
    "effects": [],
    "action": [],
    "attackMethod": " did something to "
    }
t1 = {
    "slotID": 5,
    "isActive": False,
    "type": "normal",
    "name": "TWISTED PLACEHOLDER A",
    "health": 0,
    "maxHealth": 0,
    "skill": 0,
    "skillMod": 0,
    "speed": 0,
    "speedMod": 0,
    "strength": 0,
    "strengthMod": 0,
    "damage+": 0,
    "ability": "",
    "action": [],
    "attackMethod": " did something to "
    }
t2 = {
    "slotID": 6,
    "isActive": False,
    "type": "normal",
    "name": "TWISTED PLACEHOLDER B",
    "health": 0,
    "maxHealth": 0,
    "skill": 0,
    "skillMod": 0,
    "speed": 0,
    "speedMod": 0,
    "strength": 0,
    "strengthMod": 0,
    "damage+": 0,
    "ability": "",
    "action": [],
    "attackMethod": " did something to "
    }
t3 = {
    "slotID": 7,
    "isActive": False,
    "type": "normal",
    "name": "TWISTED PLACEHOLDER C",
    "health": 0,
    "maxHealth": 0,
    "skill": 0,
    "skillMod": 0,
    "speed": 0,
    "speedMod": 0,
    "strength": 0,
    "strengthMod": 0,
    "damage+": 0,
    "ability": "",
    "action": [],
    "attackMethod": " did something to "
    }
t4 = {"slotID": 8, "isActive": False, "type": "normal", "name": "TWISTED PLACEHOLDER D", "health": 0, "maxHealth": 0, "skill": 0, "skillMod": 0, "speed": 0, "speedMod": 0, "strength": 0, "strengthMod": 0, "damage+": 0, "ability": "", "action": [], "attackMethod": " pummeled "}

chrTemp = {
        "name": "Character Template",
        "name-uc": "Uncolored Name",
        "health":    1,
        "skill":     1,
        "speed":     1,
        "stamina":   1,
        "stealth":   1,
        "strength":  1,
        "abilities": ["", ""],
        "attackMethod": " did something to "
        }

dandy = {"name": "`\033[91mD`\033[38;2;255;165;0mA`\033[38;2;255;255;0mN`\033[92mD`\033[94mY`\033[0m", "name-uc": "DANDY", "health": 4, "skill": 6, "speed": 6, "stamina": 6, "stealth": 6, "strength": 6, "abilities": ["Intimidate", "Berserk"]}
astro = {
        "name": "`\033[96mASTRO`\033[0m",
        "name-uc": "ASTRO",
        "health":    2,
        "skill":     2,
        "speed":     3,
        "stamina":   3,
        "stealth":   5,
        "strength":  3,
        "abilities": ["Rest", "Catch Breath"],
        "attackMethod": " swung at "
        }
pebble = {
        "name": "`\033[90mPEBBLE`\033[0m",
        "name-uc": "PEBBLE",
        "health":    2,
        "skill":     3,
        "speed":     5,
        "stamina":   4,
        "stealth":   3,
        "strength":  1,
        "abilities": ["Bark", "Rush"],
        "attackMethod": " tried to bite "
        }
shelly = {
        "name": "`\033[38;2;240;230;140mSHELLY`\033[0m",
        "name-uc": "SHELLY",
        "health":    2,
        "skill":     5,
        "speed":     3,
        "stamina":   2,
        "stealth":   3,
        "strength":  3,
        "abilities": ["Encourage", "Roar"],
        "attackMethod": " swung at "
        }
sprout = {
        "name": "`\033[91mSPROUT`\033[0m",
        "name-uc": "SPROUT",
        "health":    2,
        "skill":     2,
        "speed":     4,
        "stamina":   5,
        "stealth":   3,
        "strength":  2,
        "abilities": ["Bake", "Protect"],
        "attackMethod": " tried kicking "
        }
vee = {
        "name": "`\033[92mVEE`\033[0m",
        "name-uc": "VEE",
        "health":    2,
        "skill":     4,
        "speed":     2,
        "stamina":   3,
        "stealth":   2,
        "strength":  5,
        "abilities": ["Mic Check", "Disorient"],
        "attackMethod": " swung at "
        }

# Other Testers

oneStar		= ["1STAR", 1, 1, 1, 1, 1, 1, "", ""]
oneStar = {
        "name": "1STAR",
        "name-uc": "1STAR",
        "health":    1,
        "skill":     1,
        "speed":     1,
        "stamina":   1,
        "stealth":   1,
        "strength":  1,
        "abilities": ["", ""],
        "attackMethod": " pimp slapped "
        }
twoStar		= ["2STAR", 2, 2, 2, 2, 2, 2, "", ""]
twoStar = {
        "name": "2STAR",
        "name-uc": "2STAR",
        "health":    2,
        "skill":     2,
        "speed":     2,
        "stamina":   2,
        "stealth":   2,
        "strength":  2,
        "abilities": ["", ""],
        "attackMethod": " slapped "
        }
thrStar		= ["3STAR", 3, 3, 3, 3, 3, 3, "", ""]
thrStar = {
        "name": "3STAR",
        "name-uc": "3STAR",
        "health":    3,
        "skill":     3,
        "speed":     3,
        "stamina":   3,
        "stealth":   3,
        "strength":  3,
        "abilities": ["", ""],
        "attackMethod": " swung at "
        }
fouStar		= ["4STAR", 4, 4, 4, 4, 4, 4, "", ""]
fouStar = {
        "name": "4STAR",
        "name-uc": "4STAR",
        "health":    4,
        "skill":     4,
        "speed":     4,
        "stamina":   4,
        "stealth":   4,
        "strength":  4,
        "abilities": ["", ""],
        "attackMethod": " swung at "
        }
fivStar		= ["5STAR", 5, 5, 5, 5, 5, 5, "", ""]
fivStar = {
        "name": "5STAR",
        "name-uc": "5STAR",
        "health":    5,
        "skill":     5,
        "speed":     5,
        "stamina":   5,
        "stealth":   5,
        "strength":  5,
        "abilities": ["", ""],
        "attackMethod": " pummeled "
        }
sixStar		= ["6STAR", 6, 6, 6, 6, 6, 6, "", ""]
sixStar = {
        "name": "6STAR",
        "name-uc": "6STAR",
        "health":    6,
        "skill":     6,
        "speed":     6,
        "stamina":   6,
        "stealth":   6,
        "strength":  6,
        "abilities": ["", ""],
        "attackMethod": " destroyed "
        }

# Other Toons

# NOTE: Unimplemented as of now. Maybe later.
blot		= ["`\033[38;2;105;105;105mBLOT`\033[0m", 3, 1, 4, 5, 3, 2, "", ""]
boxten		= ["`\033[38;2;147;112;219mBOXTEN`\033[0m", 3, 3, 3, 3, 3, 3, "", ""]
brightney	= ["`\033[31mBRIGHTNEY`\033[0m", 3, 3, 3, 4, 1, 4, "", ""]
brusha		= ["`\033[38;2;255;215;0mBRUSHA`\033[0m", 3, 4, 3, 3, 2, 3, "", ""]
connie		= ["`\033[36mCONNIE`\033[0m", 3, 2, 1, 3, 5, 4, "", ""]
cosmo		= ["`\033[38;2;150;75;0mCOSMO`\033[0m", 3, 1, 3, 4, 4, 3, "", ""]
finn		= ["`\033[38;2;135;206;235mFINN`\033[0m", 3, 4, 3, 2, 3, 3, "", ""]
flutter		= ["`\033[38;2;221;160;221mFLUTTER`\033[0m", 3, 2, 4, 4, 3, 2, "", ""]
gigi		= ["`\033[31mGI`\033[38;2;135;206;235mGI`\033[0m", 3, 5, 3, 1, 3, 3, "", ""]
glisten		= ["`\033[38;2;240;230;140mGLISTEN`\033[0m", 3, 2, 3, 3, 2, 5, "", ""]
goob		= ["`\033[91mGO`\033[94mOB`\033[0m", 3, 3, 4, 4, 2, 2, "", ""]
looeynorm	= ["`\033[38;2;255;255;0mLOOEY`\033[0m", 3, 4, 3, 3, 2, 3, "", ""]
looey2		= [looeynorm[0], 2, 4, 4, 3, 2, 3, looeynorm[7], looeynorm[8]]
looey1		= [looeynorm[0], 1, 4, 5, 3, 2, 3, looeynorm[7], looeynorm[8]]
poppy		= ["`\033[38;2;135;206;235mPOPPY`\033[0m", 3, 3, 3, 3, 3, 3, "", ""]
razzle		= ["`\033[38;2;153;153;153mRAZZLE`\033[0m", 3, 3, 5, 3, 3, 1, "Confidence", ""]
dazzle		= ["`\033[38;2;105;105;105mDAZZLE`\033[0m", 3, 3, 1, 3, 3, 5, "Depression", ""]
razzledazzle= [razzle[0] + " `\033[31m&`\033[0m " + dazzle[0], 3, 3, 3, 3, 3, 3, razzle[7], dazzle[7]]
rodger		= ["`\033[38;2;255;165;0mRODGER`\033[0m", 3, 3, 2, 3, 3, 4, "", ""]
scraps		= ["`\033[38;2;255;215;0mSCRAPS`\033[0m", 3, 2, 2, 5, 3, 3, "", ""]
shrimpo		= ["`\033[38;2;255;69;0mSHRIMPO`\033[0m", 3, 1, 1, 1, 1, 1, "", ""]
teagan		= ["`\033[38;2;255;165;0mTEAGAN`\033[0m", 3, 3, 3, 4, 2, 3, "", ""]
tisha		= ["`\033[38;2;135;206;235mTISHA`\033[0m", 3, 4, 4, 2, 3, 2, "", ""]
toodles		= ["`\033[38;2;153;153;153mTOODLES`\033[0m", 3, 3, 3, 3, 4, 2, "", ""]
yatta		= ["`\033[38;2;255;255;0mYATTA`\033[0m", 3, 3, 4, 1, 2, 5, "", ""]

def btRemover(text):
    unBackTicked = ""
    for i in text:
        if i != "`":
            unBackTicked += i
    return unBackTicked

def printAllNames():
    print(btRemover(dandy["name"]))
    print(btRemover(astro["name"]))
    print(btRemover(pebble["name"]))
    print(btRemover(shelly["name"]))
    print(btRemover(sprout["name"]))
    print(btRemover(vee["name"]))
    print(btRemover(blot[0]))
    print(btRemover(boxten[0]))
    print(btRemover(brightney[0]))
    print(btRemover(brusha[0]))
    print(btRemover(connie[0]))
    print(btRemover(cosmo[0]))
    print(btRemover(finn[0]))
    print(btRemover(flutter[0]))
    print(btRemover(gigi[0]))
    print(btRemover(glisten[0]))
    print(btRemover(goob[0]))
    print(btRemover(looeynorm[0]))
    print(btRemover(poppy[0]))
    print(btRemover(razzledazzle[0]))
    print(btRemover(rodger[0]))
    print(btRemover(scraps[0]))
    print(btRemover(shrimpo[0]))
    print(btRemover(teagan[0]))
    print(btRemover(tisha[0]))
    print(btRemover(toodles[0]))
    print(btRemover(yatta[0]))
    
def printActiveSlots():
    for i in range(4):
        if i+1 == 1:
            toPrint = s1
        elif i+1 == 2:
            toPrint = s2
        elif i+1 == 3:
            toPrint = s3
        elif i+1 == 4:
            toPrint = s4
        if toPrint["isActive"]:
            print("Name: " + btRemover(toPrint["name"]))
            print("Health: " + str(toPrint["health"]) + "/" + str(toPrint["maxHealth"]))
            print("Stamina: " + str(toPrint["stamina"]) + "/" + str(toPrint["maxStamina"]))
            print("Skill Check: " + str(toPrint["skill"]) + " - Mod: " + str(toPrint["skillMod"]))
            print("Movement Speed: " + str(toPrint["speed"]) + " - Mod: " + str(toPrint["speedMod"]))
            print("Stealth: " + str(toPrint["stealth"]) + " - Mod: " + str(toPrint["stealthMod"]))
            print("Strength: " + str(toPrint["strength"]) + " - Mod: " + str(toPrint["strengthMod"]))
            print("Ability A: " + toPrint["abilities"][0])
            print("Ability B: " + toPrint["abilities"][1])
            print("Status Effects: " + str(toPrint["effects"]))
            print("")
    for i in range(4):
        if i+1 == 1:
            toPrint = t1
        elif i+1 == 2:
            toPrint = t2
        elif i+1 == 3:
            toPrint = t3
        elif i+1 == 4:
            toPrint = t4
        if toPrint["isActive"]:
            print("Name: " + btRemover(toPrint["name"]) + " - Type: " + toPrint["type"])
            print("Health: " + str(toPrint["health"]) + "/" + str(toPrint["maxHealth"]))
            print("Skill Check: " + str(toPrint["skill"]) + " - Mod: " + str(toPrint["skillMod"]))
            print("Movement Speed: " + str(toPrint["speed"]) + " - Mod: " + str(toPrint["speedMod"]))
            print("Strength: " + str(toPrint["strength"]) + " - Mod: " + str(toPrint["strengthMod"]))
            print("Damage+: " + str(toPrint["damage+"]))
            print("Ability: " + toPrint["ability"])
            print("")

def updateSlotStats(fromOG, toNum, isActive=False):
    
    name = fromOG["name"]
    name_uc = fromOG["name-uc"]
    health = 0
    if fromOG["health"] == 1:
        health = 50
    elif fromOG["health"] == 2:
        health = 100
    elif fromOG["health"] == 3:
        health = 150
    elif fromOG["health"] == 4:
        health = 200
    elif fromOG["health"] == 5:
        health = 250
    else:
        None
        
    stamina = 0
    if fromOG["stamina"] == 1:
        stamina = 50
    elif fromOG["stamina"] == 2:
        stamina = 75
    elif fromOG["stamina"] == 3:
        stamina = 100
    elif fromOG["stamina"] == 4:
        stamina = 150
    elif fromOG["stamina"] == 5:
        stamina = 200
    elif fromOG["stamina"] == 6:
        stamina = 225
    else:
        None
    
    speed = fromOG["speed"]
    stealth = fromOG["stealth"]
    
    strength = 0
    # Maximum damage that a Toon can do.
    if fromOG["strength"] == 1:
        strength = 30
    elif fromOG["strength"] == 2:
        strength = 40
    elif fromOG["strength"] == 3:
        strength = 50
    elif fromOG["strength"] == 4:
        strength = 65
    elif fromOG["strength"] == 5:
        strength = 75
    elif fromOG["strength"] == 6:
        strength = 100
    else:
        None
    
    hitChance = 0
    # Rolls would need to be above this value to get a hit, lower is better!!
    if fromOG["skill"] == 1:
        hitChance = 80
    elif fromOG["skill"] == 2:
        hitChance = 60
    elif fromOG["skill"] == 3:
        hitChance = 40
    elif fromOG["skill"] == 4:
        hitChance = 20
    elif fromOG["skill"] == 5:
        hitChance = 5
    elif fromOG["skill"] == 6:
        hitChance = 1
    else:
        None
    
    stats = {
        "slotID":        toNum,
        "isActive":      isActive,
        "name":          name,
        "name-uc":       name_uc,
        "health":        health,
        "maxHealth":     health,
        "healthHearts":  fromOG["health"],
        "skill":         hitChance,
        "skillMod":      0,
        "skillStars":    fromOG["skill"],
        "speed":         speed,
        "speedMod":      0,
        "speedStars":    fromOG["speed"],
        "stamina":       stamina,
        "maxStamina":    stamina,
        "staminaStars":  fromOG["stamina"],
        "stealth":       stealth,
        "stealthMod":    0,
        "strength":      strength,
        "strengthMod":   0,
        "strengthStars": fromOG["strength"],
        "abilities": [fromOG["abilities"][0], fromOG["abilities"][1]],
        "effects": [],
        "attackMethod": fromOG["attackMethod"]
        }
    if toNum == 1:
        global s1
        s1 = stats
    elif toNum == 2:
        global s2
        s2 = stats
    elif toNum == 3:
        global s3
        s3 = stats
    elif toNum == 4:
        global s4
        s4 = stats
        
def convertToTwisted(fromOG, toNum, isActive=False):
    if fromOG["name-uc"] == "DANDY":
        stats = {
            "slotID": toNum+4,
            "isActive": isActive,
            "type": "main",
            "name": "`\033[31mTWISTED`\033[0m `\033[91mD`\033[38;5;166mA`\033[93mN`\033[92mD`\033[94mY`\033[0m",
            "health": 850,
            "maxHealth": 850,
            "skill": 50,
            "skillMod": 0,
            "speed": 8,
            "speedMod": 0,
            "strength": 250,
            "strengthMod": 0,
            "damage+": 0,
            "ability": "Fear",
            "attackMethod": " obliterated "
            }
    elif fromOG["name-uc"] == "ASTRO":
        stats = {
            "slotID": toNum+4,
            "isActive": isActive,
            "type": "main",
            "name": "`\033[31mTWISTED`\033[0m `\033[36mASTRO`\033[0m",
            "health": 400,
            "maxHealth": 400,
            "skill": 40,
            "skillMod": 0,
            "speed": 4.5,
            "speedMod": 0,
            "strength": 120,
            "strengthMod": 0,
            "damage+": 0,
            "ability": "Lullaby",
            "attackMethod": " tried forcing \"sleep\" on "
            }
    else:
        # For normal Toons turning into Twisteds.
        health = 0
        if fromOG["health"] == 1:
            health = 125
        elif fromOG["health"] == 2:
            health = 150
        elif fromOG["health"] == 3:
            health = 200
        elif fromOG["health"] == 4:
            health = 250
        else:
            None
        strength = 0
        if fromOG["strength"] == 1:
            strength = 40
        elif fromOG["strength"] == 2:
            strength = 40
        elif fromOG["strength"] == 3:
            strength = 45
        elif fromOG["strength"] == 4:
            strength = 60
        elif fromOG["strength"] == 5:
            strength = 75
        elif fromOG["strength"] == 6:
            strength = 120
        else:
            None
        stats = {
            "slotID": toNum+4,
            "isActive": isActive,
            "type": "normal",
            "name": "`\033[31mTWISTED`\033[0m " + fromOG["name"],
            "health": health,
            "maxHealth": health,
            "skill": 45,
            "skillMod": 0,
            "speed": fromOG["speed"] + .5,
            "speedMod": 0,
            "strength": strength,
            "strengthMod": 0,
            "damage+": 0,
            "ability": "",
            "attackMethod": " swiped at "
            }
    if toNum == 1:
        global t1
        t1 = stats
    elif toNum == 2:
        global t2
        t2 = stats
    elif toNum == 3:
        global t3
        t3 = stats
    elif toNum == 4:
        global t4
        t4 = stats