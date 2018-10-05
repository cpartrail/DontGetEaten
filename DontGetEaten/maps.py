class Tile:
    def __init__(self):
        self.name = 'Wall'
        self.location = [0,0]
        self.description = ''

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def updateDescription(self, description):
        self.description = description

    def gimmeDescription(self):
        return self.description

    def setLocation(self, location):
        self.location = location

    def getLocation(self):
        return self.location


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

    def checkBoundary(self, x, y):
        if self.map[x][y].getName() == "Wall":
            print("I've hit a wall")
        else:
            print("I can move!")






'''
============
Testy Testy
============
'''
'''
kitchen = Room(3,4)
kitchen.printMap()
print("\nAdding sink and fridge")
sink = Tile()
fridge = Tile()
sink.setName("Sink")
fridge.setName("fridge")
kitchen.addTile(sink, 0, 0)
kitchen.addTile(fridge, 2, 3)

kitchen.printMap()
print("\n\n")
kitchen.checkBoundary(2,3)
kitchen.checkBoundary(0,1)
'''
