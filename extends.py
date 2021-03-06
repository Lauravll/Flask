#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder = "vistas")

#http://127.0.0.1:8000/user/Nombre33
@app.route('/user/<name>')
def index(name = ''):
	edad = 22
	lista = [1, 2, 3, 4]
	return render_template('usuario.html', nombre=name, edad=edad, list=lista)

#http://127.0.0.1:8000/client
@app.route('/client')
def client():
	lista_nombre = ['Test1', 'Test2', 'Test3', 'Test4']
	return render_template('client.html', list=lista_nombre)
	
if __name__ == '__main__': 
	app.run(debug = True, port= 8000)
