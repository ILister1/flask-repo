from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='' # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    customers_products = db.relationship('Customers_products', backref='customers')

class Products(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    price= db.Column(db.Float, nullable = False)
    customers_products = db.relationship('Customers_products', backref='product')


class Customers_products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column('product_id', db.Integer, db.ForeignKey('products.id'))
    customer_id = db.Column('customer_id', db.Integer, db.ForeignKey('customers.id'))
    order_date = db.Column('Date', db.String(30))

