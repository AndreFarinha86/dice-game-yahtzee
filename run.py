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

score_table()