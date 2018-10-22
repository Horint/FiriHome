num_1 = input('Введите число: ')
while len(num_1) >= 0:
    sym_0 = input('Введите знак (+;-;*:/)')

    if sym_0 == '+':
    ##    print('{} + {} = '.format(num_1,num_2))
        num_1 = float(num_1)
        num_2 = float(input('Введите число'))        
        res_0 = num_1 + num_2
        print (res_0)
        num_1 = input('Введите число: ')
    elif sym_0 == '-':
        ##    print('{} + {} = '.format(num_1,num_2))
        num_1 = float(num_1)w
        res_0 = num_1 - num_2
        print (res_0)
        num_1 = input('Введите число: ')
    elif sym_0 == '*':
        ##    print('{} + {} = '.format(num_1,num_2))
        num_1 = float(num_1)
        res_0 = num_1 * num_2
        print (res_0)
        num_1 = input('Введите число: ')
    elif sym_0 == '/':
        if num_2 == 0:
            print('Error')
    else:
        num_1 = float(num_1)
        res_0 = num_1 / num_2
        print(res_0)
        num_1 = input('Введите число: ')
else:
    print(res_0)

