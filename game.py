from func import *
# display_game, play_again, player_choice, player_pos, place_marker

print("\nHello Players, Welcome in Tic-Toc!\n")
game_on = True

while game_on:
    board = [" "] * 10
    board[0] = 'tic-toc'
    player = choose_first()
    print(f'Game begin {player}\n')
    mark = player_choice(player)
    print(f'{player} choose {mark} marker.')
    display_game(board)

    while True:
        print(f'{player} choose position\n')
        pos = player_pos(board)
        print(pos)
        print(player)
        print(mark)

        place_marker(board, mark, pos)
        display_game(board)

        if win_check(board, mark):
            print(f"Congratulation, {player} win Game!\n")
            break
        if full_board(board):
            print('Game is Pie!\n')
            break

        if player == "Player 1":
            player = "Player 2"
        else:
            player = "Player 1"
        if mark == 'X':
            mark = 'O'
        else:
            mark = 'X'

    if play_again():
        game_on = False

print("\nGood Day!")
