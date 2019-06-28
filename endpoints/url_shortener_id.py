from flask import Flask, request, jsonify, Blueprint
from models.product import db, Product
from models.product_schema import ma, ProductSchema

url_shortener_id= Blueprint('url_shortener_id', __name__)
# Init Product Schema
product_schema = ProductSchema(strict = True)
# Init Products Schema
products_schema = ProductSchema(many=True,strict = True)

@url_shortener_id.route('/url_shortener/<id>',methods=["GET","POST","DELETE"])
def url_shortener_single(id):
    if request.method == "GET":
        #DEVUELVE EL PRODUCTO SEGUN EL ID
        product = Product.query.get(id)
        return product_schema.jsonify(product)
    if request.method == "POST":
        #ACTUALIZA EL PRODUCTO SEGUN EL ID
        product = Product.query.get(id)
        url_original=request.json['url_original']
        url_corta= request.json['url_corta']
        product.url_original = url_original
        product.url_corta = url_corta
        db.session.commit()
        return product_schema.jsonify(product)
    if request.method == "DELETE":
        #ELIMINA EL PRODUCTO SEGUN EL ID
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return product_schema.jsonify(product)
