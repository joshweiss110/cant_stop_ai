import pandas as pd
import random
import copy
from funcs import *


FULL_BOARD = {2:3, 3:5, 4:7, 5:9, 6:1, 7:3, 8:1, 9:9, 10:7, 11:5, 12:3}


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
        if board[col] == 'Complete':
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
        chosen_option = int(input('Which option would you like to choose?\n'))
        chosen_sums = new_summed_options[chosen_option-1]
        return chosen_sums
    else:
        print('You have no available moves :(')
        return -1


def update_board(board_dict, chosen_sums):
    for val in chosen_sums:
        if board_dict[val] != 'Complete':
            board_dict[val] += 1
            if board_dict[val] >= FULL_BOARD[val]:
                board_dict[val] = 'Complete'
    return board_dict


def take_turn(board):
    cont = 1
    temp_nums = []
    orig_board = copy.deepcopy(board)
    print('The Current Board is:')
    print(board)
    while cont:
        dice_rolled, summed_options = roll_dice()
        chosen_sums = show_dice_roll(dice_rolled, summed_options, temp_nums, board)
        if chosen_sums == -1:
            print('orig board is')
            print(orig_board)
            return orig_board
        for chosen_val in chosen_sums:
            if chosen_val not in temp_nums:
                temp_nums.append(chosen_val)
                temp_nums.sort()
        board = update_board(board, chosen_sums)
        print(f'This is the new board:\n{board}')
        cont = int(input('To continue press 1, to save progress press 0\n'))
    return board


if __name__ == "__main__":
    take_turn(create_board())

