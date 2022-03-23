print("enter num of coins:")
coins = int(input())
print("player1 please enter num:")
player1 = int(input())
# "The players can't choose a number of coins or more."
if player1 >= coins:
    print(" please enter num in range[0,coins-1]  ")
    player1 = int(input())
    coins = coins - player1
    print(" coins become: ", coins)
# The number of coins is equal to the number of played by the player - number of coins
else:
    coins = coins - player1
    print(" coins become: ", coins)
print("player2 please enter num: ")
player2 = int(input())
# The player must enter a number of coins smaller than or equal to twice the number of coins chosen by the former player
if player2 <= (2 * player1):
    coins = coins - player2
    print(" coins become: ", coins)
# The number of coins is equal to the number of played by the player - number of coins
else:
    print("please enter num <= (2*player2): ")
    player2 = int(input())
    coins = coins - player2
    print(" coins become: ", coins)
# If the number of coins == 0 becomes, the player who withdrew his last job is the winner.
if coins == 0:
    print("player2 winner")
# If the number of coins is greater than 0, the game continues.
while coins > 0:
    print("player1 please enter num: ")
    player1 = int(input())
    if player1 <= (2 * player2):
        coins = coins - player1
        print("coins become: ", coins)
    else:
        print("please enter num <= (2*player2): ")
        player1 = int(input())
        coins = coins - player1
        print("coins become: ", coins)
    # If one of the players wins, the game stops.
    if coins == 0:
        print("player1 winner")
        break
    print("player2 please enter num: ")
    player2 = int(input())
    if player2 <= (2 * player1):
        coins = coins - player2
        print("coins become: ", coins)
    else:
        print(" please enter num <= (2*player2) : ")
        coins = coins - player2
        print("coins become: ", coins)
    if coins == 0:
        cout << "player2 winner" << endl;
        break
