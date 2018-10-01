class Tile:
    def __init__(self, name):
        self.name = name
        self.location = [0,0]
        self.description = ''

    def updateDescription(self, description):
        self.description = description

    def setLocation(self, x, y):
        self.location = [x, y]
        
