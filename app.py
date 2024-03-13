from models import db, User
from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

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
