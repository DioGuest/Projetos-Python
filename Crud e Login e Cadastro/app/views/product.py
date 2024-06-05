from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import db
from app.models.product import Product
from app.forms import ProductForm

product_bp = Blueprint('product', __name__)

@product_bp.route('/dashboard')
@login_required
def dashboard():
    products = Product.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', products=products)

@product_bp.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(name=form.name.data, price=form.price.data, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('product.dashboard'))
    return render_template('product_form.html', form=form)

@product_bp.route('/edit_product/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_product(id):
    product = Product.query.get_or_404(id)
    if product.owner != current_user:
        return redirect(url_for('product.dashboard'))
    form = ProductForm()
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        db.session.commit()
        return redirect(url_for('product.dashboard'))
    form.name.data = product.name
    form.price.data = product.price
    return render_template('product_form.html', form=form)

@product_bp.route('/delete_product/<int:id>', methods=['POST'])
@login_required
def delete_product(id):
    product = Product.query.get_or_404(id)
    if product.owner != current_user:
        return redirect(url_for('product.dashboard'))
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('product.dashboard'))
