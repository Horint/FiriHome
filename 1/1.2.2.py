num_1 = float(input('Число: '))
sym_0 = input('Знак: + - * /: ')
num_2 = float(input('Число: '))

if sym_0 == '+':
    res_0 = num_1 + num_2    
elif sym_0 == '-':
    res_0 = num_1 - num_2
elif sym_0 == '*':
    res_0 = num_1 * num_2
elif sym_0 == '/':
    if num_2 == 0:
            print('Error')
    else:
        res_0 = num_1 / num_2

print(res_0)
st_1 = 1
sym_0 = input('Знак: + - * /: ')
num_3 = float(input('Число: '))
while st_1 > 0:
##    sym_0 = input('Знак: + - * /: ')
##    num_3 = float(input('Число: '))
    if sym_0 == '+':
        num_3 = float(num_3)
        res_1 = res_0 + num_3

    elif sym_0 == '-':
        num_3 = float(num_3)
        res_1 = res_0 - num_3

    elif sym_0 == '*':
        num_3 = float(num_3)
        res_1 = res_0 * num_3

    elif sym_0 == '/':
        num_3 = float(num_3)
        if num_3 == 0:
                print('Error')
                break
        else:
            num_3 = float(num_3)
            res_1 = res_0 / num_3

    print(res_1)
    res_0 = res_1
    sym_0 = input('Знак: + - * /: ')
    num_3 = input('Число: ')
    st_1 = len(sym_0)
    
print('Результат:', res_0)

    
    