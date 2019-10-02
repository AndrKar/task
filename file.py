a_list = [i for i in range(25)]
b_list = [i ** 2 for i in range(25)]

for _ in a_list:
    if _ % 2 == 0:
        print(_)


for _ in b_list:
    if _ % 2 != 0:
        print(_)
