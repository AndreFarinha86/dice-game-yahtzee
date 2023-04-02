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