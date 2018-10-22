import re

def open_file(file):
    try:
        with open(file) as f:
            return f.read()
    except FileNotFoundError:
        print('File not found')
nasa = open_file('nasa.txt')
# (\d{9})(/\S{1,})(\S{1,}\d$)
time_nasa =re.findall(r'(\d{9})', nasa)
url_nasa = re.findall(r'(/\S{1,})', nasa)
otvet_nasa = re.findall(r'\s\d{,3}\s(\d{0,})\s', nasa)
# print(nasa)
def my_find(text, what):
    count = 0
    for x in text:
        if x in what:
            count += 1
    return count
# print(my_find(time_nasa, nasa))
# print(my_find(url_nasa, nasa))
# print(my_find(otvet_nasa, nasa))

print('Вхождений: \n  Времени: {} \n  URL: {} \n  Ответов: {} '.format(len(time_nasa), len(url_nasa), len(otvet_nasa)))
