#  pip install Flask==2.2.5 
#Instala una libreria para poder desplegar desarrollos web .py
#  pip install Werkzeug==2.2.3

from flask import Flask

app = Flask(__name__)  #Con este creo el servico Flask que se va a llamar app

@app.route('/api/hello')

def hello():
    return 'hola mundo desde docker'

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000) 

 #cd .. te lleva a la carpeta de atras 