def create_board():
    board_dict = {}
    for i in range(2, 13):
        board_dict[i] = 0
    return board_dict


def remove_occurrences(nested_list, target):
    result = []
    for element in nested_list:
        if isinstance(element, list):
            result.append(remove_occurrences(element, target))
        elif element != target:
            result.append(element)
    return result
