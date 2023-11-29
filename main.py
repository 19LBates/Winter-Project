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
        travel(curArea)
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
        return int(choice) - 1
    except:
        clear()
        print("Invalid input. Please try again \n")
        mainChoice(choices)


def main(player):
    #CREATE AREAS
    forest =    Area("The Forest", "")
    plainsW =   Area("A Grassland", "")
    village =   Area("The Village", "")
    savanna =   Area("The Savanna", "")
    desert =    Area("The Desert", "")
    mountain =  Area("The Great Mountain", "")
    hut =       Area("The Mountain Hut", "")
    hillsNW =   Area("Some Hills", "")
    plainsN =   Area("A Grassland", "")
    desertN =   Area("The Frozen Desert", "")
    hillsNE =   Area("Some Hills", "")
    valleyN =   Area("A Valley", "")
    pond =      Area("A Pond", "")
    valleyE =   Area("A Valley", "")
    ruins =     Area("The Ruins", "")
    plainsE =   Area("A Grassland", "")
    graves =    Area("The Graveyard", "")
    church =    Area("The Church", "")
    cityE =     Area("The East Side of The City", "")
    cityW =     Area("The West Side of The City", "")
    hillsS =    Area("Some Hills", "")
    valleyS =   Area("A Valley", "")
    lake =      Area("The Lake", "")
    obelisk =   Area("The Obelisk", "")
    
    forest.borderAreas =    [desert, village]
    desert.borderAreas =    [forest]
    village.borderAreas =   [forest]
    
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
    
    #MAIN LOOP
    print(mainChoice(["a", "b", "c", "d"]))
 
#RUN GAME
if __name__ == "__main__":
    main(Player())
    
