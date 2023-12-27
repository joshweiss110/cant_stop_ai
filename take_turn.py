import pandas as pd
import random
import copy
from funcs import *


FULL_BOARD = {2:3, 3:5, 4:7, 5:9, 6:11, 7:13, 8:11, 9:9, 10:7, 11:5, 12:3}


def roll_dice():
    dice_rolled = []
    for i in range(4):
        dice_rolled.append(random.randint(1, 6))

    summed_options = [[dice_rolled[0] + dice_rolled[1], dice_rolled[2] + dice_rolled[3]],
                      [dice_rolled[0] + dice_rolled[2], dice_rolled[1] + dice_rolled[3]],
                      [dice_rolled[0] + dice_rolled[3], dice_rolled[2] + dice_rolled[1]]]
    return dice_rolled, summed_options


def show_dice_roll(dice_rolled, summed_options, temp_nums, board):
    print(f'You rolled: {dice_rolled}')
    print(f'Your temporary numbers are: {temp_nums}')
    for col in board:
        if isinstance(board[col], str):
            summed_options = remove_occurrences(summed_options, col)
            summed_options = [x for x in summed_options if x != []]
    open_spots = 3 - len(temp_nums)
    can_continue = False
    new_summed_options = []
    if open_spots >= 2:
        can_continue = True
        new_summed_options = summed_options
    elif open_spots == 1:
        can_continue = True
        for option in summed_options:
            overlaps = sum(el in option for el in temp_nums)
            if overlaps == 0:
                if len(option) == 1:
                    new_summed_options.append([option[0]])
                elif option[0] == option[1]:
                    new_summed_options.append(option)
                else:
                    new_summed_options.append([option[0]])
                    new_summed_options.append([option[1]])
            else:
                new_summed_options.append(option)
    elif open_spots == 0:
        for option in summed_options:
            new_option = []
            for val in option:
                if val in temp_nums:
                    new_option.append(val)
            if new_option:
                new_summed_options.append(new_option)
                can_continue = True

    if can_continue:
        print('Therefore your options are:')
        for i, new_option in enumerate(new_summed_options, 1):
            print(f'Option {i}: {new_option}')
        chosen_option = int(input('Which option would you like to choose? '))
        chosen_sums = new_summed_options[chosen_option-1]
        return chosen_sums
    else:
        print('You have no available moves :(')
        return -1


def update_board(board_dict, chosen_sums, current_player, completed_cols):
    for col in chosen_sums:
        if isinstance(board_dict[col], int):
            board_dict[col] += 1
            if board_dict[col] >= FULL_BOARD[col]:
                board_dict[col] = f'{current_player} Completed'
                completed_cols.append(col)
    return board_dict, completed_cols


def take_turn(current_player, player_boards):
    cont = 1
    temp_nums = []
    completed_cols = []
    temp_board = copy.deepcopy(player_boards[current_player])
    print(f'{current_player}\'s Board: {player_boards[current_player]}')
    for player in player_boards:
        if player != current_player:
            print(f'{player}\'s Board: {player_boards[player]}')
    while cont:
        dice_rolled, summed_options = roll_dice()
        chosen_sums = show_dice_roll(dice_rolled, summed_options, temp_nums, temp_board)
        if chosen_sums == -1:
            return player_boards
        for chosen_val in chosen_sums:
            if chosen_val not in temp_nums:
                temp_nums.append(chosen_val)
                temp_nums.sort()
        temp_board, completed_cols = update_board(temp_board, chosen_sums, current_player, completed_cols)
        print(f'Your Temporary Numbers: {temp_nums}')
        print(f'{current_player}\'s Board: {temp_board}')
        for player in player_boards:
            if player != current_player:
                print(f'{player}\'s Board: {player_boards[player]}')
        cont = int(input('To continue press 1, to end turn and save progress press 0: '))

    for player in player_boards:
        if player != current_player:
            for val in completed_cols:
                player_boards[player][val] = f'{current_player} Completed'
        else:
            player_boards[player] = temp_board
    return player_boards



