import os
import random

from flask import Flask
app = Flask(__name__)
app.config['RANDOM']=os.environ['FLASK_RANDOM_SEED']

random.seed(app.config['RANDOM'])


@app.route("/", methods=['GET'])
def hello():
    return os.environ['FLASK_RANDOM_SEED']

@app.route("/random", methods=['GET'])
def my_random():
    return str(random.randint(1, 100))


app.run()
