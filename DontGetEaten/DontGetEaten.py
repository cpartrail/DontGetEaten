from player import Player

def main():
    player_continue = '0'

    player1 = Player()
    player_name = input('Enter your name: ')
    player1.namePlayer(player_name)
    
    print("You're in a scary cell ", player1.name, ". Have a nap until it goes away.", sep='')

    while player_continue == '0':
        player_continue = input("Continue? ")
        

if __name__ == "__main__": main ()


    
