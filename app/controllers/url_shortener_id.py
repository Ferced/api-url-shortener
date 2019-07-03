from flask import Flask, request, jsonify
from flask_restplus import Api, Resource
from server.instance import server
from models.url_shortener import Product
from models.url_shortener_schema import ProductSchema
from db.database import db,ma


app, api = server.app, server.api

# Init Product Schema
product_schema = ProductSchema(strict = True)
# Init Products Schema
products_schema = ProductSchema(many=True,strict = True)

@api.route('/url_shortener/<id>')
class UrlShortenerID(Resource):
    def get(self,id):
        #DEVUELVE EL PRODUCTO SEGUN EL ID
        product = Product.query.get(id)
        return product_schema.jsonify(product)
    def post(self,id):
        #ACTUALIZA EL PRODUCTO SEGUN EL ID
        product = Product.query.get(id)
        url_original=request.json['url_original']
        url_corta= request.json['url_corta']
        product.url_original = url_original
        product.url_corta = url_corta
        db.session.commit()
        return product_schema.jsonify(product)
    def delete(self,id):
        #ELIMINA EL PRODUCTO SEGUN EL ID
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return product_schema.jsonify(product)
