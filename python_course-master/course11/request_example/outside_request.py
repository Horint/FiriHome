from flask import Flask, request
import os

app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config['SECRET_KEY'] = os.environ['S']

app.config.update(
    DEBUG=True,
    #SECRET_KEY=os.environ['S'],
)




@app.route('/', methods=['GET', 'POST'])
def home():
    return 'hello world!', 200

#print(request, type(request), request.method)

# with app.test_request_context('/test'):
#     print(request, type(request), request.method)


if __name__ == '__main__':
    app.run()
