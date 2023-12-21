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
        self.obeliskUses = 0
        self.turnsSinceMystic = 100
        
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
    def __init__(self, name, desc = "", str = 0, cost = 0):
        self.name = name
        self.desc = desc
        self.str = str
        self.cost = cost
 

#SETUP FUNCTIONS
def numStr(singular, plural, num):
    if num == 1:
        return (f"1 {singular}")
    
    if plural == "s":
        return (f"{num} {singular}s")
    
    return (f"{num} {plural}")


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
       

def travel(startArea, travels):
    curArea = startArea

    for x in range(travels):
        newArea = travelOne(curArea)
        if newArea == "REMAIN": break
        curArea = newArea
        clear()
    clear()

    if startArea == curArea:
        print(f"You have remained in the {startArea.name}")
        return startArea

    print(f"You have travelled from the {startArea.name} to the {curArea.name}")
    return curArea


def travelOne(curArea):
    clear()
    listBorderAreas(curArea)
    areaList = curArea.borderAreas
    choice = input("\nEnter your choice: ")
    
    if choice == "1": return "REMAIN"
    
    try:
        newArea = areaList[int(choice)-2]
    except:
        print("Invalid input. Please try again. \n")
        return travelOne(curArea)
    else:
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
    print(f"You have {player.str} Strength and {numStr("Life", "Lives", player.lives)} Remaining.\n")
    print("Monsters to fight:")
    print("1 - Cancel fight")
    for monster in monsters:
        print(f"{i} - {monster.name}: Has {monster.str} Strength, Carrying {numStr("Gold Coin", "s", monster.gold)}")
        i += 1
        
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
    playerDice = dice(player, 1, 6, "high")
    monsterDice = random.randint(1, 6)
    playerFinalStr = player.str + playerDice
    monsterFinalStr = monster.str + monsterDice

    print(f"Your strength is {player.str}, and you rolled a {playerDice}. Your final strength is therefore {playerFinalStr}.")
    print(f"The {monster.name}'s strength is {monster.str}, and it rolled a {monsterDice}. Its final strength is therefore {monsterFinalStr}.")

    if playerFinalStr > monsterFinalStr:
        area.entities.remove(monster)
        print(f"\nYou defeated the {monster.name}!")
        player.gold += monster.gold
        print(f"You got {numStr("gold coin", "s", monster.gold)} from the monster. You now have {numStr("gold coin", "s", player.gold)}.")
        return
    
    if monsterFinalStr > playerFinalStr:
        player.lives += -1
        print(f"\nThe {monster.name} overpowered you! You have {numStr("Life", "Lives", player.lives)} remaining.")
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
    print("4 - Wizard:  1 Life,  0 Strength, 2 Gold Coins")
    
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
        player.lives = 1
        player.str = 0
        player.gold = 2
        player.cls = "Wizard"
   
    player.maxLives = player.lives
    clear()


def shop(items, player, name = "shop"):
    print(f"Welcome to the {name}! You have {numStr("gold coin", "s", player.gold)} to spend.")
    print(f"\n1 - Leave the {name}")
    i = 2
    for item in items:
        print(f"{i} - {item.name}: {item.desc} - Costs {item.cost} Gold")
        i += 1
    
    choice = input("\nEnter your choice: ")
    if choice == "1": return
    try:
        item = items[int(choice)-2]
    except:
        clear()
        print("Invalid input. Please try again. \n")
        return shop(items, player)
    else: 
        if player.gold < item.cost:
            print("\nYou are too poor to buy this item!")
            return
        
        player.gold -= item.cost
        player.inventory.append(item)
        items.remove(item)
        player.str += item.str
        print(f"\nYou bought a {item.name} for {numStr("gold coin", "s", item.cost)}. \nYou have {numStr("gold coin", "s", player.gold)} remaining.")
        

