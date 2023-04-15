import random
from prettytable import PrettyTable # import prettytable package to print a table
from tabulate import tabulate # import tabulate package to print a table


## Define a class named textstyle that contains a set of color codes for style text
class textstyle:
    PURPLE = '\033[95m' # purple color
    RED = '\033[91m'    # red color
    YELLOW = '\033[93m' # yellow color
    CYAN = '\033[96m'   # cyan color
    GREEN = '\033[92m'  # green color
    BOLD = '\33[1m'     # bold text
    ITALIC = '\33[3m'   # italicized text
    REDBG = '\33[41m'   # red background
    GREENBG = '\33[42m'  # green background
    BLUEBG = '\33[44m'     # blue background
    UNDERLINE = '\033[4m' # underlined text

    ENDC = '\33[0m' # reset to default color


# list that holds all game categories
categories = ["(1) Ones", 
              "(2) Twos", 
              "(3) Threes", 
              "(4) Fours", 
              "(5) Fives", 
              "(6) Sixes", 
              "(7) Three of a Kind", 
              "(8) Four of a Kind", 
              "(9) Full House (25)", 
              "(10) Small Straight (30)", 
              "(11) Large Straight (40)", 
              "(12) Yahtzee! (50)", 
              "(13) Chance"]

# game_scores dictionary that holds user and computer scores
game_scores = {"(1) Ones":["",""], 
               "(2) Twos":["",""], 
               "(3) Threes":["",""], 
               "(4) Fours":["",""], 
               "(5) Fives":["",""], 
               "(6) Sixes":["",""],
               "UPPER SCORE":[0,0],
               "UPPER BONUS (35)":[0,0],
               "(7) Three of a Kind":["",""],
               "(8) Four of a Kind":["",""], 
               "(9) Full House (25)":["",""], 
               "(10) Small Straight (30)":["",""], 
               "(11) Large Straight (40)":["",""], 
               "(12) Yahtzee! (50)":["",""],
               "(13) Chance":["",""],
               "LOWER SCORE":[0,0],
               "TOTAL":[0,0]
               }


def game_title():
    """
    Prints game title when called
    """
    print(textstyle.YELLOW + "-----------------------" + textstyle.ENDC)
    print(textstyle.BOLD + textstyle.ITALIC + textstyle.YELLOW + "Welcome to Yahtzee Game" + textstyle.ENDC)
    print(textstyle.YELLOW + "-----------------------" + textstyle.ENDC)


def game_rules():
    """
    Allows user to view game rules if desired
    """
    while True:
        try:
            rules = input("Would you like to see the game rules? Choose (y/n) then press Enter:")
            print("")
            if rules.lower() not in ['y', 'n']:
                raise ValueError("Please choose only y or n. Please try again.")
            break

        except ValueError as e:
                print(textstyle.REDBG + "Error:", str(e) + textstyle.ENDC,"\n")

    if rules.lower() == "y":
        print("Objective:")
        print("Score as many points as possible by rolling dice to reach the 13 combinations predefined in the game.\n")
        print("Game Play:")
        print("Dice can be rolled up to three times each in a turn to make one of the possible scoring combinations.")
        print("The game consists of rounds during which the player chooses which scoring combination to use in that round.")
        print("Once a combination is used in the game, it cannot be used again.")
        print("Player can select dice after first or second roll, and must score after third roll.")
        print("After the first and second roll player can save the dice by choosing each dice (1 to 5) that desires to keep") 
        print("and which ones want to throw in the spots.") 
        print("Dice that are set aside from the previous rolls can be taken out and re-rolled again.") 
        print("The game ends when all categories have been scored.") 
        print("The winner is the one who scores the most points.\n") 
        print("Categories\combinations:")
        print("There are thirteen predefined categories in Yahtzee game, each with its own unique scoring rules:")
        print("(1) Ones to (6) sixes: It scores the sum of these specific dice number only.")
        print("Three and Four of a kind: It scores the sum of all the dice.")
        print("Full house: Three of a kind & a pair|25 points.")
        print("small straight: 4 consecutive dice|30 points")
        print("Large straight: 5 consecutive dice|40 points")
        print("Yatzy: 5 dice with same number|50 points")
        print("Chance: Scores the sum of all dice\n")
        print("GOOD LUCK!\n")
        input("Press Enter to leave game rules.")
        clear_terminal()
        game_rules()


