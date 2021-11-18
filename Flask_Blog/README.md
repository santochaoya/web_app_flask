This is a notebook of [Python Flask Tutorial: Full-Featured Web App](https://www.youtube.com/watch?v=MwZwr5Tvyxo&t=41s)

There are more modules included. For example, Account(see all information, upload image a profile),
reset password, update post blog.



# Route

## Framework - Flask

### Import

```python
from flask import Flask
app = Flask(__name__)

```

* ```__name__``` it will be ```__main__``` if we run the python directly. Or it will be the name of the module if we import it.



### Run

#### Run in terminal

To run the application, we need to set the environment variable to the file

* PowerShell

```shell
$env:FLASK_APP = "flaskblog.py"
flask run
```

* CMD

```bash
set FLASK_APP = flaskblog.py
flask run
```

* bash

```bash
export FLASK_APP=hello
flask run
```

#### Run directly

```python
if __name__ == '__main__':
	app.run(debug=True)
```



### Home page

Add router of home page

> Route: the page where the browser will go to

```python
@app.route('/')
def home():
    return "<h1>Hello, World!</h1>"
```



### About Page

```python
@app.route('/about')
def about():
    return "<h1>About Page</h1>"
```



# HTML

## template

### Create home html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>HOME Page</h1>
</body>
</html>
```



### Bind html to Python

* Python

  In python, we need to render the template

  ```python
  from flask import render
  
  def home():
  	return render_template('home.html')
  ```



# Add post

## Make some dummy data

```python
posts = [
	{
        'author': 'Xiao',
        'title': 'Rainfall Analysis',
        'content': 'The analysis report of past 1 year rainfall in Chengdu.'
        'date_posted': 'Oct 15, 2021'
    },
    	{
        'author': 'Xiao',
        'title': 'Rainfall Prediction',
        'content': 'Predict the rainfall in future 48 hours in Chengdu.'
        'date_posted': 'Nov 15, 2021'
    }
]
```



## Pass variable to template

* **Python**

Add parameter to ```render_template``` to pass the variable as a parameter to template.

```python
render_template('home.html', posts=posts)
```

* The first ```posts``` is the variable we will have access and use in template.
* The second ```posts``` is our post data.



* **HTML** :
  * Loop through the posts data
  * access the variable

```html
{% for post in posts %}
    <h1>{{ post.title }}</h1>
	<p>By {{ post.author }} on {{ post.date_posted }}</p>
	<p>{{ post.content }}</p>
{% endfor %}
```



## Template inheritance

### Create a parent template - Parent template

The parent template ```layout.html``` where all child templates will inherit from. It contains all the repeat sections in the child templates.  This is a main structure of HTM that will be included on every page, and can have multiple blocks.

Replace the unique section to a block which can be override the ```content``` (can be named as anything) part by child templates.

```html
{% block content %}{% endblock %}
```



### Bind parent template to child template - child template

* **Bind to parent template**

```html
{% extends "layout.html" %}
```

* **Replace content**

```html
{% block content %}
<unique code here>
{% endblock %}
```



**Example**

* ```layout.html```

  ```html
  {% block content %}{% endblock %}
  ```

  or explicit which need to block when we have multiple content

  ```html
  (% block content %){% endblock content %}
  ```

  

* ```home.html```

  ```html
  {% extents "layout.html" %}
  {% block content %}
  	{% for post in posts %}
  		<h1>{{ post.title }}</h1>
  	{% endfor %}
  {% endblock content %}
  ```



# Bootstrap Framework

## Starter

* **Header part** - CSS and meta tag

  ```html
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
  
      <!-- Bootstrap CSS -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  ```

* **Body part** - JavaScript tag

  ```html
  <!-- Optional JavaScript; choose one of the two! -->
  
      <!-- Option 1: Bootstrap Bundle with Popper -->
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
      <!-- Option 2: Separate Popper and Bootstrap JS -->
      <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
  ```



**Example**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    {% if title %}
        <title>Flask Blog - {{ title }}</title>
    {% else %}
        <title>Flask Blog</title>
    {% endif %}
</head>
<body>
{% block content %}
{% endblock content %}

<!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
</body>
</html>
```



## Container Class

We will wrap the block content into a div with the class of container, which will give a good padding and spacing.

```html
<div class="container">
    {% block content %}{% endblock %}
</div>
```



# Navigation

Add a navigation bootstrap tags with bootstrap.

```html
<!-- A navigation bar with bootstrap here -->
<header class="site-header">
    <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
        <div class="container">
            <a class="navbar-brand mr-4" href="/">Flask Blog</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle"
                    aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarToggle">
                <div class="navbar-nav mr-auto">
                    <a class="nav-item nav-link" href="/">Home</a>
                    <a class="nav-item nav-link" href="/about">About</a>
                </div>
                <!-- Navbar Right Side -->
                <div class="navbar-nav">
                    <a class="nav-item nav-link" href="/login">Login</a>
                    <a class="nav-item nav-link" href="/register">Register</a>
                </div>
            </div>
        </div>
    </nav>
</header>
```



# Main section

This is the section contains content block.

```html
<main role="main" class="container">
    <div class="row">
        <div class="col-md-8">
            {% block content %}{% endblock %}
        </div>
        <div class="col-md-4">
            <div class="content-section">
                <h3>Our Sidebar</h3>
                <p class='text-muted'>You can put any information here you'd like.
                <ul class="list-group">
                    <li class="list-group-item list-group-item-light">Latest Posts</li>
                    <li class="list-group-item list-group-item-light">Announcements</li>
                    <li class="list-group-item list-group-item-light">Calendars</li>
                    <li class="list-group-item list-group-item-light">etc</li>
                </ul>
                </p>
            </div>
        </div>
    </div>
</main>
```



# Main CSS

This is the custom styles that isn't bootstrap. 

> The CSS and JavaScript files need to be located in a ```static``` directory.



## Bind the CSS file to the HTML

We use ```url_for``` function to bind the location of ```main.css``` to our main structure to get these custom styls.

```html
<link rel="stylesheet" type="text/css" href={{ url_for('static', filename='main.css') }}>
```

* ```url_for``` will find the exact location of routes.



# Split posts

We can split the posts with these article functional codes in each loop of posts.

```html
{% extends "layout.html" %}
{% block content %}
    {% for post in posts %}
        <article class="media content-section">
            <div class="media-body">
                <div class="article-metadata">
                    <a class="mr-2" href="#">{{ post.author }}</a>
                    <small class="text-muted">{{ post.date_posted }}</small>
                </div>
                <h2><a class="article-title" href="#">{{ post.title }}</a></h2>
                <p class="article-content">{{ post.content }}</p>
            </div>
        </article>
    {% endfor %}
{% endblock content %}
```

 

# Forms

Use to ```wt form``` make forms work with flask.

## Installation

```bash
pip install flask-wtf
```



## Import

```python
from flask_wtf import FlaskForm
```



## Create form

We can create form in Python function, then it will automatically convert to HTML form with template.



### Register form

```python
from wtforms impport StringField

class RegistrationForm(FlaskForm):
```



* **Username** -> String

  ```python
  username = StringField('Username')
  ```

  * ```Username``` will be the label in HTML as well.

* **Validators**

  The list of validations we prefer to check, Use it as the second argument of ```StringField()```

  For example, we prefer to check if the string is empty and limit the length:

  * ```DataRequired``` check if the ```StringField()``` is empty
  * ```Length``` to limit the length of the String

  ```python
  from wtforms.validators import DataRequired, Length
  
  username = StringField('Username', 
                         validators=[DataRequired(), Length(min=2, max=20)])
  ```

* **email** -> String

  * Validate it is a valid email address

  ```python
  from wtform.validators import Email
  
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  ```

* **Password** -> PasswordField

  * Using ```PasswordField``` with argument ```Password``` pass to HTML and validators
  * The same as the **Confirm Password** with ```EqualTo``` validators

  ```python
  from wtforms import PasswordField
  
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', 
                                   validators=[DataRequired(), EqualTo('password')])
  ```

* **Submit**

  Using ```SubmitField```

  ```python
  from wtform import SubmitField
  
  submit = SubmitField('Sign Up')
  ```



#### Template of Register Forms

Create two templates of ```register.html``` and ```login.html```. Inherit the main structure from ```layout.html```.

```html
{% extents "layout.html" %}
{% block content %}
	<div class="content-section">
        <form method="POST" action="">
            {{ form.hidden_tag()}}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Join Today</legend>
                <dir class="form-group">
                	{{ form.username.label(class="form-content-label")}}
                    {{ form.username(class="form-control form-control-lg")}}
                </dir>
                <dir class="form-group">
                	{{ form.email.label(class="form-content-label")}}
                    {{ form.email(class="form-control form-control-lg")}}
                </dir>
                <dir class="form-group">
                	{{ form.password.label(class="form-content-label")}}
                    {{ form.password(class="form-control form-control-lg")}}
                </dir>
                <dir class="form-group">
                	{{ form.confirm_password.label(class="form-content-label")}}
                    {{ form.confirm_password(class="form-control form-control-lg")}}
                </dir>
            </fieldset>
            <dir class="form-group">
                {{ form.submit(class="btn btn-outline-info")}}
            </dir>
        </form>
        <div class="border-top pt-3">
            <small class="text-muted">
            	Aready Have an Account? <a class="ml-2" href="{{ url_for("login")}}"
            </small>
        </div>
	</div>
{% endblock %}
```

* ```class="content-section"``` is the styles in```main.css```

* ```method="POST" action=""```  means the ```POST``` method will post the form to the same route where we currently on
* ```form.hidden_tag()``` add a ```CSRF token``` or ```cross-site``` request a foreign token, to protect the secret key from some attracts
* ```class="border-bottom mb-4">``` a margin bottom with a value of 4.
* ```{{ form.username.label(class="form-control-label") }}```  call the label of username from the form with some bootstrap style.
  * ```username``` is the variable name defined in the ```register``` class
* ```{{ form.submit(class="btn btn-outline-info"))}}``` the submit button with a style.

* ```<small class="text-muted">``` the text will be a little fade out
* ```<a class="ml-2" href="...">``` link to the login page, with margin space with 2
* ```url_for('login')``` the ```login``` is the name of route function where the ```url_for``` will route for

> When need to link to somewhere with route, using ```url_for()``` function with the argument name of the **route function**.



### Login Form

Similar to the registration form, get rid of email and confirm password.

* **Login Access**

  Allow the user to stay logged in after their browser closes using a secure cookie.

  ```python
  from wtforms import BooleanField
  
  remember = BooleanField('Remember Me')
  ```

* **Secure Key**

  The secure key used to against changing cookie or other contact. 

  * Create it after creating the app:

  ```python
  app.config['SECURE_KEY'] = '9846d58es4b5d68f9es4ab98d32w908f1se9'
  ```

  * Generate a series of random characters

  ```python
  import secrets
  
  secrets.token_hex(16)
  ```

  ```bash
  '04e971565400cb43a02d00e5e8e206e6'
  ```



#### Remember me check box

It is similar to the register page. with a **remember me **section.

```html
<div class="form-check">
    {{ form.remember(class="form-check-input")}}
    {{ form.remember.label(class="form-check-label")}}
</div>
```



#### Forgot password button

```html
<small class="text-muted ml-2">
	<a href="<forget password form>">Forget Password?</a>
</small>
```



#### validate logged in

For example, we make some dummy data to check if the username and password correct, and add methods of ```POST``` and ```GET``` to the route.

```python
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
```



#### 

### Routes for Forms

Routes the forms, and pass it to the template

In ```app``` module, we create the routes for registration and login form.

```python
@app.route('/register')
def register():
	form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)
```



### Check validate

* **check success submission**

  Set the check part to check whether the data posted and the data is valid.

  Use ```validate_on_submit()``` function to check if the data validate when submitted. Then ```flash``` message for the validation message and ```redirect``` to the **home page**. in the ```register()``` method:

  ```python
  def register():
  	form = RegistrationForm()
      if form.validate_on_submit():
          flash(f'Account created for {form.username.data}', category='success')
          return redirect(url_for('home'))
      return render_template('register.html', title='Register', form=form)
  ```

  

  In the ```layout.html``` we put the pop-up message can be in any pages. and check if there have returned some message if the account created.

  ```html
  {% with messages = get_flashed_messages(with_categories=true) %}
  	{% if messages %}
  		{% for category, message in message %}
  			<div class="alert alert-{{ category }}">
  				{{ message }}
  			</div>
  		{% endfor %}
  	{% endif %}
  {% endwith %}
  ```

  * ```get_flashed_messages(with_categories=true)``` will return the flashed message we sent to the templates, and with the category we defined in the ```register``` module.

* **check errors** 

  ```html
  {% if form.username.errors %}
  	{{ form.username(class="form-control form-control-lg is-invalid")}}
  	<div class="invalid-feedback">
          {% for error in form.username.errors %}
          	{{ error }}
          {% endfor %}
      </div>
  {% else %}
  	{{ form.username(class="form-control form-control-lg is-invalid")}}
  {% endif %}
  ```

  Check if we have errors in ```form.username```

  Then copy and past these to all field of the register form. It will return the error message for each field.



# Chapter 4 - Database

Using ```SQLachemy```, this module will easily to change the database without changing the Python code. We just change the URL for the ```PostgreSQL``` or ```SQLite```. We will using the ```SQlite``` for development environment and the ```PostgreSQL``` for our production environment.



## Database File

### Set the location

Set a relative location of ```SQLite``` as a configuration.

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
```

* ```sqlite:///site.db``` is to set the relative location for ```SQLite``` by ```///```, which means the ```SQLite``` database is set in the current directory of the Python module we current in.



### Create database

In the terminal, we open the python interface. Create the database in the same folder where the ```db``` was imported.

```python
db.create_all()
```



### Access to database

* **Add users**

  ```python
  from flaskblog import User, Post
  
  user_1 = User(username='Xiao', email='xiao@gmail.com', password='password')
  db.session.add(user_1)
  db.session.commit()
  ```

* **Get all users**

  ```
  User.query.all()
  ```

* **Get the First users**

  ```python
  User.query.first()
  ```

* **Get users with filter**

  ```python
  User.query.filter_by(username='Xiao').all()
  ```

* **Get attributes**

  Get user_id or get user with id = `

  ```python
  user = User.query.first()
  user.id
  ```

  or

  ```
  user = User.query.get(1)
  ```



All will be similar to create a post in post table. When we created a post, it will automatically generate a date_posted with the current datetime. After creating, we can check on the ```user``` table by ```user.posts```.

### Delete data in database

* **Delete all data**

  This will delete all the structure in database.

  ```python
  db.drop_all()
  ```

* **Withdraw all data structure**

  After ```drop_all()```, we use ```create_all()``` to create the database structure back.

  ```python
  db.create_all()
  ```

  

## Create Tables

We create each class model for each table.

### User

We use a class to create this table. Then create columns by ```db.Column()``` with argument ```type```, ```primary_key```, 	```unique``` , ```nullable``` and so on.

```python
class User(db.model):
    # add columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='')
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
    	return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
```

* ```db.Integer```, ```db.String(20)```: the type of the column with the length.
* ```primary_key```:
* ```unique```: must be unique value if set it to ```True```.
* ```nullable```: must be non-null if set it to ```True```.
* ```default```: the default value.
* ```def __repr__(self):```: this is the object is printed.



### Posts

Similar to **User**, 

```python
class Post(db.model):
    # add columns
    id = db.Column(db.Integer, primary_key=True)
    tile = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.datetime(), nullable=False, default=datetime.utcnow
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
    	return f"Post('{self.tile}', '{self.date_posted}')"
    
```

* ```default=datetime.utcnow``` create the current as the default output. Without parentheses to pass the function as the argument not the current time.



### Relationship of tables

* **One to many** - foreign key in child table

  *  **Parent table**(**one**)

    One author to many posts. 

    ```python
    posts = db.relationship('Post', backref='author', lasy=True)
    ```

    * ```relationship()``` the first argument is the child ```module``` name```'Post'``` 
    * ```backref``` similar to add another to the ```Post``` table, use ```author``` attribute to get the user who create the post.
    * ```lasy```  : ```True``` will return all the posts for the first user, similar to ```session.query(User).first().posts```

  * **Child table(many)**

    ```python
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ```

    * ```ForeignKey```: the first argument is the parent ```table```name



# Chapter 5 - Restructured the module to a package

