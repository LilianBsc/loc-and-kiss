from flask import Blueprint, render_template, redirect, url_for, request, flash
from init import db
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/signup')
def signup():
    return render_template("signup.html")

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))

@auth.route('/dev/view-users')
def view_users():
    users = {}
    _id = 1
    while User.query.filter_by(id=_id).first():
        user = User.query.filter_by(id=_id).first()
        user = user.__repr__().split(", ")
        users[_id] = user[1:]
        _id += 1
    print(users)
    return render_template("view_db.html", table_dict=users)

@auth.route('/dev/view-users/<int:id>')
def view_users_by_id(id):
    user = db.get_or_404(User, id)
    return render_template("view_data.html", key=f"User {id}", value=user)
