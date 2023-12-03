#IMPORT MODULES
import os
import random

#SETUP CLASSES
class Player:
    def __init__(self):
        self.lives = 1
        self.maxLives = 1
        self.inventory = []
        self.str = 0
        self.gold = 0
        self.cls = ""
        
class Area:
    def __init__(self, name, desc = ""):
        self.name = name
        self.desc = desc
        self.entities = []
        self.items = []
        self.borderAreas = []     
  
class Entity:
    def __init__(self, name, str, gold = 0):
        self.name = name
        self.str = str
        self.gold = gold
        
class Item:
    def __init__(self, name, desc = "", str = 0):
        self.name = name
        self.desc = desc
        self.str = str
 

#SETUP FUNCTIONS
def createBorderAreas(areas):
    cur = 0
    
    for area in areas:
        if cur == 0: 
            before = len(areas) - 1
        else:
            before = cur - 1
            
        if cur == len(areas) - 1: 
            after = 0
        else:
            after = cur + 1
            
        area.borderAreas.append(areas[before])
        area.borderAreas.append(areas[after])

        cur += 1
       

def travel(curArea):
    listBorderAreas(curArea)
    areaList = curArea.borderAreas
    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        clear()
        print(f"You have stayed in {curArea.name}.")
        return curArea
    
    try:
        newArea = areaList[int(choice)-2]
    except:
        clear()
        print("Invalid input. Please try again. \n")
        return travel(curArea)
    else:
        clear()
        print(f"You have travelled from {curArea.name} to {newArea.name}.")
        return newArea
        
    
def listBorderAreas(area):
    areaList = area.borderAreas  
    print(f"1 - Remain in {area.name}")
    i = 2
    for area in areaList:
        print(f"{i} - Travel to {area.name}")
        i += 1
        

def chooseMonster(area, player):
    monsters = area.entities
    i = 2
    print("Monsters to fight:")
    print("1 - Cancel fight")
    for monster in monsters:
        print(f"{i} - {monster.name}: Has {monster.str} Strength, Carrying {monster.gold} Gold Coins")
        
    choice = input("\nEnter your choice: ")
    
    if choice == "1": return
    try:
        monsters[int(choice)-2]
    except:
        clear()
        print("Invalid input. Please try again. \n")
        return chooseMonster(area, player)
    else: 
        clear()
        fight(area, player, monsters[int(choice)-2])
        return

def clear():
    os.system('cls||clear')


def mainChoice(choices):
    i = 1
    for c in choices:
        print(f"{i} - {c}")
        i += 1

    choice = input("\nEnter your choice: ")
    try:
        choices[int(choice)-1]
    except:
        clear()
        print("Invalid input. Please try again. \n")
        return mainChoice(choices)
    else:
        return choices[int(choice)-1]
    

def fight(area, player, monster):
    playerDice = random.randint(1, 6)
    monsterDice = random.randint(1, 6)
    playerFinalStr = player.str + playerDice
    monsterFinalStr = monster.str + monsterDice

    print(f"Your strength is {player.str}, and you rolled a {playerDice}. Your final strength is therefore {playerFinalStr}.")
    print(f"The {monster.name}'s strength is {monster.str}, and it rolled a {monsterDice}. Its final strength is therefore {monsterFinalStr}.")

    if playerFinalStr > monsterFinalStr:
        area.entities.remove(monster)
        print(f"\nYou defeated the {monster.name}!")
        player.gold += monster.gold
        print(f"You got {monster.gold} gold coins from the monster. You now have {player.gold} gold coins.")
        return
    
    if monsterFinalStr > playerFinalStr:
        player.lives += -1
        print(f"\nThe {monster.name} overpowered you! You have {player.lives} lives remaining.")
        return
    
    print(f"\nYou and the {monster.name} bought each other to a draw.")


def viewStats(player):
    print(f"Class: {player.cls}\n")
    print(f"Lives remaining: {player.lives}")
    print(f"Strength: {player.str}")
    print(f"Gold coins: {player.gold}")
    
    if len(player.inventory) == 0:
        print("Inventory: Empty")
        return

    print("\nInventory:")
    for item in player.inventory:
        print(f"{item.name}: {item.desc}")
        return
   

def chooseClass(player):
    print("Pick one of the following classes:")
    print("1 - Beserk:  3 Lives, 5 Strength, 1 Gold Coin")
    print("2 - Tank:    5 Lives, 3 Strength, 1 Gold Coin")
    print("3 - Trader:  3 Lives, 3 Strength, 4 Gold Coins")
    print("4 - Wizard:  2 Lives, 2 Strength, 2 Gold Coins")
    
    choice = input("\nEnter your choice: ")
    
    if not choice in ["1", "2", "3", "4"]:
        clear()
        print("Invalid input. Please try again.\n")
        return chooseClass(player)

    if choice == "1":
        player.lives = 3
        player.str = 5
        player.gold = 1
        player.cls = "Berserk"

    if choice == "2":
        player.lives = 5
        player.str = 3
        player.gold = 1
        player.cls = "Tank"

    if choice == "3":
        player.lives = 3
        player.str = 3
        player.gold = 4
        player.cls = "Trader"

    if choice == "4":
        player.lives = 2
        player.str = 2
        player.gold = 2
        player.cls = "Wizard"
   
    player.maxLives = player.lives
    clear()


