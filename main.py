#IMPORT MODULES
from calendar import c
import os

#SETUP CLASSES
from asyncio.windows_events import NULL


class Player:
    def __init__(self):
        self.health = 10
        self.inventory = []
        
class Area:
    def __init__(self, name):
        self.name = name
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
    print(choice)
    
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
    


def main(player):
    #CREATE AREAS
    forest =    Area("The Forest")
    desert =    Area("The Desert")
    village =   Area("The Village")
    
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
    area = travel(area)
 
#RUN GAME
if __name__ == "__main__":
    main(Player())
    