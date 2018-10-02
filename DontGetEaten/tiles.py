class Tile:
    def __init__(self):
        self.name = 'empty tile'
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

    def gimmeLocation(self):
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
        self.map[x][y] = tile

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






'''
============
Testy Testy
============
'''

kitchen = Room(3,4)
kitchen.printMap()
print("\n\n")
sink = Tile()
sink.setName("Kitchen Sink")

kitchen.addTile(sink, 0, 0)
kitchen.addTile(sink, 1, 2)

kitchen.printMap()

