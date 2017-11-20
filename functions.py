import sys, csv

#TO DO
#vote log

# board_names = [x for x in input('Geef de bestuursnamen(bijv. A,B,C,E): ').strip().split(',')]
board_names = ['A','B','C','D']

# def import_votes(argv):
log = open('log.csv', 'w')

f = open('test.csv','r')
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
        board_lst[idx_name][idx_board]+= 1

print(board_lst)