def mystic(player):
    print("Welcome to the Mystic! Here, anything can happen, good or bad!\n")
    print("1 - Leave the Mystic")
    print("2 - Allow the Mystic to use her magic")
    
    choice = input("\nEnter your choice: ")
    if choice == "1": return
    if choice not in ["1", "2"]:
        clear()
        print("Invalid input. Please try again. \n")
        return mystic(player)
    
    roll = dice(player, 1, 6, "high")
    player.turnsSinceMystic = 0
    print()
    if roll == 1:
        player.lives += -1
        print(f"The mystic blundered, and you lost a life! \nYou have {numStr("life","lives",player.lives)} remaining.")
    elif roll == 2:
        player.gold += -1
        print(f"The mystic blundered, and you lost a gold coin! \nYou now have {numStr("gold coin", "s", player.gold)}.")
    elif roll == 3:
        print("Nothing happened")
    elif roll == 4:
        player.gold += 1
        print(f"Golden dust appears before you, and materialises into a golden coin! \nYou now have {numStr("gold coin", "s", player.gold)}.")
    elif roll == 5:
        player.str += 1
        print(f"You feel strength coursing through your veins. \nYou now have {player.str} strength.")
    elif roll == 6:
        player.lives += 1
        print(f"You feel a wave of rejuvination wash over you. \nYou now have {numStr("Life", "Lives", player.lives)}.")

        
def obeliskInspect(player):
    if player.cls != "Wizard":
        print("You walk up to the obelisk and see an inscribed message:")
        print("!¡ꖎᔑᓵᒷ ᔑ ⊣𝙹ꖎ↸ coin 𝙹リ thee, ᔑリ↸ ᒲᔑ⊣╎ᓵ powers ||𝙹⚍ ∴╎ꖎꖎ ᓭᒷᒷ")
        return
    
    if player.obeliskUses > 7:
        print("The obelisk is drained of power...")
        return
    
    print("You walk up to the obelisk and see an inscribed message:")
    print("Place a gold coin on thee, and magic powers you will see...")
    
    if player.gold < 1:
        return
    
    player.gold += -1
    player.obeliskUses += 1
    if random.randint(0,1) == 0:
        print("\nYou sacrificed 1 gold coin in return for 1 strength.")
        player.str += 1
    else:
        print("\nYou sacrificed 1 gold coin in return for 1 extra life.")
        player.lives += 1
        player.maxLives += 1

    
def dice(player, small, big, better = "none"):
    if (player.cls != "Wizard") or (random.randint(0,1) == 0):
        return random.randint(small, big)
    
    a = random.randint(small, big)
    b = random.randint(small, big)
    
    if better == "high": return max([a,b])
    if better == "low": return min([a,b])
    return a


def win(player):
    while True:
        clear()
        print("Congratulations! \nYou were able to reach to reach the portal, allowing you to return the land to peace once again...\n\n")
        viewStats(player)
        input()


