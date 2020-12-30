import random


def display_game(board):
    print("\n"*100)
    print("Hello Giorgi, your new Project -  play X-O \n")
    print('--Example of positions--')

    print('   ' + "|" + '   ' + "|" + '  ')
    print(' 7 ' + "|" + ' 8 ' + "|" + ' 9 ')
    print('   ' + "|" + '   ' + "|" + '  ')
    print('-----------')
    print('   ' + "|" + '   ' + "|" + '  ')
    print(' 4 ' + "|" + ' 5 ' + "|" + ' 6 ')
    print('   ' + "|" + '   ' + "|" + '  ')
    print('-----------')
    print('   ' + "|" + '   ' + "|" + '  ')
    print(' 1 ' + "|" + ' 2 ' + "|" + ' 3 ')
    print('   ' + "|" + '   ' + "|" + '  ')
    print('-----------\n \n')
    print('-----------')
    print('   ' + "|" + '   ' + "|" + '  ')
    print(' ' + board[7] + " | " + board[8] + " | " + board[9] + ' ')
    print('   ' + "|" + '   ' + "|" + '  ')
    print('-----------')
    print('   ' + "|" + '   ' + "|" + '  ')
    print(' ' + board[4] + " | " + board[5] + " | " + board[6] + ' ')
    print('   ' + "|" + '   ' + "|" + '  ')
    print('-----------')
    print('   ' + "|" + '   ' + "|" + '  ')
    print(' ' + board[1] + " | " + board[2] + " | " + board[3] + ' ')
    print('   ' + "|" + '   ' + "|" + '  ')
    print('-----------\n')


def play_again():
    while True:
        ans = input("Play again: Y/N ")
        if ans.upper() == "N":
            return True
        elif ans.upper() == "Y":
            return False
        else:
            continue


def player_choice(player):
    marker = ""
    if marker != "X" or marker != "O":
        while True:
            marker = input(f"{player} choose X or O :  ").upper()
            if marker == 'X' or marker == 'O':
                break
            else:
                print("Not Correct choice! Try again")
    if marker == "X":
        return 'X'
    return 'O'


# ცარიელია თუ არა უჯრა
def space_check(board, pos):
    if board[pos] == ' ':
        return True
    else:
        return False


# მოთამაშე ირჩევს უჯრას შესავსებად
def player_pos(board):
    while True:
        pos = input("Please Enter Your position choice from 1  to 9: ")
        if pos.isdigit() and int(pos) in range(1, 10) and space_check(board, int(pos)):
            return int(pos)


# არჩეულ ადგილზე ვსვავთ შესაბამის მარკერს
def place_marker(board, marker, pos):
    board[pos] = marker


# ვამოწმებთ მოგებული ხომ არაა ვინც სვლა გააკეთა
def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))


# ვინ იწყებს პირველი
def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


# თუ მოგება არაა და დაფა შევსებულია, ესე იგი ფრეა.
def full_board(board):
    for i, elem in enumerate(board):
        if board[i] == ' ':
            return False
    return True
