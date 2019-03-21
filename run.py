from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return 'Cambio'

if __name__ == '__main__': #comun en python

	app.run(debug = True, port= 8000)#Cambiamos de puerto por el 8000, tenemos una bandera (debug) el default es False pero no permite ver los cambios al actualizar.
