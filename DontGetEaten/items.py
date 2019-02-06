class Item:
    def __init__(self, name):
        self.name = name
        self.description = ""
        self.specialPrompt = ""
        self.specialText = ""

    def setName(self, name):
        self.name = name

    def getName(self):
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

    def removeItem(self, item):
        try:
            self.contents.remove(item)
        except ValueError:
            return False
        return True

    def removeItemByName(self, item_name):
        for item in self.contents:
            if item.getName() == item_name:
                self.contents.remove(item)
                

    def takeItem(self, item_name):
        for items in self.contents:
            if items.getName() == item_name:
                item = items
                self.contents.remove(item)
                return item
        return None
        
    def showItems(self):
        if not self.contents:
            print("There is nothing there.")
        for items in self.contents:
            if not items == None: print("You see", items.getDescription())
