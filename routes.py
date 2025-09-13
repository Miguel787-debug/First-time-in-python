from main import app
from flask import render_template # usado para renderizar as templates do HTML


@app.route('/') # a barra '/' representa a pasta raiz do site
def home(): # A função está associada a rota("route")
    return render_template('formulario.html')

@app.route('/contato')   
def contato():
    return 'Miguel, Celular 11 9876-4321'