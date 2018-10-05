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

def movePlayer(player, the_map, direction):
    startPosition = player.getLocation()
    


def main():
    cell = Room(4,4)
    topLeft = Tile()
    topCenter = Tile()
    topRight = Tile()
    centerLeft = Tile()
    centerCenter = Tile()
    centerRight = Tile()
    bottomLeft = Tile()
    bottomCenter = Tile()
    bottomRight = Tile()


    
    player1 = runIntro()

    player_continue = True
    while player_continue:
        userInput = input("Press 0 to nap. ")
        if (userInput == '0'):
            player_continue = False
            
        

if __name__ == "__main__": main ()


    
