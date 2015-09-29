#!/usr/bin/python -tt

def get_corner_array(x,y, board):
    return


def get_edge_array(x,y, board):
    return


def get_inner_array(x,y, board):
    return


def position_type(x,y, size):
    result = 'N'
    if (x == 0 and y == 0) or (x == size - 1 and y == 0)\
            or (x == size - 1 and y == size - 1) or (x == 0 and y == size - 1):
        result = 'c'
    elif (x == 0 and (y != 0 and y < size)) or (0 < x < size and y == 0)\
            or (0 < x < size and y == size - 1) or (x == size - 1 and 0 < y < size):
        result = 'e'
    elif 0 < x < size and 0 < y < size:
        result = 'i'
    return result


def main():
    print("Starting Program.....")
    board = [['O', 'S', 'D', 'L', 'P'],
             ['M', 'L', 'E', 'I', 'D'],
             ['I', 'K', 'G', 'M', 'A'],
             ['S', 'I', 'M', 'A', 'R'],
             ['E', 'U', 'N', 'P', 'Y']]
    word_lengths = [6, 7, 4, 3, 5]

    print("found array with {} x {} items".format(len(board), len(board[0])))

    position_choices = []


    for i in range(len(board)):
        for j in range(len(board[0])):
            ptype = position_type(i, j, len(board))
            if ptype == 'c':
                position_choices.append(get_corner_array(i, j, board))
            elif ptype == 'e':
                position_choices.append(get_edge_array(i, j, board))
            elif ptype == 'i':
                position_choices.append(get_inner_array(i, j, board))


if __name__ == '__main__':
    main()
