from server.instance import server
import sys, os

# Se necesitan importar todas las rutas/resources
# asi se registran con el servidor
from resources.url_shortener_general import *
from resources.url_shortener_id import *


if __name__ == '__main__':
    server.run()