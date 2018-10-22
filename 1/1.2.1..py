num_1 = float(input('Первое число: '))
sym_0 = input('Введите знак (+;-;*:/)')
num_2 = float(input('Второе число: '))
st_1 = 1 
while st_1 > 0:
    if sym_0 == '+':
        res_0 = num_1 + num_2
        print (res_0)
        sym_0 = input('Введите знак (+;-;*:/)')
        num_1 = input('Введите число: ')
        st_1 = len(num_1)
        num_1 = float(num_1)
        num_2 = res_0
    elif sym_0 == '*':
        res_0 = num_1 * num_2
        print (res_0)
        sym_0 = input('Введите знак (+;-;*:/)')
        num_1 = input('Введите число: ')
        st_1 = len(num_1)
        num_1 = float(num_1)
        num_2 = res_0   
##    elif sym_0 == '-':
##        res_0 = num_1 - num_2
##        print (res_0)
##        sym_0 = input('Введите знак (+;-;*:/)') 
##        num_1 = input('Введите число: ')   
##    elif sym_0 == '/':
##        if num_2 == 0:
##        print('Error')
##    else:
##       res_0 = num_1 / num_2
##       print(res_0)
##       num_1 = input('Введите число: ')
##
##
##        
