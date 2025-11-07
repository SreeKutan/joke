from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)



@app.route('/')
def index():
    joke= None
    return render_template('index.html', joke=joke)

@app.route('/get-joke', methods=['GET'])
def get_joke():
    url ="https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    print(response.json())
    joke = response.json()
    joke= joke['setup'] + joke['punchline']
    return render_template('index.html', joke=joke)


if __name__ == '__main__':
    app.run(debug=True)
