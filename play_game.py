from take_turn import *
from funcs import *


def start_game():
    bot_game = True
    num_games = 100000
    sum_turns = 0

    for game_num in range(num_games):
        game_continues = True
        players = []
        player_boards = {}
        ai_num = 0
        turns = 0

    # Getting the player info
        if not bot_game:
            num_players = int(input('How many players are there? '))
            for i in range(1, num_players+1):
                name = input('What is your name? (For AI, type ai) ')
                if name == 'ai':
                    ai_num += 1
                    name = f'ai {ai_num}'
                players.append(name)
                player_boards[name] = create_board()
            random.shuffle(players)
        else:
            players.append('ai 1')
            player_boards['ai 1'] = create_board()

        # Starting the game
        while game_continues:
            turns += 1
            for player in players:
                # print(f'It\'s {player}\'s turn!')
                player_boards = take_turn(player, player_boards)
                cols_completed = sum(1 for v in player_boards[player].values() if v == f'{player} Completed')
                if cols_completed >= 3:
                    # print(f'{player} Wins!')
                    game_continues = False
                    break
        # print('Thanks for Playing!')
        print(f'Game number {game_num} was {turns} turns')
        sum_turns += turns
    avg_turns = sum_turns/num_games
    print(f'{avg_turns} average turns')


if __name__ == "__main__":
    start_game()

