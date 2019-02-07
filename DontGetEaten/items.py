class Item:
    def __init__(self, name):
        self.name = name
        self.description = ""
        self.specialPrompt = ""
        self.specialText = ""

    def setName(self, name):
        self.name = name

    def getName(self):
        #returns string
        return self.name

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    def setSpecialText(self, text):
        self.specialText = text

    def setPrompt(self, prompt):
        self.specialPrompt = prompt

    def checkPrompt(self, prompt):
        if prompt == specialPrompt: return self.specialText
        else: return False 
        

class Inventory:
    def __init__(self):
        self.contents = []

    def addItem(self, item):
        self.contents.append(item)

    def removeItem(self, item_name):
        for items in self.contents:
            if items.getName() == item_name:
                item = items
                self.contents.remove(item)
                return item
        return None

    def checkInventory(self, item_name):
        for items in self.contents:
            if items.getName() == item_name:
                return True
        return False
        
    def showItems(self):
        if not self.contents:
            print("There is nothing there.")
        for items in self.contents:
            if not items == None: print("You see", items.getDescription())

    def showPlayerItems(self):
        if not self.contents:
            print("Your pockets are empty.")
        else:
            print("You check your pockets. You have: ")
            for items in self.contents:
                if not items == None: print(items.getName())
