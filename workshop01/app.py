import flask, random
from flask import jsonify, Flask

app = Flask(__name__)
app.config["DEBUG"] = True

text = [
        {'text':'Logic will get you from A to B. Imagination will take you everywhere.'},
        {'text':"There are 10 kinds of people. Those who know binary and those who don't."},
        {'text':"There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies."},
        {'text':"It's not that I'm so smart, it's just that I stay with problems longer."},
        {'text':"It is pitch dark. You are likely to be eaten by a grue."}
        ]

@app.route('/')
def index():
    #i = random.randint(0,4)
    #result = text[i]
    # random.choice() will pick from the list with equal probability
    result = random.choice(text)
    return flask.render_template('index.html', result=result['text'])

#Creating an API, but do not need to use it
@app.route('/api/v1/getText', methods=['GET'])
def getText():
    index = random.randint(0,4)
    result = text[index]
    return jsonify(result)


if __name__ == "__main__":
	app.run()