def shop(area, player):
    return


def mystic(player):
    return
        
def obeliskInspect(player):
    if player.cls == "Wizard":
        print("You walk up to the obelisk and see an inscribed message:")
        print("Place a gold coin on thee, and magic powers you will see...")
        return
    
    print("You walk up to the obelisk and see an inscribed message:")
    print("!¡ꖎᔑᓵᒷ ᔑ ⊣𝙹ꖎ↸ coin 𝙹リ thee, ᔑリ↸ ᒲᔑ⊣╎ᓵ powers ||𝙹⚍ ∴╎ꖎꖎ ᓭᒷᒷ")

def main(player):
    #CREATE AREAS
    forest =    Area("The Forest", "a large, luscious forest with many trees all around you")
    plainsW =   Area("The Western Grassland", "a stretch of flat, grass-filled land")
    village =   Area("The Village", "a small, medieval village, dotted with rickety houses")
    savanna =   Area("The Savanna", "a stretch of warm grassland, with a few trees dotted around")
    desert =    Area("The Desert", "a hot, dry and empty stretch of sand")
    mountain =  Area("The Great Mountain", "a large mountain, with steep, rocky sides")
    hut =       Area("The Mountain Hut", "a small hut situated on a flat area of the mounatin")
    hillsNW =   Area("The Northern Hills", "a stretch of hilly grassland")
    plainsN =   Area("The Northern Grassland", "a stretch of flat, grass-filled land")
    desertN =   Area("The Frozen Desert", "a large, deserted area, filled with snow and ice")
    hillsNE =   Area("Some Hills", "a stretch of hilly grassland")
    valleyN =   Area("The Valley", "an area surrounded by many hills")
    pond =      Area("The Pond", "a small pond, home to a few ducks")
    valleyE =   Area("The Valley", "an area surrounded by many hills")
    ruins =     Area("The Ruins", "the remnants of a great castle that stood here almost a thousand years ago")
    plainsE =   Area("The Eastern Grassland", "a stretch of flat, grass-filled land")
    graves =    Area("The Graveyard", "a fenced-off area, with the graves of many dead souls")
    church =    Area("The Church", "a secluded and eerily empty church")
    cityE =     Area("The East Side of The City", "an old city, once home to many, but now barely populated")
    cityW =     Area("The West Side of The City", "an old city, once home to many, but now barely populated")
    hillsS =    Area("The Southern Hills", "a stretch of hilly grassland")
    valleyS =   Area("The Southern Valley", "an area surrounded by many hills")
    lake =      Area("The Lake", "a great, deep-blue lake")
    obelisk =   Area("The Obelisk", "a large stone obelisk, surrounded with mist")
    
    createBorderAreas([forest, plainsW, village, savanna, desert, mountain, hut, hillsNW, plainsN, desertN, hillsNE, valleyN, 
                       pond, valleyE, ruins, plainsE, graves, church, cityE, cityW, hillsS, valleyS, lake, obelisk])

    eeriePlains = Area("The Eerie Grassland", "a stretch of grassland, with eerie mists falling to the ground")
    gate = Area("The Portal Gate", "a large, stone gate that prevents you from progressing further")
    portal = Area("The Swirling Portal", "a swirling, screaming portal")

    desertN.borderAreas.append(eeriePlains)
    eeriePlains.borderAreas = [desertN, gate]
    gate.borderAreas = [eeriePlains] #ADD PORTAL LATER AS AN ACTION (USING A KEY)
    portal.borderAreas = [gate]

    #CREATE ENTITIES
    goblin =    Entity("Goblin", 3, 2)
    golem =     Entity("Golem",  6, 4)
    
    #CREATE ITEMS
    stick =     Item("Stick")
    sword =     Item("Sword")
    stone =     Item("Stone")
    
    #SETUP VARIABLES
    area = forest
    
    #PRE-GAME
    chooseClass(player)

    #MAIN LOOP
    while True:
        
        choices = ["View stats", "Travel to another area"]
        print(f"You are currently in {area.name}: {area.desc}.\n")
        
        if len(area.entities) == 1:
            choices.append("Fight a monster")
            print(f"There is a monster in this area.\n")
            
        if len(area.entities) > 1:
            choices.append("Fight a monster")
            print(f"There are {len(area.entities)} monsters in this area.\n")
            
        if area == village:
            choices.append("Visit the tavern")
            choices.append("Visit the mystic")
            
        if area == obelisk:
            choices.append("Inspect the obelisk")

        print("Choose what to do:")
        choice = mainChoice(choices)
        
        if choice == "View stats":
            clear()
            viewStats(player)
 
        if choice == "Travel to another area":
            clear()
            area = travel(area)
       
        if choice == "Fight a monster":
            clear()
            chooseMonster(area, player)
            
        if choice == "Visit the tavern":
            clear()
            shop(village, player)            

        if choice == "Visit the mystic":
            clear()
            mystic(player)
            
        if choice == "Inspect the obelisk":
            clear()
            obeliskInspect(player)
            
        if player.lives <= 0:
            clear()
            print("You have run out of lives! \nGame over... \n")
            break
            
        input("\nPress enter to continue...")
        clear()
                
    
 
#RUN GAME
if __name__ == "__main__":
    main(Player())
    
