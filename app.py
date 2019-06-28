from flask import Flask, request, jsonify
from endpoints.url_shortener_general import url_shortener
from endpoints.url_shortener_id import url_shortener_id
from models.product import db
from models.product_schema import ma
import os

app= Flask(__name__)
# Init DataBase
db.init_app(app)
# Init Marshmallow
ma.init_app(app)
# Path de directorio
basedir = os.path.abspath(os.path.dirname(__file__))
# Configuracion APP
app.config.from_object("config.DevelopmentConfig")
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir,'models/db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.register_blueprint(url_shortener)
app.register_blueprint(url_shortener_id)

if __name__ == "__main__":
    app.run()