pole = [' 1', ' 2',  ' 3',  ' 4', 
        ' 5' , ' 6',  ' 7',  ' 8',
        ' 9', '10', '11', '12',
        '13', '14', '15', '  ',]

res_pole = [ '1', '2',  '3',  '4', 
        '5' , '6',  '7',  '8',
        '9', '10', '11', '12',
        '13', '14',  '15', '  ']

left_border = 0, 4, 8, 12
up_border = 0, 1, 2, 3
right_border = 3, 7, 11, 15
down_border = 12, 13, 14, 15

while pole != res_pole:
   
    print('|',pole[0], '|', pole[1],'|',pole[2],'|',pole[3],'|',)
##    print('_____________________')
    print('|',pole[4],'|',pole[5],'|',pole[6],'|',pole[7],'|',)
##    print('_____________________')
    print('|',pole[8],'|',pole[9],'|',pole[10],'|',pole[11],'|',)
##    print('_____________________')
    print('|',pole[12],'|',pole[13],'|',pole[14],'|',pole[15],'|',)
    
    vod = input('Введите напрваление (up, down, left, right):')
    zero = pole.index('  ')
    
    if vod == 'left':
        if zero in left_border:
            print('Так нельзя')
        else:
            pole.remove('  ')
            pole.insert((zero-1),'  ')

    elif vod == 'up':
        if zero in up_border:
            print('Так нельзя')
        else:
            zam_index = pole[zero-4]
            pole[zero-4] = pole[zero]
            pole[zero] = zam_index

    elif vod == 'down':
        if zero in down_border:
            print('Так нельзя')
        else:
            zam_index = pole[zero+4]
            pole[zero+4] = pole[zero]
            pole[zero] = zam_index
            
    elif vod == 'right':
        if zero in right_border:
            print('Так нельзя')
        else:
            pole.remove('  ')
            pole.insert((zero+1),'  ')
            
print('Ура ты победил!')

    
    
    
    
    
    
    
    
    
    

