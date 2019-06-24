from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models.product import db
from models.product import Product
from models.product_schema import ma
from models.product_schema import ProductSchema
import os

app= Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir,'models/db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)
ma.init_app(app)

product_schema = ProductSchema(strict = True)
products_schema = ProductSchema(many=True,strict = True)
@app.route('/url_shortener', methods = ['POST'])
def add_url():
    url_original=request.json['url_original']
    url_corta= request.json['url_corta']
    new_product = Product(url_original,url_corta)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)
    return("HELLO WORLD")
# Get All Products
@app.route('/url_shortener', methods=['GET'])
def get_products():
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  return jsonify(result.data)

# Get Single Products
@app.route('/url_shortener/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

# Update a Product
@app.route('/url_shortener/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    url_original=request.json['url_original']
    url_corta= request.json['url_corta']

    product.url_original = url_original
    product.url_corta = url_corta

    db.session.commit()

    return product_schema.jsonify(product)

# Delete Product
@app.route('/url_shortener/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)

if __name__ == "__main__":
    app.run(debug=True)