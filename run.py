import random
from prettytable import PrettyTable

print("-----------------------")
print("Welcome to Yahtzee Game")
print("-----------------------\n")

def score_table():
    """
    Table that holds the points of the game
    """
    game_table = PrettyTable()

    game_table.field_names = ["Categories", "User", "Computer"]

    game_table.add_row(["Ones", 6, 11])
    game_table.add_row(["Twos", 4, 10])
    game_table.add_row(["Threes", 7, 13])
    game_table.add_row(["Fours", 7, 13])
    game_table.add_row(["Fives", 7, 13])
    game_table.add_row(["Sixes", 7, 13])
    game_table.add_row(["UPPER SCORE", 7, 13])
    game_table.add_row(["UPPER BONUS (35)", 7, 13])
    game_table.add_row(["Three of a Kind", 7, 13])
    game_table.add_row(["Four of a Kind ", 7, 13])
    game_table.add_row(["Full House (25)", 7, 13])
    game_table.add_row(["Small Straight (30)", 7, 13])
    game_table.add_row(["Large Straight (40)", 7, 13])
    game_table.add_row(["Yahtzee! (50)", 7, 13])
    game_table.add_row(["Chance", 7, 13])
    game_table.add_row(["LOWER SCORE", 7, 13])
    game_table.add_row(["TOTAL", 7, 13])

    print(game_table)


def roll_dice(num_dice):
    """
    Rolls dices and returns a list of their values
    """
    dice = [random.randint(1, 6) for i in range(num_dice)]
    return dice


def user_dices():
    """
    Allows the user to roll the dice 3 times and choose which dice to keep
    """
    num_dice = 5
    user_dice = roll_dice(num_dice)
    print("Your dices:", user_dice)
    for i in range(2):
        while True:
            try:
                keep = input("Which dices would you like to keep? (e.g. 1,3,5 or none) then press Enter\n")
                if keep == "":
                    user_dice = roll_dice(num_dice)
                    print("Your dices:", user_dice)
                    break
                keep_dice = [int(k) for k in keep.split(",")]
                if len(keep_dice) != len(set(keep_dice)):
                    raise ValueError("You cannot choose the same dice more than once. Please try again.\n")
                if not all(0 < k <= num_dice for k in keep_dice):
                    raise ValueError("Please choose only valid dice numbers between 1 and 5 separated by commas. Please try again.\n")
                user_dice = [user_dice[k-1] for k in keep_dice] + roll_dice(num_dice - len(keep_dice))            
                print("keep_dice", keep_dice)
                print("Your dices:", user_dice,"\n")
                break

            except ValueError as e:
                if str(e).startswith("invalid literal for int() with base 10"):
                    print("Error: Please input only numeric values separated by commas. Please try again.\n")
                else:
                    print("Error:", str(e), "\n")
    print("Your Final Dices:", user_dice, "\n")
    return user_dice


def computer_dices():
    """
    Calculates and returns the computer dices
    """
    num_dice = 5
    computer_dice = roll_dice(num_dice)
    print("Computer dices:", computer_dice)
    return computer_dice


def user_choice():
    """
    Allows the user to choose the desired category
    """
    while True:
        try:
            choice = int(input("Which Category would you like to choose? (choose only one value from 1 to 13)\n"))
            if not 1 <= choice <= 13:
                raise ValueError("Please choose a number between 1 and 13. Please try again.\n")
            break
        except ValueError as e:
            if str(e).startswith("invalid literal for int() with base 10"):
                print("Error: Please input only numeric values between 1 and 13. Please try again.\n")
            else:
                print("Error:", str(e), "\n")
            
    if choice == 1:
        category = "Ones"
    elif choice == 2:
        category = "Twos"
    elif choice == 3:
        category = "Threes"
    elif choice == 4:
        category = "Fours"
    elif choice == 5:
        category = "Fives"
    elif choice == 6:
        category = "Sixes"
    elif choice == 7:
        category = "Three of a Kind"
    elif choice == 8:
        category = "Four of a Kind"
    elif choice == 9:
        category = "Full House"
    elif choice == 10:
        category = "Small Straight"
    elif choice == 11:
        category = "Large Straight"
    elif choice == 12:
        category = "Yahtzee"
    elif choice == 13:
        category = "Chance"

    print("You chose:", category, "\n")
    return category
    

def calculate_score(dice):
    """
    Calculates and returns the score for each category based on the given dices
    """
    print(dice)
    category = user_choice()
    if category == "Ones":
        result = dice.count(1)
    elif category == "Twos":
        result = 2 * dice.count(2)
    elif category == "Threes":
        result = 3 * dice.count(3)
    elif category == "Fours":
        result = 4 * dice.count(4)
    elif category == "Fives":
        result = 5 * dice.count(5)
    elif category == "Sixes":
        result = 6 * dice.count(6)
    elif category == "Three of a Kind":
        if len(set(dice)) <= 3:
            result = sum(dice)
        else:
            result = 0
    elif category == "Four of a Kind":
        if len(set(dice)) <= 2:
           result = sum(dice)
        else:
            result = 0
    elif category == "Full House":
        if len(set(dice)) == 2 and (dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3):
            result = 25
        else:
            result = 0
    elif category == "Small Straight": 
        if {1, 2, 3, 4}.issubset(set(dice)) or {2, 3, 4, 5}.issubset(set(dice)) or {3, 4, 5, 6}.issubset(set(dice)):
            result = 30
        else:
            result = 0
    elif category == "Large Straight":
        if set(dice) == {1,2,3,4,5} or set(dice) == {2,3,4,5,6}:
            result = 40
        else:
            result = 0
    elif category == "Yahtzee":
        if len(set(dice)) == 1:
            result = 50
        else:
            result = 0
    elif category == "Chance":
        result = sum(dice)
    else:
        result = 0
    print(result)
    return result


def play_game():
    """
    Run all program functions.
    """
    user_dice = user_dices()
    computer_dice = computer_dices()
    #calculate_score(user_dice)
    #score_table()

play_game()