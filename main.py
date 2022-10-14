import Controlador.Controlador1_ViewController
import webbrowser
from flask import Flask

app = Flask(__name__, template_folder='Vista', static_folder='Vista')
url = "http://127.0.0.1:5000"
app.secret_key = '123'

#Aquí se carga la vista principal por defecto
@app.route("/")
def main():
	return Controlador.Controlador1_ViewController.vistaPrincipal()


@app.route("/<vista_nombre>")
def vista_cambiar(vista_nombre):
	_vista_activa = Controlador.Controlador1_ViewController.vistas_url(vista_nombre)
	return _vista_activa

#@app.route('/<label_name>', methods=['POST'])
#def input_redirect(label_name):
	#response = controllers.url_controller.url_label(label_name)
	#return response

#webbrowser.open('http://net-informations.com', new=2)

webbrowser.open(url, new=1)
if __name__ == "__main__":
    app.run(debug=True)