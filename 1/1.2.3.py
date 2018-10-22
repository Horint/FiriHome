num_0 = float(input('Число: '))
num_1= input('Действие: ')
num_2 = float(input('Число: '))

if num_1 == '+':
    res_0 = num_0 + num_2 #
elif num_1 == '-':
    res_0 = num_0 - num_2
elif num_1 == '*':
    res_0 = num_0 * num_2
elif num_1 == '/':
    if num_2 == 0:
            print('Error')
    else:
        res_0 = num_0 / num_2

print('Промежуточный результат', res_0)

st_0 = 1
while st_0 > 0:
    num_3 = input('Действие: ')
    if len(num_3) != '\n':
        if num_3 == '+':
            num_4 = float(input('Число: '))
            res_1 = res_0 + num_4
        elif num_3 == '-':
            num_4 = float(input('Число: '))
            res_1 = res_0 - num_4
        elif num_3 == '*':
            num_4 = float(input('Число: '))
            res_1 = res_0 * num_4
        elif num_3 == '/':
            num_4 = float(input('Число: '))
            if num_4 == 0:
                    print('Error')
                    break
            else:
                res_1 = res_0 / num_4
        res_0 = res_1
        print('Промежуточный результат', res_1)
    else:
        st_0 = 0
print('Результат', res_1)
    