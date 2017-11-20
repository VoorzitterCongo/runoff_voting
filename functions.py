import sys, csv

#TO DO
#vote log

def import_files(file_name):

    # board_names = [x for x in input('Geef de bestuursnamen(bijv. A,B,C,E): ').strip().split(',')]
    board_names = ['A','B','C','D']
    print(board_names)
    yes_no = 'n'
    while yes_no is not 'y':
        yes_no = input("is this correct? [y/n]: ")

    f = open(file_name,'r')
    data = csv.reader(f, delimiter=',')
    dat_lst = []

    board_num = len(board_names)
    board_lst = [[0] * board_num  for _ in range(board_num)]

    for idx_bal, row in enumerate(data):
        dat_lst.append(row)

        for idx_board, board in enumerate(row):

            if board not in board_names:
                sys.exit('row '+str(idx_bal)+' '+board+': board name does not exist')

            idx_name = board_names.index(board)
            board_lst[idx_board][idx_name]+= 1

    print(board_lst)
    return board_lst, dat_lst

def get_first(board_lst, dat_lst):
    high_first = 0
    for index, b_num in enumerate(board_lst):
