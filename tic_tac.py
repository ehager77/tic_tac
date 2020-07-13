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
    player_one["name"] = ''
    player_one["team"] = ''
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
    player_two["name"] = ''
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
    print("Current Player: " + player["name"].capitalize())
    row_choice = ''
    column_choice = ''

    print(player['name'].capitalize() + ", make your move.")

    while row_choice == '':
        print("Please enter a row number from 1 - 3...")
        row_choice = input("Row: ")
        if not row_choice.isdigit() or int(row_choice) not in range(1,4):
            print("Row selection is invalid.")
            row_choice = ''

    while column_choice == '':
        print("Please enter a column number from 1 - 3...")
        column_choice = input("Column: ")
        if not column_choice.isdigit() or int(column_choice) not in range(1,4):
            print("Column selection is invalid.")
            column_choice = ''

    if int(row_choice) == 1 and int(column_choice) == 1:
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

    elif int(row_choice) == 1 and int(column_choice) == 2:
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

    elif int(row_choice) == 1 and int(column_choice) == 3:
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

    elif int(row_choice) == 2 and int(column_choice) == 1:
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

    elif int(row_choice) == 2 and int(column_choice) == 2:
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

    elif int(row_choice) == 2 and int(column_choice) == 3:
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

    elif int(row_choice) == 3 and int(column_choice) == 1:
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

    elif int(row_choice) == 3 and int(column_choice) == 2:
        cell = 'bottom-center'
        if cell in occupied_cells:
            print("Cell occupied.  Please choose another.")
            row_choice = ''
            column_choice = ''
        else:
            occupied_cells.append(cell)
            player["choices"].append(cell)
            row3[1] = player["team"].capitalize()

    elif int(row_choice) == 3 and int(column_choice) == 3:
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
    if "top-left" in player["choices"] and "center-left" in player["choices"] and "bottom-left" in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    elif "top-center" in player["choices"] and "center-center" in player["choices"] and "bottom-center" in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    elif "top-right" in player["choices"] and "center-right" in player["choices"] and "bottom-right" in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    elif "top-left" in player["choices"] and "top-center" in player["choices"] and "top-right" in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    elif "center-left" in player["choices"] and "center-center" in player["choices"] and "center-right" in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    elif "bottom-left" in player["choices"] and "bottom-center" in player["choices"] and "bottom-right" in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    elif "top-left" in player["choices"] and "center-center" in player["choices"] and "bottom-right" in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    elif "top-right" in player["choices"] and "center-center" in player["choices"] and "bottom-left" in player["choices"]:
        print(player["name"].capitalize() + " wins!")
        return True
    elif len(occupied_cells) == 9:
        print("Stalemate.  You're both losers!!")
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

    while True:
        choose_cell(first_player)
        if check_for_win(first_player):
            display_game() 
            break
    
        choose_cell(second_player)
        if check_for_win(second_player):
            display_game() 
            break

def reset_game():
    for i in range(len(row1)):
        row1[i] = ' '
    for i in range(len(row2)):
        row2[i] = ' '
    for i in range(len(row3)):
        row3[i] = ' '
    occupied_cells.clear()
    player_one["choices"].clear()
    player_two["choices"].clear()

def try_again():
    play_again = ''
    while play_again != "y" or "n":
        play_again = input("Would you like to play again? Please enter Y or N: ").lower()
        if play_again == "y":
            reset_game()
            play_game()
        elif play_again == "n":
            print("Thanks for playing Tic Tac Toe.  See you next time!")
            break

play_game()
try_again()


    




    
