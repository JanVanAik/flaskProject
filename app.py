from flask import Flask, render_template

app = Flask(__name__)


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
                 'desc': 'Kingerie for women'
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


if __name__ == '__main__':
    app.run()
