from player import Player

def playerCommands(playerInput):
    '''
    For use in main while loop. Take in player input figure out if it is an action,
    movement, or quit command. Output nothing.
    '''

def main():
    print("===================================\n         Don't Get Eaten\n===================================\n\n")

    player1 = Player()
    player_name = input('Hello?\n\nWho\'s there? ')
    player1.namePlayer(player_name)
    
    print("\n\nYou're in a scary cell ", player1.name, ". Have a nap until it goes away.\n", sep='')

    player_continue = True
    while player_continue:
        userInput = input("Press 0 to nap. ")
        if (userInput == '0'):
            player_continue = False
            
        

if __name__ == "__main__": main ()


    