def drink(player, potion):
    if potion.name == "Health Potion":
        if player.lives >= player.maxLives:
            player.lives += 1
        else:
            player.lives += 2
        print(f"You now have {numStr("Life", "Lives", player.lives)}.")
    
    if potion.name == "Strength Potion":
        player.str += 1
        print(f"You now have {player.str} Strength.")
        
    player.inventory.remove(potion)
    return



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
    valleyN =   Area("The Northern Valley", "an area surrounded by many hills")
    pond =      Area("The Pond", "a small pond, home to a few ducks")
    valleyE =   Area("The Eastern Valley", "an area surrounded by many hills")
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
    spider =    Entity("Spider", 2, 0)
    bear =      Entity("Bear", 4, 0)
    golem =     Entity("Golem",  6, 4)
    mummy =     Entity("Ancient Mummy", 3, 3)
    shark =     Entity("Shark", 7, 4)
    piranha =   Entity("Piranha", 3, 2)
    skeleton =  Entity("Reanimated Skeleton", 3, 3)

    forest.entities =   [goblin, bear]
    plainsW.entities =  []
    village.entities =  []
    savanna.entities =  []
    desert.entities =   [mummy]
    mountain.entities = [golem]
    hut.entities =      []
    hillsNW.entities =  []
    plainsN.entities =  []
    desertN.entities =  []
    hillsNE.entities =  [golem]
    valleyN.entities =  []
    pond.entities =     [piranha]
    valleyE.entities =  []
    ruins.entities =    [skeleton]
    plainsE.entities =  []
    graves.entities =   [skeleton, skeleton]
    church.entities =   []
    cityE.entities =    []
    cityW.entities =    []
    hillsS.entities =   []
    valleyS.entities =  []
    lake.entities =     [shark]  
    obelisk.entities =  []
    
    #CREATE ITEMS
    pot_hp =    Item("Health Potion", "A small vile of glowing, pink liquid.", 0, 2)
    pot_str =   Item("Strength Potion", "A small vile of deep, crimson liquid.", 0, 2)
    sword =     Item("Sword", "A gleaming, steel sword.", 2, 4)
    portalKey = Item("Portal Key", "A mysterious key, that faintly glows purple in the dark.", 0, 10)
    
    #SETUP VARIABLES
    area = forest
    randomMonsters = [goblin, spider]
    
    #PRE-GAME
    clear()
    print("You find yourself in a corrupted world, overrun by monsters. \nTo restore peace to the world, you must acquire the artifact of power. \nTo find the artifact, you must travel through the swirling portal, which is guarded by an indestructable gate.")
    input("\nPress enter to begin...") ; clear()
    chooseClass(player)
    tavernItems = [pot_hp, pot_str, sword, portalKey]
    marketItems = [pot_hp, pot_hp, pot_str, pot_str, sword, portalKey]

    #MAIN LOOP
    while True:

        if (portalKey in player.inventory) and not (portal in gate.borderAreas):
            gate.borderAreas.append(portal)
        
        if random.randint(0,5) == 0:
            monster = random.choice(randomMonsters)
            print(f"You have been attacked by a {monster.name}!\n")
            input("Press enter to continue...")
            clear()
            area.entities.append(monster)
            fight(area, player, monster)
        
        if player.lives <= 0:
            print("\nYou have run out of lives! \nGame over... \n")
            break

        choices = ["View stats", "Travel to another area"]
        print(f"You are currently in {area.name}: {area.desc}.\n")
        
        if pot_hp in player.inventory: choices.append("Drink your Health Potion")
        if pot_str in player.inventory: choices.append("Drink your Strength Potion")

        if len(area.entities) == 1:
            choices.append("Fight a monster")
            print(f"There is a monster in this area.\n")
            
        if len(area.entities) > 1:
            choices.append("Fight a monster")
            print(f"There are {len(area.entities)} monsters in this area.\n")
            
        if area == village: choices.append("Visit the tavern")
        
        if (area == village) and (player.turnsSinceMystic >= 4): choices.append("Visit the mystic")

        if area == cityE: choices.append("Visit the mystic")
        if area == cityW: choices.append("Visit the market")
            
        if area == obelisk: choices.append("Inspect the obelisk")

        print("Choose what to do:")
        choice = mainChoice(choices)
        
        if choice == "View stats":
            clear()
            viewStats(player)
            player.turnsSinceMystic += -1
 
        if choice == "Travel to another area":
            clear()
            area = travel(area, random.randint(1, 3))
            if area == portal:
                win(player)
       
        if choice == "Fight a monster":
            clear()
            chooseMonster(area, player)
            
        if choice == "Visit the tavern":
            clear()
            shop(tavernItems, player, "tavern")        

        if choice == "Visit the market":
            clear()
            shop(marketItems, player, "market")   

        if choice == "Visit the mystic":
            clear()
            mystic(player)
            
        if choice == "Inspect the obelisk":
            clear()
            obeliskInspect(player)

        if choice == "Drink your Health Potion":
            clear()
            drink(player, pot_hp)

        if choice == "Drink your Strength Potion":
            clear()
            drink(player, pot_str)
            
        if player.lives <= 0:
            print("\nYou have run out of lives! \nGame over... \n")
            break
            
        input("\nPress enter to continue...")
        player.turnsSinceMystic += 1
        clear()
                
    
 
#RUN GAME
if __name__ == "__main__":
    main(Player())
    
