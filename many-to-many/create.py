from app import db, Customers, Products

db.create_all()

ben = Customers(first_name='Ben',last_name='Hesketh', email='ben@ben.com')

phone = Products(name='Samsung 7', price=250.00)

db.session.add(ben)
db.session.add(phone)
db.session.commit()

order_phone = Customers_products(product_id=phone.id, customer_id=ben.id)

db.session.add(order_phone)
db.session.commit()


