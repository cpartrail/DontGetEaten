from player import Player
from maps import Tile
from maps import Room

def playerCommands(playerInput):
    '''
    For use in main while loop. Take in player input figure out if it is an action,
    movement, or quit command. Output nothing.
    '''

def runIntro():
    player1 = Player()
    print("===================================\n         Don't Get Eaten\n===================================\n\n")
    player_name = input('Hello?\n\nWho\'s there? ')
    player1.namePlayer(player_name)    
    print("\n\nYou're in a scary cell ", player1.name, ". Have a nap until it goes away.\n", sep='')
    return player1

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
    centerLeft.setDescription("The wall is bare. A half eaten sandwich sits on the floor.")
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
    centerRight.setDescription("There is a door - locked and far to heavy to break.")
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

    return cell


def main():
    
    player1 = runIntro()
    startRoom = loadStartingRoom()
    player1.putPlayer(startRoom, 1, 1)
    player_moved = False
    
    player_continue = True
    while player_continue:
        userInput = input("Press q to nap. ")
        if userInput == 'q':
            player_continue = False
        if userInput == 'w':
            player_moved = player1.movePlayer("n")
        if userInput == 'a':
            player_moved = player1.movePlayer("w")
        if userInput == 's':
            player_moved = player1.movePlayer("s")
        if userInput == 'd':
            player_moved = player1.movePlayer("e")
        if player_moved == True: player1.printScene()
        player_moved = False

        if userInput == 'look': player1.printScene()
        if userInput.split(' ', 1)[0] == 'take': print("TakeIt!")
        

if __name__ == "__main__": main ()


    