def get_user_name():
    """
    Allows the user to input their name and stores it in the 'user_name' variable.
    """
    while True:
        try:
            user_name = input("Please enter your name: ")
            print("")
            if user_name == "":
                raise ValueError("Please add some text. Please try again.")
            break

        except ValueError as e:
                print(textstyle.REDBG + "Error:", str(e) + textstyle.ENDC,"\n")

    return user_name


def assign_scores(user_category, user_score, computer_category, computer_score, user_dice):
    """
     Updates the game scores for the user and computer based on the chosen category and scores.
    """
    
    game_scores[user_category][0] = user_score
    game_scores[computer_category][1] = computer_score
    
    
    upper_score_user = sum(game_scores[key][0] for key in ["(1) Ones", "(2) Twos", "(3) Threes", "(4) Fours", "(5) Fives", "(6) Sixes"] if game_scores[key][0])
    upper_score_computer = sum(game_scores[key][1] for key in ["(1) Ones", "(2) Twos", "(3) Threes", "(4) Fours", "(5) Fives", "(6) Sixes"] if game_scores[key][1])

    upper_bonus_user = 0
    upper_bonus_computer = 0

    if upper_score_user >= 63:
        game_scores["UPPER BONUS (35)"][0] = 35
        upper_bonus_user = 35
    if upper_score_computer >= 63:
        game_scores["UPPER BONUS (35)"][1] = 35
        upper_bonus_computer = 35
    lower_score_user = sum(game_scores[key][0] for key in ["(7) Three of a Kind","(8) Four of a Kind","(9) Full House (25)","(10) Small Straight (30)","(11) Large Straight (40)","(12) Yahtzee! (50)","(13) Chance"] if game_scores[key][0])
    lower_score_computer = sum(game_scores[key][1] for key in ["(7) Three of a Kind","(8) Four of a Kind","(9) Full House (25)","(10) Small Straight (30)","(11) Large Straight (40)","(12) Yahtzee! (50)","(13) Chance"] if game_scores[key][1])
    total_user = upper_score_user + upper_bonus_user + lower_score_user
    total_computer = upper_score_computer + upper_bonus_computer + lower_score_computer

    game_scores["UPPER SCORE"][0] = upper_score_user
    game_scores["UPPER SCORE"][1] = upper_score_computer
    game_scores["LOWER SCORE"][0] = lower_score_user
    game_scores["LOWER SCORE"][1] = lower_score_computer
    game_scores["TOTAL"][0] = total_user
    game_scores["TOTAL"][1] = total_computer

    return game_scores


def clear_terminal():
    """Clears the terminal screen."""
    print("\033c", end="")
    game_title()


def score_table(game_scores, user):
    """
    Table that displays the user and computer game scores
    """

    clear_terminal()

    game_table = PrettyTable()

    game_table.field_names = ["Categories", f"{user}", "Computer"]

    for category, scores in game_scores.items():
        game_table.add_row([category, scores[0], scores[1]])

    print(game_table)


def roll_dice(num_dice):
    """
    Rolls dice and returns a list of their values
    """
    dice = [random.randint(1, 6) for i in range(num_dice)]
    return dice


