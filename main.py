import logging
from flask import Flask, render_template, send_file
from waitress import serve


app = Flask(__name__, template_folder=".")
logger = logging.getLogger("doms")
logging.basicConfig(filename="example.log", level=logging.INFO)
logging.getLogger('werkzeug').disabled = True

#######################################

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/founder")
def founder():
    return render_template('founder.html')

@app.route("/demo")
def demo():
    return render_template('demo.html')


if __name__ == "__main__":
    print("Starting server!")
    serve(app, host="0.0.0.0", port=80)
    #app.run(host="127.0.0.1", port=8080, debug=True)