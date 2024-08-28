import logging
from flask import Flask, render_template, request
from waitress import serve


app = Flask(__name__, template_folder=".")
logger = logging.getLogger("doms")
logging.basicConfig(filename="example.log", level=logging.INFO)
logging.getLogger('werkzeug').disabled = True

#######################################

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/", methods=['POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    if username == "dstipic" and password == "123":
        return render_template('index.html')
    else:
        return render_template('login.html')


@app.route("/founder")
def founder():
    return render_template('founder.html')

@app.route("/demo")
def demo():
    return render_template('demo.html')


if __name__ == "__main__":
    print("Starting server!")
    #erve(app, host="0.0.0.0", port=80)
    app.run(host="127.0.0.1", port=8080, debug=True)