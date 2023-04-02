import random
#from prettytable import PrettyTable

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

#score_table()

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
                keep = input("Which dices would you like to keep? (e.g. 1,3,5 or none) then press Enter")
                if keep == "":
                    user_dice = roll_dice(num_dice)
                    print("Your dices:", user_dice)
                    break
                keep_dice = [int(k) for k in keep.split(",")]
                if len(keep_dice) != len(set(keep_dice)):
                    raise ValueError("You cannot choose the same dice more than once. Please try again.")
                if not all(0 < k <= num_dice for k in keep_dice):
                    raise ValueError("Please choose only valid dice numbers between 1 and 5 separated by commas. Please try again.")
                user_dice = [user_dice[k-1] for k in keep_dice] + roll_dice(num_dice - len(keep_dice))            
                print("keep_dice", keep_dice)
                print("Your dices:", user_dice)
                break

            except ValueError as e:
                if str(e).startswith("invalid literal for int() with base 10"):
                    print("Error: Please input only numeric values separated by commas. Please try again.")
                else:
                    print("Error:", str(e))
    print("Your Final Dices:", user_dice)
    return user_dice

user_dices()

def user_choice():
    """
    Allows the user to choose the desired category
    """
    while True:
        try:
            choice = int(input("Which Category would you like to choose? (choose only one value from 1 to 13)"))
            if not 1 <= choice <= 13:
                raise ValueError("Please choose a number between 1 and 13. Please try again.")
            break
        except ValueError as e:
            if str(e).startswith("invalid literal for int() with base 10"):
                print("Error: Please input only numeric values between 1 and 13. Please try again.")
            else:
                print("Error:", str(e))
            
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

    print(category)
    return category
    

user_choice()