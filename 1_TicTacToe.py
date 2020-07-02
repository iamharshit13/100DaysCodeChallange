# >>>> GLOBAL VARIABLES <<<<<

#Game Board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#if Game still going
game_still_going = True

#WON or TIE
winner = None

#Who's turn
current_player = "X"


#Display Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play a game of tictactoe
def play_game():

    #display initial board
    display_board()


    #while the game is still going
    while game_still_going:

        # handle a single turn of random player
        handle_turn(current_player)

        #Check if the game has ended
        check_if_game_over()


        # flip to the other player
        flip_player()

    #the game has ended
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("Tie.")


# handle a single turn of random player
def handle_turn(player):
    print(player + "'s Turn.")
    position = input("choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there. Go again")

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    #setup global variable
    global winner
    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return

def check_rows():
    #setup global variable
    global game_still_going
    #check if any of the row have same value and is not "-"
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if any row is true
    if row_1 or row_2 or row_3:
        game_still_going = False

    #return the winner
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

def check_columns():
    #setup global variable
    global game_still_going
    #check if any of the column have same value and is not "-"
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    #if any column is true
    if column_1 or column_2 or column_3:
        game_still_going = False

    #return the winner
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

def check_diagonals():
    # setup global variable
    global game_still_going
    # check if any of the diagonals have same value and is not "-"
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"

    # if any diagonals is true
    if diagonals_1 or diagonals_2 :
        game_still_going = False

    # return the winner
    if diagonals_1:
        return board[0]
    if diagonals_2:
        return board[2]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()




# board
# display board
# play game
# handle turn
# check win
    # check rows
    # check columns
    # check diagonals
# check tie
# flip player
