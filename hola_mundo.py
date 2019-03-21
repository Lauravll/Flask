from flask import Flask

app = Flask(__name__)#nuevo objeto (necesitamos una instancia), recibe como parametro __name__

@app.route('/')#wrap o un decorador, son las rutas donde el usuario puede acceder, recibe de parametro un String donde indicamos la ruta, en este caso no ponemos nada

def index():#funcion
    return 'Hola Mundo'#regresa un string
app.run()#Se encarga de ejecutar el servidor en el puerto 5000

