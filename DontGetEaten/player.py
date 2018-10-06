from maps import Tile
from maps import Room

class Player:

    def __init__(self):
        self.name = 'nobody'
        self.alive = True
        self.inventory = []
        self.map = None
        self.location = [0,0]

    def killPlayer(self):
        self.alive = False

    def revivePlayer(self):
        self.alive = True

    def namePlayer(self, name):
        self.name = name

    def addItem(self, item):
        self.inventory.append(item)

    def removeItem(self, item):
        self.inventory.remove(item)

    def showItems(self):
        for items in self.inventory: print(items)

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
            self.location[1] -= 1
            return True
        return False
        


    
    

'''
=================
    TESTING
=================
'''

'''
Player1 = Player()
Player1.namePlayer('Corey')
Player1.killPlayer()
print("Player 1 name is", Player1.name)
print("Player 1 is alive?", Player1.alive, "\n")
      
Player2 = Player()
print("Player 2 name is", Player2.name)
print("Player 2 is alive?", Player2.alive)
'''
kitchen = Room(3,4)
sink = Tile()
fridge = Tile()
counter = Tile()
sink.setName("Sink")
fridge.setName("fridge")
counter.setName("counter")
kitchen.addTile(sink, 0, 0)
kitchen.addTile(fridge, 0, 1)
kitchen.addTile(counter, 0, 2)
kitchen.getTile(0, 1).makePath("n")
kitchen.getTile(0, 1).makePath("s")

player1 = Player()
player1.putPlayer(kitchen, 0, 1)
print(player1.getLocation())
player1.movePlayer("n")
print(player1.getLocation())
player1.movePlayer("e")
print(player1.getLocation())
