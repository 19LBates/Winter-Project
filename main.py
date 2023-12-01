#IMPORT MODULES
import os

#SETUP CLASSES
class Player:
    def __init__(self):
        self.health = 10
        self.inventory = []
        
class Area:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.entities = []
        self.items = []
        self.borderAreas = []     
  
class Entity:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
class Item:
    def __init__(self, name):
        self.name = name
 

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
        print(f"You have stayed in {curArea.name} \n")
        return curArea
    
    try:
        newArea = areaList[int(choice)-2]
    except:
        clear()
        print("Invalid input. Please try again. \n")
        return travel(curArea)
    else:
        clear()
        print(f"You have travelled from {curArea.name} to {newArea.name} \n")
        return newArea
        
    
def listBorderAreas(area):
    areaList = area.borderAreas  
    print(f"1 - Remain in {area.name}")
    i = 2
    for area in areaList:
        print(f"{i} - Travel to {area.name}")
        i += 1

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
        return int(choice)


def main(player):
    #CREATE AREAS
    forest =    Area("The Forest", "")
    plainsW =   Area("The Western Grassland", "")
    village =   Area("The Village", "")
    savanna =   Area("The Savanna", "")
    desert =    Area("The Desert", "")
    mountain =  Area("The Great Mountain", "")
    hut =       Area("The Mountain Hut", "")
    hillsNW =   Area("The Northern Hills", "")
    plainsN =   Area("The Northern Grassland", "")
    desertN =   Area("The Frozen Desert", "")
    hillsNE =   Area("Some Hills", "")
    valleyN =   Area("The Valley", "")
    pond =      Area("The Pond", "")
    valleyE =   Area("The Valley", "")
    ruins =     Area("The Ruins", "")
    plainsE =   Area("The Eastern Grassland", "")
    graves =    Area("The Graveyard", "")
    church =    Area("The Church", "")
    cityE =     Area("The East Side of The City", "")
    cityW =     Area("The West Side of The City", "")
    hillsS =    Area("The Southern Hills", "")
    valleyS =   Area("The Southern Valley", "")
    lake =      Area("The Lake", "")
    obelisk =   Area("The Obelisk", "")
    
    createBorderAreas([forest, plainsW, village, savanna, desert, mountain, hut, hillsNW, plainsN, desertN, hillsNE, valleyN, 
                       pond, valleyE, ruins, plainsE, graves, church, cityE, cityW, hillsS, valleyS, lake, obelisk])

    eeriePlains = Area("The Eerie Grassland", "")
    gate = Area("The Portal Gate", "")
    portal = Area("The Swirling Portal", "")

    desertN.borderAreas.append(eeriePlains)
    eeriePlains.borderAreas = [desertN, gate]
    gate.borderAreas = [eeriePlains, portal]
    portal.borderAreas = [gate]

    #CREATE ENTITIES
    goblin =    Entity("Goblin", 8)
    spider =    Entity("Spider", 3)
    mummy =     Entity("Mummy" , 9)
    
    #CREATE ITEMS
    stick =     Item("Stick")
    sword =     Item("Sword")
    stone =     Item("Stone")
    
    #SETUP VARIABLES
    area = forest
    
    #MAIN LOOP)
    clear()
    while True:

        #choice = mainChoice(["Travel to a different area", "crip"])
        area = travel(area)
    
 
#RUN GAME
if __name__ == "__main__":
    main(Player())
    
