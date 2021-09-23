from bottle import run, template, default_app
from bottle import get, post 
from bottle import debug
from bottle import request, response, redirect

# http://localhost:8068/.... <route> 

#######
import os 
import json
import random
import string

def new_user(username):
    user = {
        "username" : username,
    }
    os.makedirs("data/users", exist_ok=True)
    with open(f"data/users/{username}.user", 'w') as f:
        json.dump(user, f)
    return user

def load_user(username):
    try:
        os.makedirs("data/users", exist_ok=True)
        with open(f"data/users/{username}.user", 'r') as f:
            user = json.load(f)
    except Exception as e:
        print("user error:", e)
        user = new_user(username)
    print("loaded user", user)
    return user

def save_user(user):
    username = user['username']
    os.makedirs("data/users", exist_ok=True)
    with open(f"data/users/{username}.user", 'w') as f:
        json.dump(user, f)
    print("saved user", user)

def random_id():
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=16))

def new_session():
    session_id = random_id()
    session = { 'session_id':session_id }
    os.makedirs("data/sessions", exist_ok=True)
    with open(f"data/sessions/{session_id}.session", 'w') as f:
        json.dump(session, f)
    response.set_cookie('session_id',session_id)
    return session

def load_session(request):
    session_id = request.get_cookie("session_id", default=None)
    try:
        if session_id == None:
            raise Exception("No session id cookie found.")
        os.makedirs("data/sessions", exist_ok=True)
        with open(f"data/sessions/{session_id}.session", 'r') as f:
            session = json.load(f)
    except Exception as e:
        print("session error:", e)
        session = new_session()
    if username in session:
        session['user'] = load_user(username)
    else:
        session['user'] = {}

    print("loaded session", session)
    return session

def save_session(session, response):
    session_id = session['session_id']
    if 'user' in session:
        save_user(session['user'])
    os.makedirs("data/sessions", exist_ok=True)
    with open(f"data/sessions/{session_id}.session", 'w') as f:
        json.dump(session, f)
    response.set_cookie('session_id',session_id)
    print("saved session", session)

#######

@get("/")
@get("/hello")
def get_hello(name=None):
    session = load_session(request)
    print("hello loaded session",session)
    if 'username' in session:
        username = session['username']
    else:
        username = "complete stranger"
    favcolor = session.get('favcolor','not known')
    print("saving loaded session",session)
    save_session(session, response)
    return template('hello', name=username, color=favcolor)

@get("/login")
def get_login():
    session = load_session(request)
    save_session(session, response)
    return template("login", message="")

@post("/login")
def post_login():
    session = load_session(request)
    username = request.forms['username']
    favcolor = request.forms['favcolor']
    session['favcolor'] = favcolor
    #password = request.forms['password']
    #if password != "magic":
    #    response.set_cookie("session_id", session_id)
    #    save_session(response)
    #    redirect('/login')
    session['username'] = username
    session['user'] = load_user(username)
    session['user']['favcolor'] = favcolor
    save_session(session, response)
    redirect("/hello")

debug(True)
run(host="localhost", port=8068, reloader=True)
