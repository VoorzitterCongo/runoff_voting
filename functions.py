import sys, csv

#TO DO
#vote log

def import_files(file_name):

    # board_names = [x for x in input('Geef de bestuursnamen(bijv. A,B,C,E): ').strip().split(',')]
    board_names = ['A','B','C','D']
    board_nums = [i for i in range(len(board_names))]
    # print(board_names)
    yes_no = 'n'
    while yes_no is not 'y':
        print(board_names)
        yes_no = input("is this correct? [y/n]: ")

    f = open(file_name,'r')
    data = csv.reader(f, delimiter=',')
    dat_lst = []

    board_num = len(board_names)
    board_lst = [[0] * board_num  for _ in range(board_num)]
    n_votes = 0
    for idx_bal, row in enumerate(data):
        dat_lst.append(row)

        for idx_board, board in enumerate(row):

            if board not in board_names:
                sys.exit('row '+str(idx_bal)+' '+board+': board name does not exist')

            idx_name = board_names.index(board)
            board_lst[idx_board][idx_name]+= 1

        n_votes += 1

    # print(board_lst)
    jeej = get_first(board_lst, dat_lst, n_votes, board_names)
    # print(jeej)
    # print(dat_lst)
    # print(board_lst)
    return board_lst, dat_lst

# def iter_data(dat_lst):

def get_first(board_lst, dat_lst, n_votes, board_names):
    max_first = max(board_lst[0])
    max_loc = [i for i, b_num in enumerate(board_lst[0]) if b_num == max_first]
    print(len(max_loc), n_votes)
    if len(max_loc) == 1 and max_first > (n_votes / 2):
        print("winner: "+str(board_names[max_loc[0]]))
        # return board_names[max_loc]

    else:
        min_first = min(board_lst[0])
        min_loc = [i for i, b_num in enumerate(board_lst[0]) if b_num == min_first]
        if len(min_loc) == 1:
            loser = board_names[min_loc[0]]
            print(loser)
            print(board_names[min_loc[0]])

        new_names = board_names.remove(loser)
        print(new_names)
        for ballot in dat_lst:
            if ballot[0] == loser:
                print('jeej')
                # ballot[1]
                idx_name = board_names.index(ballot[1])
                board_lst[idx_board][idx_name]+= 1


        # print('jeej')
def get_winner(board_lst, dat_lst, n_votes, board_names):
