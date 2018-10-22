##Напишите программу, которая проверяет, является ли введенная строка панграммой (т.е. содержит все буквы либо русского,
##                                                                                либо английской алфавита)
##Пример русской панграммы - Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства.
##Пример английской - The quick brown fox jumps over the lazy dog
##Расширенный вариант - выводится, каких букв алфавита не хватает во фразе

##ex_text = 'Привет, как твои дкла? чего хорошего?'
print('Напишите текст: ')
ex_text = input()
ex_text = ex_text.replace(' ', '').replace('?', '').replace('-', '').lower().replace(',', '').replace('!', '')
ex_text = list(ex_text)

##print(ex_text)

abc = list()                       #создаем список из используемых букв
for a in ex_text:
    if a in abc:
        pass
    else:
        abc.append(a)
##print(abc)
        
rus_letter = list ('ёйцукенгшщзхъфывапролджэячсмитьбю') #создаем списки русского и англтийского словаря
eng_letter = list('qwertyuiopasdfghjklzxcvbnm')

what_letter = list()                     #Спискок для проверки буквы
for a in abc:
    if a in rus_letter:
        what_letter.append(True)              #если буква русская в список добавляется Тру
    elif a not in rus_letter:
        what_letter.append(False)            # если буква не русская в список добавляется Фолс
if not False in what_letter:                #   если нет фолса, т.е. все буквы руские,
    for a in rus_letter:                 
        if a in rus_letter:                #   если буква есть в списке, она из него удаляется и в конце выводится буквы не используемые в списке
            rus_letter.remove(a)              
    print('Это панагамма на русском языке, но не использованы следющие буквы: ', sorted(rus_letter))
    
if False in what_letter:                  #  если в списке есть фолс идет проверка на английский язык
    what_letter=list()
    for a in abc:
        if a in eng_letter:6
            what_letter.append(True)
        elif a not in eng_letter:
            what_letter.append(False)
            
    if not False in what_letter:           # если нет ошибок то проверятся словарь и из него удаляютс буквы используемые в фразе
        for a in eng_letter:   
            if a in eng_letter:
                eng_letter.remove(a)
        print('Это панагамма на английском языке, но не использованы следющие буквы: ', sorted(eng_letter))
    elif False in what_letter:                    # если в фразе есть ошибки, значит там и русские буквы и английские, а может и ещё какие то
        print('Я думаю это смешанная фраза')
            
        
