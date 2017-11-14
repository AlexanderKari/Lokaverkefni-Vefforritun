from bottle import *

@route("/")
def home():
    return template("index.html")
run(host='localhost', port=8080, debug=True, Realoader=True)
