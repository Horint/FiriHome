# https://www.reddit.com/r/Python/comments/9q6xtx/things_i_wish_python_did_differently/
import requests

url = 'https://www.reddit.com/r/Python/comments/9q6xtx/things_i_wish_python_did_differently'
r = requests.get(url)
p = requests.post(url)
# with open ('test.txt', 'w') as out_put:
#     out_put.write(r.text)
with open ('1test.txt', 'w') as out_put:
    out_put.write(p.text)

#
# <!-- END TEMPLATE: bbcode_quote --> Место начала сообщения
#
# <!-- message -->