from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
# this is so that you can hash the password
# hashing function is a function that has no inverse, 
# one that you can't map back to get back the original (here, password)
# You can only check if the password that you typed in is correct or not
# if it matches the password that was originally present.
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
# by default, get is there so don't need to mention it exclusively.
def login():
    # return "<p>Login</p>"
    # data = request.form
    # print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user is not None:
            if check_password_hash(user.password, password):
                flash('Log in successful.', category='success')
                login_user(user, remember=True)
                # remember = True remembers that the user is logged in until the user closes his browser or session
                # it stores it in the flash session. As long as the web server is running, will run.
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password. Try again.', category='error')
        else:
            flash('User does not exist. Create an account!', category='error')

    # removed text="Testinggg", user="Yashwanth", boolean=True from the above line inside render_template.
    # replaced it with user = current_user

    return render_template("login.html",  user=current_user)

@auth.route('/logout')
@login_required
# decorator function so that we can only logout when we are logged in
def logout():
    # return "<p>Logout</p>"
    # return render_template("base.html")
    logout_user()
    return redirect(url_for('auth.login'))
    # this is redirecting to the login() function of this file.

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # return "<p>Sign Up</p>"
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user is not None:
            flash('User already exists.', category='error')
            return redirect(url_for('auth.sign_up'))
        elif len(email) < 4:
            flash("Email must be greater than 3 characters", category='error')
        elif len(first_name) < 2:
            flash("First Name must be greater than 1 characters", category='error')
        elif password1 != password2:
            flash("Passwords don\'t match", category='error')
        elif len(password1) < 7:
            flash("Password must be greater than 6 characters", category='error')
            # pass
        else:
            new_user = User(email=email, first_name=first_name, password = generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()

            user = User.query.filter_by(email=email).first() # NEW CHANGES
            if user is not None:
                login_user(user, remember=True)
                flash("Account created.", category='success')
                return redirect(url_for('views.home'))
            
            else:
                flash('An error occured. Please try again later', category='error')
                return redirect(url_for('auth.sign_up'))
            # can replace 'views.home' with '/'. Since default is the home for our website.
            # add user to database
    return render_template("sign_up.html", user=current_user)