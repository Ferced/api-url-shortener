from flask import Flask, request, jsonify, Blueprint
from flask_restplus import Api, Resource
from models.product import db
from models.product import Product
from models.product_schema import ma
from models.product_schema import ProductSchema
import random



blueprint = Blueprint('api', __name__)
api = Api(blueprint)
# Init Product Schema
product_schema = ProductSchema(strict = True)
# Init Products Schema
products_schema = ProductSchema(many=True,strict = True)

def generarUrl():
	#GENERA UN CODIGO DE 7 CARACTERES DE BASE64 (ELIGE UNA DE LAS 3 LISTA DE NUMEROS ASCII Y DE ESA ELIJE UNO ALEATORIO) ASI X 7
	url_corta="http://meli.st/"
	lista_ascii_aceptables=[[48,57],[65,90],[97,122]]
	for i in range(7):
		numero_lista_aleatorio=random.randint(0,len(lista_ascii_aceptables)-1)
		numero_ascii=random.randint(lista_ascii_aceptables[numero_lista_aleatorio][0],lista_ascii_aceptables[numero_lista_aleatorio][1])
		url_corta+=chr(numero_ascii)
	return url_corta
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
            url_corta= generarUrl()
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
