class Tile:
    def __init__(self):
        self.name = 'empty tile'
        self.location = [0,0]
        self.description = ''

    def getName(self):
        return self.name

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
        emptyTile = Tile()
        self.map = [[emptyTile] for i in range(x)]
        for i in range(x):
            for j in range(1, y):
                self.map[i].append(emptyTile)

    def addTile(self, tile, x, y):
        self.map[x][y] = tile
        
        
    def gimmeMap(self):
        return self.map






'''
============
Testy Testy
============

listy = [[]]

print(listy)
listy[0] += ['blue']
listy[0].append('red')
print(listy[0][0])
print(listy[0][1])
print('\n\n', listy[0], '\n\n')
'''
kitchen = Room(3,4)
kitchenMap = kitchen.gimmeMap()
print(kitchenMap[0][0].getName(), "\n\n")
print(kitchenMap[1][1].getName(), "\n\n")



