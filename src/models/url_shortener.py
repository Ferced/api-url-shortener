from flask_sqlalchemy import SQLAlchemy
import os

db=SQLAlchemy()
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    url_original=db.Column(db.String(500), unique=True)
    url_corta=db.Column(db.String(500), unique=True)
    def __init__(self, url_original,url_corta):
        self.url_original=url_original
        self.url_corta=url_corta 
