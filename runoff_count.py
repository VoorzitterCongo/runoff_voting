import csv, sys

def import_data(file_name):

    # names of boards
    board_names = ['a','b','c','d','e','f']

    f = open(file_name,'r')
    data = csv.reader(f, delimiter=',')
    dat_lst = []

    board_len = len(board_names)
    board_lst = [0] * board_len
    ballot_num, blanco_num, abst_num = 0, 0, 0

    for row in data:
        ballot_num += 1
        temp_ballot = set(row)
        print('stem nr. :', ballot_num,' ',row)
        if len(temp_ballot) == 1:
            if row[0] == 'bl':
                blanco_num += 1
            elif row[0] == 'gv':
                abst_num += 1
            else:
                sys.exit('row '+str(ballot_num)+': ongeldige stem')
        elif board_len ==  len(temp_ballot) and all(board in board_names for board in row) == True:
            idx_name = board_names.index(row[0])
            board_lst[idx_name] += 1
            dat_lst.append(row)
        else:
            sys.exit('row '+str(ballot_num)+': ongeldige stem')

    cor_votes = ballot_num - blanco_num
    vot_round = 1
    won = get_winner(board_lst, dat_lst, cor_votes, board_names, vot_round)

def get_winner(board_lst, dat_lst, cor_votes, board_names, vot_round):
    max_first = max(board_lst)
    max_loc = [i for i, b_num in enumerate(board_lst) if b_num == max_first]

    if len(max_loc) == 1 and max_first > (cor_votes / 2):
        winner = board_names[max_loc[0]]
        print('bestuur met meeste stemmen:', winner,'aantal stemmen:', max_first, 'na ronde:', vot_round)
        return 1

    else:
        print(cor_votes, board_lst, board_names)
        min_first = min(board_lst)
        min_loc = [i for i, b_num in enumerate(board_lst) if b_num == min_first]
        loser_name = [board_names[loc] for loc in min_loc]
        loser_num = [board_lst[loc] for loc in min_loc]
        print('Afvallers: ', loser_name, loser_num)
        if len(board_lst) <= 2:
            print('gelijkspel: ', board_names, board_lst)
            return 2

        elif len(min_loc) != len(board_names):
            new_lst = []
            new_names = []

            for idx_lose, board in enumerate(board_names):
                if idx_lose not in min_loc:
                    print(idx_lose)
                    new_names.append(board)
                    new_lst.append(board_lst[idx_lose])

            print(new_names, new_lst)

            for row in dat_lst:
                if row[0] not in new_names:
                    for b_name in row:
                        if b_name in new_names:
                            new_lst[new_names.index(b_name)] += 1
                            break

            vot_round += 1
            get_winner(new_lst, dat_lst, cor_votes, new_names, vot_round)
        else:
            print('alle besturen staan gelijk', board_lst, board_names)
            return 3

import_data('randvote.csv')
