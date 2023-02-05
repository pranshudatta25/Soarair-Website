from ast import keyword
from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Product, ProductCategory, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    categories = ProductCategory.query.order_by(
        ProductCategory.name.desc()).all()
    newarrivals = Product.query.order_by(Product.date.desc()).limit(6)
    return render_template('index.html', categories=categories, newarrivals=newarrivals)


@bp.route('/shop/<int:categoryid>/')
def shop(categoryid):
    products = Product.query.filter(Product.category_id == categoryid)
    category = ProductCategory.query.filter(ProductCategory.id == categoryid)
    return render_template('shop.html', products=products, category=category)


@bp.route('/shop/new/<int:categoryid>/')
def shopnew(categoryid):
    products = Product.query.filter(Product.category_id == categoryid).order_by(
        Product.date.desc()).limit(5)
    category = ProductCategory.query.filter(ProductCategory.id == categoryid)
    return render_template('shop.html', products=products, category=category)


@bp.route('/shop/highrate/<int:categoryid>/')
def shophighrate(categoryid):
    products = Product.query.filter(Product.category_id == categoryid).filter(
        Product.rating == 5).all()
    category = ProductCategory.query.filter(ProductCategory.id == categoryid)
    return render_template('shop.html', products=products, category=category)


@bp.route('/product/<int:category>/<int:productid>/')
def product(category, productid):
    product = Product.query.filter(Product.id == productid)
    categoryid = ProductCategory.query.filter(
        ProductCategory.id == category)
    relatedprods = Product.query.filter(
        Product.category_id == category).filter(Product.id != productid).limit(3)
    return render_template('productDetails.html', product=product, categoryid=categoryid, relatedprods=relatedprods)


@bp.route('/search/')
def search():
    search = request.args.get('search')
    search1 = '%{}%'.format(search)  # substrings will match
    products = Product.query.filter(Product.description.like(
        search1) | Product.name.like(search1)).all()
    return render_template('shopsearch.html', products=products, keyword=search)


@bp.route('/order', methods=['POST', 'GET'])
def order():
    product_id = request.values.get('product_id')
   # retrieve order if there is one
    if 'order_id' in session.keys():
        order = Order.query.get(session['order_id'])
    # order will be None if order_id stale
    else:
        # there is no order
        order = None
    # create new order if needed
    if order is None:
        order = Order(status=False, firstname='', lastname='', street='', apartment='', state='', zip='',
                      email='', phone='', notes='', totalcost=0, totalpoints=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None

    # calcultate totalprice
    totalcost = 0
    if order is not None:
        for product in order.products:
            totalcost = totalcost + product.price

    # calcultate totalpoints
    totalpoints = 0
    if order is not None:
        for product in order.products:
            totalpoints = totalpoints + product.points

    if product_id is not None and order is not None:
        product = Product.query.get(product_id)
        if product not in order.products:
            try:
                order.products.append(product)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            flash('item already in basket')
            return redirect(url_for('main.order'))

    return render_template('order.html', order=order, cost=totalcost, point=totalpoints)

# Delete specific basket items


@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id = request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        product_to_delete = Product.query.get(id)
        try:
            order.products.remove(product_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))


@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))


@bp.route('/checkout/<float:total_cost>/<int:total_points>/', methods=['POST', 'GET'])
def checkout(total_cost, total_points):
    form = CheckoutForm()
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])

        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.lastname = form.lastname.data
            order.street = form.street.data
            order.apartment = form.apartment.data
            order.state = form.state.data
            order.zip = form.zip.data
            order.email = form.email.data
            order.phone = form.phone.data
            order.notes = form.notes.data
            totalcost = 0
            totalpoints = 0
            for product in order.products:
                totalcost = totalcost + product.price
            order.totalcost = totalcost
            for product in order.products:
                totalpoints = totalpoints + product.points
            order.totalpoints = totalpoints
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                return redirect(url_for('main.thankyou'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form=form, order=order, tc=total_cost, tp=total_points)


@bp.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')