def user_dices():
    """
    Allows the user to roll the dice 3 times and choose which dice to keep
    """
    num_dice = 5
    user_dice = roll_dice(num_dice)
    print("Your dice:", user_dice)
    for i in range(2):
        while True:
            try:
                keep = input("Which dice would you like to keep? (e.g. 1,3,5 or none) then press Enter\n")
                if keep == "":
                    user_dice = roll_dice(num_dice)
                    print("Your dice:", user_dice)
                    break
                keep_dice = [int(k) for k in keep.split(",")]
                if len(keep_dice) != len(set(keep_dice)):
                    raise ValueError("You cannot choose the same dice more than once. Please try again.")
                if not all(0 < k <= num_dice for k in keep_dice):
                    raise ValueError("Please choose only valid dice numbers between 1 and 5 separated by commas. Please try again.")
                user_dice = [user_dice[k-1] for k in keep_dice] + roll_dice(num_dice - len(keep_dice))            
                print("keep_dice", keep_dice)
                print("Your dice:", user_dice,"\n")
                break

            except ValueError as e:
                if str(e).startswith("invalid literal for int() with base 10"):
                    print(textstyle.REDBG + "Error: Please input only numeric values separated by commas. Please try again." + textstyle.ENDC,"\n")
                else:
                    print(textstyle.REDBG + "Error:", str(e) + textstyle.ENDC,"\n")
    print("Your Final Dice:", user_dice, "\n")
    return user_dice


def computer_dices():
    """
    Calculates and returns the computer dice
    """
    num_dice = 5
    computer_dice = roll_dice(num_dice)
    print("Computer dice:", computer_dice, "\n")
    return computer_dice


def user_choice(dice):
    """
    Allows the user to choose the desired category
    """
    while True:
        try:
            choice = int(input("Which Category would you like to choose? (choose only one value from 1 to 13 for unscored categories!)\n"))
            if not 1 <= choice <= 13:
                raise ValueError("Please choose a number between 1 and 13. Please try again.")
            break
        except ValueError as e:
            if str(e).startswith("invalid literal for int() with base 10"):
                print(textstyle.REDBG + "Error: Please input only numeric values between 1 and 13. Please try again." + textstyle.ENDC,"\n")
            else:
                print(textstyle.REDBG + "Error:", str(e) + textstyle.ENDC,"\n")
            
    if choice == 1:
        user_category = "(1) Ones"
    elif choice == 2:
        user_category = "(2) Twos"
    elif choice == 3:
        user_category = "(3) Threes"
    elif choice == 4:
        user_category = "(4) Fours"
    elif choice == 5:
        user_category = "(5) Fives"
    elif choice == 6:
        user_category = "(6) Sixes"
    elif choice == 7:
        user_category = "(7) Three of a Kind"
    elif choice == 8:
        user_category = "(8) Four of a Kind"
    elif choice == 9:
        user_category = "(9) Full House (25)"
    elif choice == 10:
        user_category = "(10) Small Straight (30)"
    elif choice == 11:
        user_category = "(11) Large Straight (40)"
    elif choice == 12:
        user_category = "(12) Yahtzee! (50)"
    elif choice == 13:
        user_category = "(13) Chance"

    print("You chose:", user_category)
    print("With score:", calculate_score(dice, user_category),"\n")
    return user_category


def user_category_check(dice):
    """
    Checks if the chosen category has already been scored.
    """
    
    user_category = user_choice(dice)
    
    while True:
        try:
            if game_scores[user_category][0] != "":
                raise ValueError("This category has already been scored. Please choose another category.")
            break
        except ValueError as e:
                print(textstyle.REDBG + "Error:", str(e) + textstyle.ENDC,"\n")
                user_category = user_choice(dice)
    
    return user_category


