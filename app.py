import hashlib
import random

from models import db, User
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from forms import RegistrationForm
from flask import Flask, render_template, request, make_response, redirect, url_for
app = Flask(__name__)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = '1b3fde7edce84a1c69310362b96692987da22c7f75a12f9661407449f6e59b54'
db.init_app(app)
csrf = CSRFProtect(app)


def hex_password(password):
    salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:6]
    user_password = hashlib.sha1((password + salt).encode('utf-8')).hexdigest()
    return user_password

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.cli.command('init-db')
def init_db():
    db.create_all()


@app.route('/register/', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = hex_password(form.password.data)
        new_user = User(firstname=firstname, lastname=lastname, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
    return render_template('register.html', form=form)



@app.route('/clothes/')
def clothes():
    products = [{'name': 'Bat Norton',
                 'price': 10000,
                 'desc': 'Some new famous clothes'
                 },
                {'name': "Victoria's Secret",
                 'price': 1000,
                 'desc': 'Lingerie for women'
                 },
                {'name': 'Burton',
                 'price': 10,
                 'desc': 'Snowboard clothes'
                 }]
    return render_template('clothes.html', products=products, title='Одежда')


@app.route('/shoes/')
def shoes():
    products = [{'name': 'Balenciaga',
                 'price': 10000,
                 'desc': 'Very comfrotable trash'
                 },
                {'name': 'Gucci',
                 'price': 100000,
                 'desc': 'Very expensive trash'},
                {'name': 'Krossovki',
                 'price': 10,
                 'desc': 'Best every shoes'}]
    return render_template('shoes.html', products=products, title='Обувь')


@app.route('/bags/')
def bags():
    products = [{'name': 'Dolce&Gabbana',
                 'price': 1000,
                 'desc': 'Bag made for rich people'
                 },
                {'name': 'Adidas',
                 'price': 3000,
                 'desc': 'Sportbag'
                 },
                {'name': 'ABIBAS',
                 'price': 1000,
                 'desc': 'Chinese version of Adidas'}]
    return render_template('bags.html', products=products, title='Сумки')

@app.get('/form/')
def get_form():
    return render_template('form.html')

@app.post('/form/')
def post_form():
    name = request.form.get('name')
    email = request.form.get('email')
    response = make_response(redirect(url_for('get_greeting')))
    response.set_cookie('name', name)
    response.set_cookie('email', email)
    return response

@app.get('/greeting/')
def get_greeting():
    name = request.cookies.get('name')
    email = request.cookies.get('email')
    return render_template('greeting.html', name=name, email=email)

@app.post('/greeting/')
def post_greeting():
    response = make_response(redirect(url_for('get_form')))
    response.set_cookie('name', 'name', max_age=0)
    response.set_cookie('email', 'email', max_age=0)
    return response


if __name__ == '__main__':
    app.run()
