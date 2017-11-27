import random, csv

f = open('randvote2.csv','w')
data = csv.writer(f, delimiter=',')
asc_a = 97
for i in range(80):

    num_lst = random.sample(range(0,6), 6)
    alpha_lst = [str(chr(letter + asc_a)) for letter in num_lst]
    print(alpha_lst)
    data.writerow(alpha_lst)
