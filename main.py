
#SETUP CLASSES
class Player:
    def __init__(self):
        self.health = 100
        
class Area:
    def __init__(self, name):
        self.name = name
        self.entities = []
        self.items = []
        self.borderAreas = []
        
    def addEntity(self, entity):
        self.entities += entity
        
    def addItem(self, item):
        self.items += item
        
    def delEntity(self, entity):
        self.entities.remove(entity)
        
    def delItem(self, item):
        self.items.remove(item)
  
class Entity:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
class Item:
    def __init__(self, name):
        self.name = name
 

#SETUP FUNCTIONS
def travel(curArea, newArea):  
    
    if newArea in curArea.borderAreas:
        print(f"Travelled from {curArea.name} to {newArea.name}")
        return newArea
    
    print(f"Could not travel from {curArea.name} to {newArea.name}")
    return curArea


def main(player):
    #CREATE AREAS
    forest =    Area("Forest")
    desert =    Area("Desert")
    village =   Area("Village")
    
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
    while True:
        travel(forest, forest)
        travel(forest, desert)
        travel(forest, village)
        travel(desert, forest)
        travel(desert, desert)
        travel(desert, village)
        travel(village, forest)
        travel(village, desert)
        travel(village, village)
        input()
 
#RUN GAME
if __name__ == "__main__":
    main(Player())
    