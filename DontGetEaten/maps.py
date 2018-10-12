from items import Item
from items import Inventory

class Tile:
    def __init__(self):
        self.name = 'Empty'
        self.location = [0,0]
        self.description = ''
        self.inventory = Inventory()
        self.north = False
        self.east = False
        self.south = False
        self.west = False

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    def setLocation(self, location):
        self.location = location

    def getLocation(self):
        return self.location

    def makePath(self, direction):
        if direction == "n": self.north = True
        if direction == "e": self.east = True
        if direction == "s": self.south = True
        if direction == "w": self.west = True
        if direction == "all":
            self.north = True
            self.east = True
            self.south = True
            self.west = True

    def clearPath(self, direction):
        if direction == "n": self.north = False
        if direction == "e": self.east = False
        if direction == "s": self.south = False
        if direction == "w": self.west = False
        if direction == "all":
            self.north = False
            self.east = False
            self.south = False
            self.west = False

    def checkPath(self, direction):
        if direction == "n": return self.north
        if direction == "e": return self.east
        if direction == "s": return self.south
        if direction == "w": return self.west

    def putItem(self, item):
        self.inventory.addItem(item)

    def takeItem(self, item):
        self.inventory.removeItem()

    def lookForThings(self):
        self.inventory.showItems()


class Room:
    def __init__(self, x, y):
        self.width = x
        self.length = y
        emptyTile = Tile()
        self.map = [[emptyTile] for i in range(x)]
        for i in range(x):
            for j in range(1, y):
                self.map[i].append(emptyTile)

    def addTile(self, tile, x, y):
        tile.setLocation([x, y])
        self.map[x][y] = tile

    def getTile(self, x, y):
        return self.map[x][y]

    def nameTile(self, name, x, y):
        self.map[x][y].setName(name)

    def getMap(self):
        return self.map

    def printMap(self):
        y = self.length - 1
        x = self.width - 1
        for i in range(self.width):
            for j in range(self.length):
                print(x, y, " : ", self.map[x][y].getName())
                y -= 1
            print("\n")
            y = self.length - 1
            x -= 1


