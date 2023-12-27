from take_turn import *
from funcs import *


def start_game():
    board = create_board()
    cols_completed = 0
    while cols_completed < 3:
        print('----------------------------------------------')
        print('Start of Turn')
        board = take_turn(board)
        cols_completed = sum(1 for v in board.values() if v == 'Complete')
    print('You Win!')


if __name__ == "__main__":
    start_game()

