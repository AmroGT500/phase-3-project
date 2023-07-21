import ipdb
from cli import *

if __name__ == '__main__':
    # Create instances of the classes
    game1 = Game("Super Mario")
    game2 = Game("Minecraft")

    user1 = User("JohnDoe")
    user2 = User("JaneSmith")

    user1.own_game(game1)
    user1.own_game(game2)

    user2.own_game(game1)

    # Add more debug code here

    # Start the ipdb debugger
    ipdb.set_trace()
