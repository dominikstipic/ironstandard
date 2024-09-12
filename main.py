import logging
from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__, template_folder=".")
logger = logging.getLogger("doms")
logging.basicConfig(filename="example.log", level=logging.INFO)
logging.getLogger('werkzeug').disabled = True

CERT_PATH = "/etc/letsencrypt/live/ironstandard.org"
private_key = f"{CERT_PATH}/privkey.pem"
cert_key = f"{CERT_PATH}/cert.pem"

#######################################

LOGIN = 0

def check_auth(page):
    if LOGIN == 0:
        return render_template('login.html')
    else:
        return render_template(page)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    global LOGIN
    LOGIN = 0
    return render_template('login.html')

@app.route("/", methods=['POST', "GET"])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "dstipic" and password == "123":
            global LOGIN
            LOGIN = 1
            return render_template('index.html')
        else:
            return render_template('login.html')
    else:
        return check_auth("index.html")


@app.route("/founder")
def founder():
    return check_auth("founder.html")

@app.route("/demo")
def demo():
    return check_auth("demo.html")

if __name__ == "__main__":
    print("Starting server!")
    CERT_PATH = "/etc/letsencrypt/live/ironstandard.org"
    private_key = f"{CERT_PATH}/privkey.pem"
    cert_key = f"{CERT_PATH}/cert.pem"

    app.run(host='0.0.0.0', port=443, ssl_context=(cert_key,  private_key))
    #app.run(host="127.0.0.1", port=8080, debug=True)