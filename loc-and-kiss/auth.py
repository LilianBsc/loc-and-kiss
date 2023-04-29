from flask import Blueprint, render_template
from init import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/signup')
def singup():
    return render_template("signup.html")