def calculate_score(dice, category):
    """
    Calculates and returns the score for each category based on the given dice
    """
    if category == "(1) Ones":
        result = dice.count(1)
    elif category == "(2) Twos":
        result = 2 * dice.count(2)
    elif category == "(3) Threes":
        result = 3 * dice.count(3)
    elif category == "(4) Fours":
        result = 4 * dice.count(4)
    elif category == "(5) Fives":
        result = 5 * dice.count(5)
    elif category == "(6) Sixes":
        result = 6 * dice.count(6)
    elif category == "(7) Three of a Kind":
        if len(set(dice)) <= 3:
            result = sum(dice)
        else:
            result = 0
    elif category == "(8) Four of a Kind":
        if len(set(dice)) <= 2:
           result = sum(dice)
        else:
            result = 0
    elif category == "(9) Full House (25)":
        if len(set(dice)) == 2 and (dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3):
            result = 25
        else:
            result = 0
    elif category == "(10) Small Straight (30)": 
        if {1, 2, 3, 4}.issubset(set(dice)) or {2, 3, 4, 5}.issubset(set(dice)) or {3, 4, 5, 6}.issubset(set(dice)):
            result = 30
        else:
            result = 0
    elif category == "(11) Large Straight":
        if set(dice) == {1,2,3,4,5} or set(dice) == {2,3,4,5,6}:
            result = 40
        else:
            result = 0
    elif category == "(12) Yahtzee! (50)":
        if len(set(dice)) == 1:
            result = 50
        else:
            result = 0
    elif category == "(13) Chance":
        result = sum(dice)
    else:
        result = 0
    return result


def display_score(dice):
    """
    Display all possible non-null scores
    """
    unscored_categories = [category for category in categories if game_scores[category][0] == ""]

    scores = []
    for category in unscored_categories:
        score = calculate_score(dice, category)
        if score != 0:
            scores.append([category, score])
    if scores:
        print(textstyle.BLUEBG + "Possible Scores:" + textstyle.ENDC)
        print(tabulate(scores, headers=["Category", "Score"]),"\n")
    else:
        print(textstyle.BLUEBG + "All possible scores are 0, please choose one of the unscored categories!" + textstyle.ENDC ,"\n")


def computer_choice(dice):
    """
    Generates a computer score based on the unscored categories with the highest expected score
    """
    computer_score = -1
    computer_category = None

    unscored_categories = [category for category in categories if game_scores[category][1] == ""]
    
    for category in unscored_categories:
        score = calculate_score(dice, category)
        if score > computer_score:
           computer_score = score
           computer_category = category
    
    print("Computer chose: " + textstyle.UNDERLINE + f"{computer_category}" + textstyle.ENDC + " | With score: " + textstyle.UNDERLINE + f"{computer_score}" + textstyle.ENDC + "\n")
    return computer_category


def end_game(user):
    """
    Ends the game by printing the final scores and a message indicating the winner.
    """

    print(textstyle.BOLD + textstyle.GREENBG + "Game over!" + textstyle.ENDC,"\n")
    computer_final_score = game_scores["TOTAL"][1]
    user_final_score = game_scores["TOTAL"][0]
    if user_final_score > computer_final_score:
        print(f"Congratulations {user}! You won! with score: " + textstyle.UNDERLINE + f"{user_final_score}" + textstyle.ENDC + ".\n")
    elif user_final_score < computer_final_score:
        print("Computer won with score: " + textstyle.UNDERLINE + f"{computer_final_score}" + textstyle.ENDC + ". Better luck next time!\n")
    else:
        print("It's a tie!\n")


def restart_game():
    input("Press Enter to restart game.")
    play_game()


def play_game():
    """
    Run all program functions.
    """
    clear_terminal()
    game_rules()
    user = get_user_name()

    for round_num in range(len(categories)):
        print(textstyle.BOLD + textstyle.PURPLE + f"Round {round_num + 1}\n" + textstyle.ENDC)

        # Computer's turn
        print(textstyle.CYAN + "It's the computer's turn.\n" + textstyle.ENDC)
        computer_dice = computer_dices()
        computer_category = computer_choice(computer_dice)
        computer_score = calculate_score(computer_dice, computer_category)

        # User's turn
        print(textstyle.GREEN + f"{user}, It's your turn!\n" + textstyle.ENDC)
        user_dice = user_dices()
        display_score(user_dice)
        user_category = user_category_check(user_dice)
        user_score = calculate_score(user_dice, user_category)

        # Display scores
        game_scores = assign_scores(user_category, user_score, computer_category, computer_score, user_dice)
        score_table(game_scores, user)
        print("\n")

    end_game(user)
    restart_game()

play_game()