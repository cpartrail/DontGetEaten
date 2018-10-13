from maps import Tile
from maps import Room
from items import Item
from items import Inventory

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

    def lookForThings(self):
        self.map.getTile(self.location[0], self.location[1]).lookForThings()

    def pickUp(self, item_name):
        item = self.map.getTile(self.location[0], self.location[1]).takeItem(item_name)
        if item:
            self.inventory.addItem(item)

    def putDown(self, item_name):
        item = self.inventory.takeItem(item_name)
        if item: self.map.getTile(self.location[0], self.location[1]).putItem(item)


    def addItem(self, item):
        self.inventory.addItem(item)

    def removeItem(self, item):
        return self.inventory.removeItem(item)

    def showItems(self):
        self.inventory.showItems()


