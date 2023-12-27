from take_turn import *
from funcs import *


def start_game():
    board = create_board()
    game_continues = True
    players = []
    cols_completed = {}
    num_players = int(input('How many players are there?'))
    for i in range(1, num_players+1):
        name = input('What is your name?')
        players.append(name)
        cols_completed[name] = 0
    while game_continues:
        for player in players:
            print(f'It\'s {player}\'s turn!')
            board = take_turn(player, board)
        cols_completed = sum(1 for v in board.values() if v == 'Complete')
    print('You Win!')


if __name__ == "__main__":
    start_game()

