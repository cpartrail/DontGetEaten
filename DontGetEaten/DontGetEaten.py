from player import Player
from first_cell import loadStartingRoom

def runIntro():
    player1 = Player()
    print("===================================\n         Don't Get Eaten\n===================================\n\n")
    player_name = input('Hello? Who\'s there? ')
    player1.namePlayer(player_name)    
    print("\nYou're in a scary cell ", player1.name, ". Have a nap until it goes away.\n", sep='')
    input("\n")
    print("Fine then. Have a look around if you must. \nUse W A S D to move around. Press 'q' if you change your mind.\n")
    return player1

def main():
    
    player1 = runIntro()
    startRoom = loadStartingRoom()
    player1.putPlayer(startRoom, 1, 1)

    player_moved = False
    
    player_continue = True
    while player_continue:
        userInput = input("...")
        if userInput == 'q':
            player_continue = False
        if userInput == 'w':
            player_moved = player1.movePlayer("n")
            if player_moved == False: print("I can't move further north")
        if userInput == 'a':
            player_moved = player1.movePlayer("w")
            if player_moved == False: print("I can't move further west")
        if userInput == 's':
            player_moved = player1.movePlayer("s")
            if player_moved == False: print("I can't move further south")
        if userInput == 'd':
            player_moved = player1.movePlayer("e")
            if player_moved == False: print("I can't move further east")
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

        if userInput.split(' ', 1)[0] == 'eat':
            try:
                item_name = userInput.split(' ', 1)[1]
                if player1.inventory.checkInventory(item_name):
                    if item_name == "sandwich":
                        key = startRoom.takeItem("key")
                        player1.transmute("sandwich", key)
                        print("Ouch! My tooth!\n\nYou seem to have munched down on something hard. You pull it out of your mouth.")
                    else:
                        print("You can't eat that.\n Gross.")
                else:
                    print("You don't any. There might be some food around here if you look.")
            except IndexError:
                print("Eat what?")

        if userInput.split(' ', 1)[0] == 'unlock':
            if player1.inventory.checkInventory("key"):
                print("You have successfully unlocked the cell door! Now flee!\n\n\nPress 'q' to flee.")
            else:
                print("You need a key to unlock things sillyhead.")

                          

        if userInput == 'i':
            player1.inventory.showPlayerItems()
            

if __name__ == "__main__": main ()


    
