from player import Player

def main():
    print("===================================\n         Don't Get Eaten\n===================================\n\n")

    player1 = Player()
    player_name = input('Enter your name: ')
    player1.namePlayer(player_name)
    
    print("\n\nYou're in a scary cell ", player1.name, ". Have a nap until it goes away.", sep='')

    player_continue = '0'
    while player_continue == '0':
        player_continue = input("Continue? ")
        

if __name__ == "__main__": main ()


    
