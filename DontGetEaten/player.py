class Player:

    def __init__(self):
        self.name = 'nobody'
        self.alive = True
        self.inventory = []
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

    def move(self, direction):
        print("useless")
        

    
    

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

        
