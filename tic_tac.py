print('Welcome to Tic Tac Toe')
teams = ['x', 'o']
player_one = {'name': '', 'team': '', 'choices' : []}
player_two = {'name': '', 'team': '', 'choices': []}
first_player = ''
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
occupied_cells = []

def get_player_one():
    while len(player_one['name']) < 1:
        player_one['name'] = input('Hi Player One!  Please enter your name: ')
        if len(player_one['name']) > 0:
            print('Thanks ' + player_one['name'].capitalize() + '!')
    while len(player_one['team']) < 1:
        player_one['team'] = input("Now choose your team. X's or O's? ").lower()
        if player_one['team'] not in teams:
            player_one['team'] = ''
            print('Please enter a valid team choice.  X or O...')
        if player_one['team'] == "x":
            print("You chose X's!")
            player_two["team"] = 'o'
        elif player_one['team'] == "o":
            print("You chose O's!")
            player_two["team"] = 'x'
    
def get_player_two():
    while len(player_two['name']) < 1:
        player_two['name'] = input('Now, Player 2.  What is your name? ')
    print("Thanks " + player_two["name"].capitalize() + "!")

    if player_two["team"] == "o":
        print("Since " + player_one["name"].capitalize() + " chose X's, you are playing as O's!")

    if player_two["team"] == "x":
        print("Since " + player_one["name"].capitalize() + " chose O's, you are playing as X's")
def goes_first():
    valid_player = False

    while not valid_player:
        first_player = input("Now, who goes first? ")
        if first_player == player_one["name"]:
            valid_player = True
            print("OK, " + player_one["name"].capitalize() + " will go first.")
            return player_one
        elif first_player == player_two["name"]:
            valid_player = True
            print("OK, " + player_two["name"].capitalize() + " will go first.")
            return player_two
        else:
            print("Please enter a valid player name...")
            
def choose_cell(player):
    display_game()
    row_choice = ''
    column_choice = ''

    print(player['name'].capitalize() + ", make your move.")

    while row_choice not in range(1,4):
        print("Please enter a row number from 1 - 3...")
        row_choice = int(input("Row: "))

    while column_choice not in range(1,4):
        print("Please enter a column number from 1 - 3...")
        column_choice = int(input("Column: "))

    if row_choice == 1 and column_choice == 1:
        cell = 'top-left'
        if cell in occupied_cells:
            print("Cell occupied.  Please choose another.")
            row_choice = ''
            column_choice = ''
            choose_cell(player)
        else:
            occupied_cells.append(cell)
            player["choices"].append(cell)
            row1[0] = player["team"].capitalize()

    elif row_choice == 1 and column_choice == 2:
        cell = 'top-center'
        if cell in occupied_cells:
            print("Cell occupied.  Please choose another.")
            row_choice = ''
            column_choice = ''
            choose_cell(player)
        else:
            occupied_cells.append(cell)
            player["choices"].append(cell)
            row1[1] = player["team"].capitalize()

    elif row_choice == 1 and column_choice == 3:
        cell = 'top-right'
        if cell in occupied_cells:
            print("Cell occupied.  Please choose another.")
            row_choice = ''
            column_choice = ''
            choose_cell(player)
        else:
            occupied_cells.append(cell)
            player["choices"].append(cell)
            row1[2] = player["team"].capitalize()

    elif row_choice == 2 and column_choice == 1:
        cell = 'center-left'
        if cell in occupied_cells:
            print("Cell occupied.  Please choose another.")
            row_choice = ''
            column_choice = ''
            choose_cell(player)
        else:
            occupied_cells.append(cell)
            player["choices"].append(cell)
            row2[0] = player["team"].capitalize()

    elif row_choice == 2 and column_choice == 2:
        cell = 'center-center'
        if cell in occupied_cells:
            print("Cell occupied.  Please choose another.")
            row_choice = ''
            column_choice = ''
            choose_cell(player)
        else:
            occupied_cells.append(cell)
            player["choices"].append(cell)
            row2[1] = player["team"].capitalize()

    elif row_choice == 2 and column_choice == 3:
        cell = 'center-right'
        if cell in occupied_cells:
            print("Cell occupied.  Please choose another.")
            row_choice = ''
            column_choice = ''
            choose_cell(player)
        else:
            occupied_cells.append(cell)
            player["choices"].append(cell)
            row2[2] = player["team"].capitalize()

    elif row_choice == 3 and column_choice == 1:
        cell = 'bottom-left'
        if cell in occupied_cells:
            print("Cell occupied.  Please choose another.")
            row_choice = ''
            column_choice = ''
            choose_cell(player)
        else:
            occupied_cells.append(cell)
            player["choices"].append(cell)
            row3[0] = player["team"].capitalize()

    elif row_choice == 3 and column_choice == 2:
        cell = 'bottom-center'
        if cell in occupied_cells:
            print("Cell occupied.  Please choose another.")
            row_choice = ''
            column_choice = ''
        else:
            occupied_cells.append(cell)
            player["choices"].append(cell)
            row3[1] = player["team"].capitalize()

    elif row_choice == 3 and column_choice == 3:
        cell = 'bottom-right'
        if cell in occupied_cells:
            print("Cell occupied.  Please choose another.")
            row_choice = ''
            column_choice = ''
            choose_cell(player)
        else:
            occupied_cells.append(cell)
            player["choices"].append(cell)
            row3[2] = player["team"].capitalize()

def check_for_win(player):
    print("Current Player: " + player["name"].capitalize())
    if ["top-left", "center-left", "bottom-left"] in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    elif ["top-center", "center-center", "bottom-center"] in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    elif ["top-right", "center-right", "bottom-right"] in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    elif ["top-left", "top-center", "top-right"] in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    elif ["center-left", "center-center", "center-right"] in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    elif ["bottom-left", "bottom-center", "bottom-right"] in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    elif ["top-left", "center-center", "bottom-right"] in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    elif ["top-right", "center-center", "bottom-left"] in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    else:
        return False

def display_game():
    print(row1)
    print(row2)
    print(row3)

def play_game():
    get_player_one()
    get_player_two()

    first_player = goes_first()

    if first_player == player_one:
        second_player = player_two

    elif first_player == player_two:
        second_player = player_one

    while not check_for_win(first_player) or not check_for_win(second_player):
        choose_cell(first_player)
        if check_for_win(first_player):
            display_game()
            break
    
        choose_cell(second_player)
        if check_for_win(second_player):
            display_game()
            break

def try_again():
    play_again = ''
    while play_again != "y" or "n":
        play_again = input("Would you like to play again? Please enter Y or N: ").lower()
        if play_again == "y":
            play_game()
        elif play_again == "n":
            print("Thanks for playing Tic Tac Toe.  See you next time!")
            break

play_game()
try_again()


    




    
