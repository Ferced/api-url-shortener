from server.instance import server
import sys, os

# Se necesitan importar todas las rutas/resources/controllers
# asi se registran con el servidor
from controllers.url_shortener_general import *
from controllers.url_shortener_id import *


if __name__ == '__main__':
    server.run()