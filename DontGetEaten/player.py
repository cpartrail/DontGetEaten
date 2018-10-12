from maps import Tile
from maps import Room

class Player:

    def __init__(self):
        self.name = 'nobody'
        self.alive = True
        self.inventory = Inventory()
        self.map = None
        self.location = [0,0]

    def killPlayer(self):
        self.alive = False

    def revivePlayer(self):
        self.alive = True

    def namePlayer(self, name):
        self.name = name

    def putPlayer(self, room, x, y):
        self.map = room
        self.location = [x, y]

    def getLocation(self):
        return(self.location)

    def movePlayer(self, direction):
        if self.map == None: return False
        start_tile = self.map.getTile(self.location[0], self.location[1])
        if direction == "n" and start_tile.checkPath("n"):
            self.location[1] += 1
            return True
        if direction == "e" and start_tile.checkPath("e"):
            self.location[0] += 1
            return True
        if direction == "s" and start_tile.checkPath("s"):
            self.location[1] -= 1
            return True
        if direction == "w" and start_tile.checkPath("w"):
            self.location[0] -= 1
            return True
        return False

    def printScene(self):
        print(self.map.getTile(self.location[0], self.location[1]).getDescription())

    def addItem(self, item):
        self.inventory.addItem(item)

    def removeItem(self, item):
        return self.inventory.removeItem(item)

    def showItems(self):
        self.inventory.showItems()

    

class Item:
    def __init__(self, name):
        self.name = name
        self.description = ""

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description


class Inventory:
    def __init__(self):
        self.contents = []

    def addItem(self, item):
        self.contents.append(item)

    def removeItem(self, item):
        try:
            self.contents.remove(item)
        except ValueError:
            return False
        return True
        
    def showItems(self):
        for items in self.contents: print(items.getName())
    
    

'''
=================
    TESTING
=================
'''


Player1 = Player()
Player1.namePlayer('Corey')

chocolate = Item("Chocolate Bar")
chocolate.setDescription("A great big bar of chocolate")
pizza = Item("Pizza")
pizza.setDescription("A half eaten slice of pizza.")
sandwich = Item("Sandwich")
sandwich.setDescription("A peanut butter and ketchup sandwich. Gross.")


Player1.addItem(chocolate)
Player1.addItem(pizza)
Player1.addItem(sandwich)
Player1.showItems()

t = Player1.removeItem(pizza)

print(t, "\n\n")
Player1.showItems()
f = Player1.removeItem(pizza)
print("\n", f)

