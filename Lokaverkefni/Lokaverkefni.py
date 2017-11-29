import json
from sys import argv
from bottle import route,run,template, static_file,request,redirect,response

@route('/myndir/<nafn>')
def static(nafn):
    return static_file(nafn, root='/myndir')



@route("/")
def home():
    if request.get_cookie("visited"):
        hallo = request.get_cookie("visited")
        return template("index3.tpl",a = "Cookie")
    else:
        return template("index.tpl")


@route("/login", method = 'POST')
def index():

    username = request.forms.get('notendanafn')
    password = request.forms.get('lykilord')

    with open("users.txt","r") as f:
        users = f.read()
        users = users.split(",")
        login = False
        for a in users:
            user = a.split(":")
            if username == user[0]:
                if password == user[1]:
                    nafn = username
                    pas = password
                    login = True
        if login == True:
            response.set_cookie("visited", "welcome back to ")
            return template("index3.tpl",a = "Login",n = nafn,p = pas)
        else:
            redirect('http://localhost:8080/')
@route("/del")
def delcookie():
    response.set_cookie("visited", "", expires=0)
    return '''<h1>Cookie deleted</h1>
    <a href="/">Go to Log in</a>'''
@route("/lykil")
def lykil():

    return template('index5.tpl')
@route("/skra", method = "POST")
def skra():

    username = request.forms.get('notendanafn')
    password = request.forms.get('lykilord')

    with open("users.txt", "a") as f:
        user = ","+username+":"+password
        f.write(user)
    return '''
        <h1>Notanda hefur verið bætt við</h1>
    '''
@route("/not")
def notandi():
    return template('index4.tpl')



@route("/bilar")
def bilar():
    ioStream = open('myndir.json', 'r', encoding='utf-8')
    dData = json.load(ioStream)
    ioStream.close()
    return template('index2.tpl',gogn = dData)
run(host='localhost', port=8080, debug=True, Realoader=True)