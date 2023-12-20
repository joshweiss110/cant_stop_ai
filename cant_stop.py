import pandas as pd
import random


def roll_dice():
    dice_list = []
    for i in range(4):
        dice_list.append(random.randint(1,6))
    options_list = [f'{dice_list[0]+dice_list[1]}, {dice_list[2]+dice_list[3]}',
                    f'{dice_list[0]+dice_list[2]}, {dice_list[1]+dice_list[3]}',
                    f'{dice_list[0]+dice_list[3]}, {dice_list[2]+dice_list[1]}']
    return dice_list, options_list


dice_rolled, summed_options = roll_dice()
print(f'You rolled: {dice_rolled}')
print('Your options are:')
print(f'Option 1: {summed_options[0]}')
print(f'Option 2: {summed_options[1]}')
print(f'Option 3: {summed_options[2]}')
