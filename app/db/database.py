from server.instance import server
from models.url_shortener import db
from models.url_shortener_schema import ma

app, api = server.app, server.api
# Init DataBase
db.init_app(app)
# Init Marshmallow
ma.init_app(app)
