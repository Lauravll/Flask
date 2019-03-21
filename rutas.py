from flask import Flask
from flask import request #Para trabajar co parametros

app = Flask(__name__)

@app.route('/')#Tenemos una unica ruta que es la del slash pero podemos tener n cantidad de funciones y rutas
def index():#No podemos repetir el mismo metodo
    return 'Hola Mundo'
	
#http://127.0.0.1:8000/params?params1=Parametro1


#params es la ruta y puede o no recibir un parametro dentro de la url si contiene un parametro llamado params1 se guarda el valor y si no lo contiene envia el string los parametros son indefinidos

#http://127.0.0.1:8000/params?params1=Parametro1&params2=Parametro2

@app.route('/params')#Tenemos una unica ruta que es la del slash pero podemos tener n cantidad de funciones y rutas
def params():#No podemos repetir el mismo metodo
	param = request.args.get('params1', 'no contiene este parametro')#Dentro de la url necesita ese parametro
	param2 = request.args.get('params2', 'no contiene este parametro')#Dentro de la url necesita ese parametro
	return 'El parametro es: {}, {}'.format(param, param2)

if __name__ == '__main__': 

	app.run(debug = True, port= 8000)
