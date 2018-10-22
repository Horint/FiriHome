
import requests

url = 'http://starlab.ru/showthread.php?t=29557'
r = requests.get(url)

with open ('test.txt', 'w') as out_put:
    out_put.write(r.text)

<!-- END TEMPLATE: bbcode_quote --> Место начала сообщения