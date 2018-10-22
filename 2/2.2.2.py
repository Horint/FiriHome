text = 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?'
l = list(text)

new_l = text.replace('?', '').replace('.', '').replace(',', '')
new_text = new_l.lower() 
new_word=new_text.split()

dict_word = {}                             # новый сорварь
for word in new_word:
    if word in dict_word:                  # каждое слово в тексте становиться ключем, значением становится 1, если оно вновь
        dict_word[word] += 1               # встречается значению +1
    else:
        dict_word[word] = 1
##
##
a = dict_word.items()                                  #делаем словрь списком
sort_word = sorted((a), key=lambda x: x[1])            #сортируем его по значению 1 индекса
print(sort_word[-10:])                                 #делаем слайс по последним 10 значениям списка