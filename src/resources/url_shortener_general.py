from flask import Flask, request, jsonify
from flask_restplus import Api, Resource
from models.url_shortener import db, Product
from models.url_shortener_schema import ma, ProductSchema
from models.database import db
from server.instance import server
from helpers.generadorUrl import GeneradorUrl


app, api= server.app, server.api
# Init Product Schema
product_schema = ProductSchema(strict = True)
# Init Products Schema
products_schema = ProductSchema(many=True,strict = True)



@api.route('/url_shortener')
class UrlShortnerGeneral(Resource):
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
