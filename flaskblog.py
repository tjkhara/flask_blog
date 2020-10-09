from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b236e81c6176ccecab375843dd8379e1'

posts = [
    {
        'author': 'TJ',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 20th 2018'
    },
    {
        'author': 'Django',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 28th 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f"You have been logged in!", "success")
            return redirect(url_for('home'))
        else:
            flash("Login unsuccessful. Please check username and password.","danger")
    return render_template('login.html', title='Login', form=form)