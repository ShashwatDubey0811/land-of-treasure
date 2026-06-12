
## AdventureGame.py

while True:
    print('Welcome to the game of land!')
    print("Your mission is to find the treasure")
    direction = input("You are at a cross road where do you wanna go?\n " \
                      "Type 'left' or 'right.': ").lower()
    if direction == "right":
        print("You fell into a hole. Game over.")
    elif direction == "left":
        choice = input("You\'ve come to a lake.'"
                       "There is an island!! \n"
                       "Type wait to wait for a boat. "
                       "Type swim to swim across.: ").lower()
        if choice == "swim":
            print("You drowned into a mudhole Game over.")
        elif choice == "wait":
            print("Which Door?: ")
            door = input("you arrive at the island unharmed "
                         "There is a house with 3 doors "
                         "One Red, One Blue and One Yellow? "
                         "Which color do you choose?: ").lower()
            if door == "red":
                print("It's a Room full of Fire. Game over.")
            elif door == "blue":
                print("You are Attacked by a Demon. Game over.")
            elif door == "yellow":
                print("YOU Found the Treasure. You Win!!!")
            
    else:
    
        print("Invalid Operation.Game Over!!")
    
    again = input("\nDo you want to play again? Type 'yes' or 'no': ").lower()
    if again != "yes":
        print("Thanks for playing. Goodbye!")
        break