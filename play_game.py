from take_turn import *
from funcs import *


def start_game():
    game_continues = True
    players = []
    player_boards = {}
    ai_num = 0
    num_players = int(input('How many players are there? '))
    for i in range(1, num_players+1):
        name = input('What is your name? (For AI, type ai) ')
        if name == 'ai':
            ai_num += 1
            name = f'ai {ai_num}'
        players.append(name)
        player_boards[name] = create_board()
    random.shuffle(players)
    while game_continues:
        for player in players:
            print(f'It\'s {player}\'s turn!')
            player_boards = take_turn(player, player_boards)
            cols_completed = sum(1 for v in player_boards[player].values() if v == f'{player} Completed')
            if cols_completed >= 3:
                print(f'{player} Wins!')
                game_continues = False
                break
    print('Thanks for Playing!')


if __name__ == "__main__":
    start_game()

