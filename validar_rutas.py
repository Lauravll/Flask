from flask import Flask
from flask import request 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Mundo'

#http://127.0.0.1:8000/params/nombre/apellido/5
@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<last_name>')
@app.route('/params/<name>/<last_name>/<int:num>')

def params(name = '', last_name = '', num = ''):
	return 'El parametro es: {}, {}, {}'.format(name, last_name, num)

if __name__ == '__main__': 
	app.run(debug = True, port= 8000)
