from flask import render_template, flash, redirect, url_for
from flaskblog.form import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app


posts = [
	{
        'author': 'Xiao',
        'title': 'Rainfall Analysis',
        'content': 'The analysis report of past 1 year rainfall in Chengdu.',
        'date_posted': 'Oct 15, 2021'
    },
    {
        'author': 'Xiao',
        'title': 'Rainfall Prediction',
        'content': 'Predict the rainfall in future 48 hours in Chengdu.',
        'date_posted': 'Nov 15, 2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'santochaoya' and form.password.data == '12345678':
            flash(f'You have been logged in!', category='success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessfully! Please check your username and password.', category='danger')
    return render_template('login.html', title='Login', form=form)