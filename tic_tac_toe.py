import random

board = { 'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
          'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
          'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}
lat = ['top-', 'mid-', 'bot-']
lon = ['L', 'M', 'R']

player_icon = ''
computer_icon = ''

#def reset_board():
#    for i in board.keys():
#        board[i] = ' '

def print_board():
    print(' ' + board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
    print('---+---+---')
    print(' ' + board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
    print('---+---+---')
    print(' ' + board['bot-L'] + ' | ' + board['bot-M'] + ' | ' + board['bot-R'])

def check_for_victory(is_player):
    if is_player:
        check_char = player_icon
    else:
        check_char = computer_icon
    
    # Check for horizontal rows
    for rows in range(len(lat)):
        if (board[lat[rows]+lon[0]] == check_char and
            board[lat[rows]+lon[1]] == check_char and
            board[lat[rows]+lon[2]] == check_char):
            return True
    # Check for vertical rows
    for cols in range(len(lon)):
        if (board[lat[0]+lon[cols]] == check_char and
            board[lat[1]+lon[cols]] == check_char and
            board[lat[2]+lon[cols]] == check_char):
            return True
    # Check for diagonal rows
    if (board['mid-M'] == check_char and
        ((board['top-L'] == check_char and board['bot-R'] == check_char) or
         (board['top-R'] == check_char and board['bot-L'] == check_char))):
        return True
    # No complete rows were made; return False
    return False

def player_choice():
    print('Please select where to place your piece: ', end='')
    has_played = False
    # Do not advance the app until the player has made a valid move
    while not has_played:
        choice = input() # Get input from the user
        # Validate that input is valid (i.e. has a key in the list)
        while not validate_player_input(choice):
            print('Input valid, try again: ', end='')
            choice = input()
        # Check that there is not already a piece in the chosen spot
        if check_if_played(choice):
            print('Piece has already been played in spot; select another spot: ', end='')
        else:
            board[choice] = player_icon
            has_played = True
    print_board()
    if check_for_victory(True):
        return True
    else:
        return False

def computer_choice():
    rand_row = random.randint(0,2)
    rand_col = random.randint(0,2)
    
    while check_if_played(lat[rand_row] + lon[rand_col]):
        rand_row = random.randint(0,2)
        rand_col = random.randint(0,2)
    
    board[lat[rand_row] + lon[rand_col]] = computer_icon
    print_board()
    if check_for_victory(False):
        return True
    else:
        return False

def validate_player_input(p_input):
    for i in board.keys():
        if p_input == str(i):
            return True
    return False

# Return true if there is a piece played in that spot, otherwise return false
def check_if_played(inputted_move):
    if board[inputted_move] == ' ':
        return False
    else:
        return True

# Start application
#reset_board()
print('This is a tic-tac-toe game. We\'ll flip a coin to see who goes first.')
print('Heads or tails?')
answer = input()
answer = answer.lower()
while (answer != 'heads' and answer != 'tails'):
    print('Please enter heads or tails')
    answer = input()
    answer = answer.lower()

random.seed()
coin_flip = random.randint(1,2)
if ((answer == 'heads' and coin_flip == 1) or (answer == 'tails' and coin_flip == 2)):
    print('You won the coin flip, you will to go first.')
    player_icon = 'X'
    computer_icon = 'O'
else:
    print('You lost the coin flip, you will go second.')
    player_icon = 'O'
    computer_icon = 'X'

move_count = 0
winner = None
print_board()
while move_count != 9:
    if player_icon == 'X':
        if player_choice():
            winner = 'player'
            break
        print()
        if computer_choice():
            winner = 'computer'
            break
    else:
        if computer_choice():
            winner = 'computer'
            break
        print()
        if player_choice():
            winner = 'player'
            break
    print()
    move_count += 1

# Check for a tie
if move_count == 9 and winner == None:
    print('You ended in a tie. Try again next time')
else:
    if winner == 'player':
        print('Congratulations! You won.')
    else:
        print('You lost! Better luck next time.')
