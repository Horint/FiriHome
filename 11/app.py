import random

from flask import Flask, request

seed = 100

app = Flask(__name__)

random.seed(seed)

NUMBER = random.randint(1, 100)


@app.route("/", methods=["GET"])
def index():
    global NUMBER
    NUMBER = random.randint(1, 100)
    return "Число загадано"


@app.route("/guess", methods=["POST"])
def guess():
    global NUMBER
    # user_number = request.form["number"] #если ключа нет,то будет исключение KeyError

    user_number = request.form.get("number", default=None)
    if user_number is not None:
        user_number = int(user_number)

        if user_number > NUMBER:
            return ">"
        elif user_number < NUMBER:
            return "<"
        else:
            NUMBER = random.randint(1, 100)
            return "="
    else:
        return "Please add into form data value with key 'number'"



# a = 100
#
# s = "(" + str(a) + ")"
# s = "({})".format(a)
# s = "(%d)" % (a)
# s = f"({a})"



if __name__ == '__main__':
    app.run()
