import random
import os
import sys

def clear():
    os.system('cls')

# Function to print the mastermind board
def print_mastermind_board(name, guess_codes, guess_flags):
    print("-----------------------------------------")
    print("\t" + "Hi " + name + " Welcome to GameInt")
    print("-----------------------------------------")
    print("Number to Guess - X X X X ")
    print("Color Mapping: 1-White 2-Blue 3-Red 4-Yellow 5-Green 6-Purple")
    print("-----------------------------------------")
    print("Attempt No       " + "Guess         " + "Result")

    for i in range(len(guess_codes)):
        print("-----------------------------------------")
        print("     "+str(i + 1) + "            " +
              str(guess_codes[i][0]) + str(guess_codes[i][1]) + str(guess_codes[i][2]) + str(guess_codes[i][3]) + "          " +
              guess_flags[i][0], guess_flags[i][1])
        print("                                " + guess_flags[i][2], guess_flags[i][3])

        print()
    print("-----------------------------------------")

# The Main function
if __name__ == '__main__':

    name = input("Enter your name: ")

    print("-----------------------------------------")
    print("MAIN MENU")
    print("-----------------------------------------")
    print("1. Start the Game")
    print("2. End")
    print("-----------------------------------------")
    choice = int(input("Enter the menu number to continue: "))

    if choice == 1:

        # List of colors
        colors = ["White", "Blue", "Red", "Yellow", "Green", "Purple"]

        # Mapping of colors to numbers
        colors_map = {1: "White", 2: "Blue", 3: "Red", 4: "Yellow", 5: "Green", 6: "Purple"}

        hidden_code = []

        # Random color code generation
        for i in range(4):
            col = random.choice(colors)
            i = i + 1
            hidden_code.append(col)
        print(hidden_code)

        # Number of chances for the player
        chances = 8

        # The codes guessed by the player each turn
        guess_codes = [['.', '.', '.', '.'] for x in range(chances)]
        guess_codes_mapped = [['.', '.', '.', '.'] for x in range(chances)]

        # The clues provided to the player each turn
        guess_flags = [['.', '.', '.', '.'] for x in range(chances)]

        clear()

        # The current turn
        turn = 0

        # Game Starts here
        while turn < chances:

            print_mastermind_board(name, guess_codes, guess_flags)

            # Accepting the player input
            try:
                input_code = input("Enter your choice = ")
                code = list(map(int, input_code))
                print(hidden_code)
            # Check if the input is in the correct data type
            except ValueError:
                clear()
                print("\tWrong input! Only numbers are accepted")
                continue

            print(input_code)
            if input_code == '0000':
                clear()
                print("You have quitted the game")
                sys.exit()

            # Check if the number of colors are 4
            if len(code) != 4:
                clear()
                print("\tWrong input! Only 4 digit numbers are accepted")
                continue

            # Check if each number entered corresponds to an existing color
            flag = 0
            for x in code:
                if x > 6 or x < 0:
                    clear()
                    print("\tWrong input!! Each digit should be in the 1-6 range")
                    continue

            if flag == 1:
                clear()
                print("\tWrong input!! Each digit should be in the 1-6 range")
                continue

            # Storing the player input
            for i in range(4):
                guess_codes[turn][i] = code[i]
                guess_codes_mapped[turn][i] = colors_map[code[i]]

            # Process to apply clues according to the player input
            dummy_code = [x for x in hidden_code]

            pos = 0

            # Loop to set up clues for the player move
            for x in code:
                if colors_map[x] in dummy_code:
                    if code.index(x) == hidden_code.index(colors_map[x]):
                        guess_flags[turn][pos] = '1'
                    else:
                        guess_flags[turn][pos] = '0'
                    pos += 1
                    dummy_code.remove(colors_map[x])

            random.shuffle(guess_flags[turn])

            # Check for win condition
            if guess_codes_mapped[turn] == hidden_code:
                clear()
                print_mastermind_board(name, guess_codes, guess_flags)
                print("Congratulations!! You have won the game")
                points = (chances - turn) / chances * 100
                print("You have scored " + str(points) + "%")
                break

            # Update turn
            turn += 1
            clear()

        # Check for loss condition
        if turn == chances:
            clear()
            print_mastermind_board(name, guess_codes, guess_flags)
            print("You Lose!!")

    elif choice == 2:
        sys.exit()

    else:
        print("You have entered a wrong menu number!")
