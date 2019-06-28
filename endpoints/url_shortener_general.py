from flask import Flask, request, jsonify, Blueprint
from models.product import db, Product
from models.product_schema import ma, ProductSchema
from url_generator.generadorUrl import GeneradorUrl

url_shortener= Blueprint('url_shortener', __name__)
# Init Product Schema
product_schema = ProductSchema(strict = True)
# Init Products Schema
products_schema = ProductSchema(many=True,strict = True)

@url_shortener.route('/url_shortener',methods=["GET","POST"])
def url_shortener_general():
    if request.method == "GET":
        #DEVUELVE TODOS LOS PRODUCTOS
        all_products = Product.query.all()
        result = products_schema.dump(all_products)
        return jsonify(result.data)
    if request.method == "POST":
        #AGREGA UN PRODUCTO NUEVO
        url_original=request.json['url_original']
        url_basededatos=Product.query.filter_by(url_original=url_original).first()
        if url_basededatos is None:
            url_corta= GeneradorUrl.generarUrlAleatoria()
            new_product = Product(url_original,url_corta)
            db.session.add(new_product)
            db.session.commit()
        else:
            new_product = url_basededatos
        return product_schema.jsonify(new_product)
