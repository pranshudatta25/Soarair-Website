from . import db


class ProductCategory(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    products = db.relationship(
        'Product', backref='ProductCategory', cascade="all, delete-orphan")

    def __repr__(self):
        str = "Id: {}, Name: {}, Image: {}, Description: {}\n"
        str = str.format(self.id, self.name, self.image, self.description)
        return str


orderdetails = db.Table('orderdetails',
                        db.Column('order_id', db.Integer, db.ForeignKey(
                            'orders.id'), nullable=False),
                        db.Column('product_id', db.Integer, db.ForeignKey(
                            'products.id'), nullable=False),
                        db.PrimaryKeyConstraint('order_id', 'product_id'))


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    name = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    ageIntended = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    image1 = db.Column(db.String(500), nullable=False)
    image2 = db.Column(db.String(500), nullable=False)
    # images = db.relationship(
    #     'Image', backref='Product', cascade="all, delete-orphan")

    def __repr__(self):
        str = "Id: {}, Category: {}, Name: {}, Description: {}, Price: {}, Points: {}, Age Intended: {}, Rating: {}, Date: {}, Image1: {}, Image2: {}\n"
        str = str.format(self.id, self.category_id, self.name, self.description,
                         self.price, self.points, self.ageIntended, self.rating, self.date, self.image1, self.image2)
        return str


# class Image(db.Model):
#     __tablename__ = 'images'
#     id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
#     name = db.Column(db.String(500), nullable=False)

#     def __repr__(self):
#         str = "Id: {}, Product ID: {}, Name: {}\n"
#         str = str.format(self.id, self.product_id, self.name)
#         return str


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    street = db.Column(db.String(64))
    apartment = db.Column(db.String(64))
    state = db.Column(db.String(64))
    zip = db.Column(db.Integer)
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    notes = db.Column(db.String(500))
    totalcost = db.Column(db.Float)
    totalpoints = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    products = db.relationship(
        "Product", secondary=orderdetails, backref='orders')

    def __repr__(self):
        str = "Id: {}, Status: {}, Firstname: {}, Last Name: {}, Street: {}, Apartment: {}, State: {}, Zip: {}, Email: {}, Phone: {}, Notes: {}, Date: {}, Products: {}, Total Cost: {}, Total Points: {}\n"
        str = str.format(self.id, self.status, self.firstname, self.lastname, self.street, self.apartment, self.state,
                         self.zip, self.email, self.phone, self.notes, self.date, self.products, self.totalcost, self.totalpoints)
        return str
