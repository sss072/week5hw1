from flask import Blueprint, render_template, request, redirect, url_for 
from recipe_api.forms import UserLoginForm
from recipe_api.models import db, User

auth = Blueprint('auth',__name__, template_folder='auth_templates')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email, password)
        new_user = User(email, password)
        db.session.add(new_user)
        db.session.commit() 
        redirect(url_for('site.home'))
    return render_template('signup.html', form = form)


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email, password)
    return render_template('signin.html', form = form)
