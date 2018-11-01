import time
import requests

url = 'https://www.reddit.com/r/Python/comments/9qrit5/public_api_question_a_function_that_accepts_one/'
time.sleep(10)
r = requests.get(url)
time.sleep(10)
p = requests.post(url)
time.sleep(10)
with open ('test.txt', 'w') as out_put:
    time.sleep(10)
    out_put.write(r.text)
time.sleep(10)
with open ('1test.txt', 'w') as out_put:
    time.sleep(10)
    out_put.write(p.text)
time.sleep(10)

print('STOP')
# <!-- END TEMPLATE: bbcode_quote --> Место начала сообщения
# <!-- message -->