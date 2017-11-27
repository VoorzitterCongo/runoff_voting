import csv, sys

def import_data(file_name):
    # board_names = [x for x in input('Geef de bestuursnamen(bijv. A,B,C,E): ').strip().split(',')]
    board_names = ['A','B','C','D']
    yes_no = 'n'
    while yes_no is not 'y':
        print(board_names)
        yes_no = input("is this correct? [y/n]: ")

    f = open(file_name,'r')
    data = csv.reader(f, delimiter=',')
    dat_lst = []

    board_len = len(board_names)
    board_lst = [0] * board_len
    ballot_num = 0
    blanco_num = 0
    abst_num = 0
    for row in data:
        temp_ballot = set(row)
        print(row)
        if board_len == 1:
            if row[0] == 'bl':
                blanco_num += 1
            elif row[0] == 'oh':
                abst_num += 1
        elif board_len ==  len(temp_ballot):
            if all(board in board_names for board in row) == True:
                idx_name = board_names.index(row[0])
                board_lst[idx_name] += 1
        else:
            sys.exit('row '+str(ballot_num)+': invalid ballot')

        dat_lst.append(row)

        ballot_num += 1
    print(board_lst)
    won = get_winner(board_lst, dat_lst, ballot_num, board_names)
    if won == 2:
        print("it's a tie")
    elif won == 3:
        print('meerdere losers')
    else:
        print(won)
    return dat_lst, board_lst

def get_winner(board_lst, dat_lst, ballot_num, board_names):
    max_first = max(board_lst)
    max_loc = [i for i, b_num in enumerate(board_lst) if b_num == max_first]
    if len(max_loc) == 1 and max_first > (ballot_num / 2):
        winner = board_names[max_loc[0]]
        print(winner)
        return winner
    else:
        print(ballot_num, board_lst, board_names)
        min_first = min(board_lst)
        print('loser')
        print(min_first)
        min_loc = [i for i, b_num in enumerate(board_lst) if b_num == min_first]
        if len(board_lst) <= 2:
            # to do -> tie
            print('kom ik hier')
            return 2
        elif len(min_loc) != len(board_names):
            loser = [board for board in board_names]
            print(min_loc)
            loser = [board_names[loc] for loc in min_loc]
            # loser = board_names[min_loc]
            print('lame', loser)
            # print(loser, board_names)
            new_names = board_names
            del new_names[min_loc[0]]
            # print(new_names)
            new_board = [0] * len(new_names)

            for row in dat_lst:
                if row[0] == loser:
                    idx_new = new_names.index(row[1])
                else:
                    idx_new = new_names.index(row[0])
                new_board[idx_new] += 1
            print(new_board)
            get_winner(new_board, dat_lst, ballot_num, new_names)
        else:
            print('besturen staan gelijk', board_lst, board_names)
            return 3


import_data('test.csv')
