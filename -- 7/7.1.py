# шалаш, мадам, а роза упала на лапу азора
##if my_list == my_list[::-1]: 
##    print(True)
##else:
##    print(False)

my_list = '1шалаш2'
a = list(map(str, my_list))

c = list(map(lambda x, y: x[y], my_list, list(range(len((my_list))))))
##print(list(range(len((my_list)))))

##a =list(map(lambda x: x[::-1], range(len((my_list)))))