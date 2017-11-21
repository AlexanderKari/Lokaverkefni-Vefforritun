from bottle import route, run, request, static_file, error, template, response

@route("/")
def home():
    return template("index.tpl")
run(host='localhost', port=8080, debug=True, Realoader=True)
