from player import Player
from first_cell import loadStartingRoom

def runIntro():
    player1 = Player()
    print("===================================\n         Don't Get Eaten\n===================================\n\n")
    player_name = input('Hello?\n\nWho\'s there? ')
    player1.namePlayer(player_name)    
    print("\n\nYou're in a scary cell ", player1.name, ". Have a nap until it goes away.\n", sep='')
    return player1

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

        if userInput == 'look':
            player1.lookForThings()
 
        if userInput.split(' ', 1)[0] == 'take':
            try:
                item_name = userInput.split(' ', 1)[1]
                player1.pickUp(item_name)
            except IndexError:
                print("Take what?")

        if userInput.split(' ', 1)[0] == 'drop':
            try:
                item_name = userInput.split(' ', 1)[1]
                player1.putDown(item_name)
            except IndexError:
                print("Drop what?")

        if userInput == 'i':
            player1.showItems()
            

if __name__ == "__main__": main ()


    
