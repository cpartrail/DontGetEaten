from items import Inventory
from items import Item
from maps import Tile
from maps import Room


def loadStartingRoom():
    cell = Room(3,3)

    topLeft = Tile()
    topLeft.setName("Top Left Corner")
    topLeft.setDescription("The corner is dark and full of bones.")
    topLeft.makePath("s")
    topLeft.makePath("e")
    cell.addTile(topLeft, 0, 2)

    topCenter = Tile()
    topCenter.setName("Top Center Wall")
    topCenter.setDescription("Dim grey light spills through a barred window.")
    topCenter.makePath("w")
    topCenter.makePath("e")
    topCenter.makePath("s")
    cell.addTile(topCenter, 1, 2)
    
    topRight = Tile()
    topRight.setName("Top Right Corner")
    topRight.setDescription("The corner looks empty, but it's too dark to know for sure.")
    topRight.makePath("w")
    topRight.makePath("s")
    cell.addTile(topRight, 2, 2)

    centerLeft = Tile()
    centerLeft.setName("Center Left Wall")
    centerLeft.setDescription("The wall is bare.")
    centerLeft.makePath("s")
    centerLeft.makePath("n")
    centerLeft.makePath("e")
    cell.addTile(centerLeft, 0, 1)

    center = Tile()
    center.setName("Cell Center")
    center.setDescription("The light is dim and the shadows deep. You must find a way out of this place.")
    center.makePath("all")
    cell.addTile(center, 1, 1)
    
    centerRight = Tile()
    centerRight.setName("Center Right Door")
    centerRight.setDescription("There is a door - locked and far too heavy to break.")
    centerRight.makePath("s")
    centerRight.makePath("n")
    centerRight.makePath("w")
    cell.addTile(centerRight, 2, 1)
    
    bottomLeft = Tile()
    bottomLeft.setName("Bottom Left Corner")
    bottomLeft.setDescription("A sad pile of blankets sits balled up in the corner.")
    bottomLeft.makePath("n")
    bottomLeft.makePath("e")
    cell.addTile(bottomLeft, 0, 0)
    
    bottomCenter = Tile()
    bottomCenter.setName("Bottom Center Wall")
    bottomCenter.setDescription("Bright eyes shine from a small hole in the wall. Large bones lie scattered on the floor.")
    bottomCenter.makePath("n")
    bottomCenter.makePath("e")
    bottomCenter.makePath("w")
    cell.addTile(bottomCenter, 1, 0)
    
    bottomRight = Tile()
    bottomRight.setName("Bottom Right Corner")
    bottomRight.setDescription("Rocks and debris lie everywhere, crunching and crackling underfoot.")
    bottomRight.makePath("n")
    bottomRight.makePath("w")
    cell.addTile(bottomRight, 2, 0)

    paper = Item("paper")
    paper.setDescription("an old piece of yellowed paper. There's some faded writing on it.")
    paper.setPrompt("read")
    topRight.putItem(paper)

    sandwich = Item("sandwich")
    sandwich.setDescription("a half eaten sandwich. It looks like peanut butter and pickle.")
    sandwich.setPrompt("eat")
    centerLeft.putItem(sandwich)

    key = Item("key")
    key.setDescription("a shiny key.")
    key.setPrompt("unlock")
    cell.putItem(key)
    
    return cell
