from flask import Flask, request, jsonify, Blueprint
from flask_restplus import Api, Resource
from models.product import db
from models.product import Product
from models.product_schema import ma
from models.product_schema import ProductSchema
from urlShortener.generadorUrl import GeneradorUrl
import random



blueprint = Blueprint('api', __name__)
api = Api(blueprint)
# Init Product Schema
product_schema = ProductSchema(strict = True)
# Init Products Schema
products_schema = ProductSchema(many=True,strict = True)

@api.route('/url_shortener')
class UrlShortener(Resource):
    def get(self):
        #DEVUELVE TODOS LOS PRODUCTOS
        all_products = Product.query.all()
        result = products_schema.dump(all_products)
        return jsonify(result.data)
    def post(self):
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
@api.route('/url_shortener/<id>')
class ObtenerProducto(Resource):
    def get(self,id):
        #DEVUELVE EL PRODUCTO SEGUN EL ID
        product = Product.query.get(id)
        return product_schema.jsonify(product)
    def put(self,id):
        #ACTUALIZA EL PRODUCTO SEGUN EL ID
        product = Product.query.get(id)
        url_original=request.json['url_original']
        url_corta= request.json['url_corta']
        product.url_original = url_original
        product.url_corta = url_corta
        db.session.commit()
        return product_schema.jsonify(product)
    def delete_product(self,id):
        #ELIMINA EL PRODUCTO SEGUN EL ID
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return product_schema.jsonify(product)
