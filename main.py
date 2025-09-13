from flask import Flask # Importa somente o módulo (FLASK)

app = Flask(__name__) # (app) é uma variavel que inicia nossa aplicaçã

from routes import *

if __name__ == '__main__':
    app.run(debug=True)