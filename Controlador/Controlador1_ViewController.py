import Controlador.Controlador2_LoginController
from flask import render_template

# VISTA PRINCIPAL DEL APLICATIVO
def vistaPrincipal():
    return render_template('index.html')

# AGREGAR VISTAS NUEVAS AQUI
def vistas_url(lista_nombre):
    if "portal" in lista_nombre:
        return getattr(Controlador.Controlador2_LoginController, lista_nombre)()

	#if "login" in label_name:
	#	return  getattr(controllers.login_controller, label_name)()
	#if "signup" in label_name:
	#	return getattr(controllers.signup_controller, label_name) ()
	#if "team" in label_name:
	#	return getattr(controllers.team_controller, label_name) ()
	#if "update" in label_name:
	#	return getattr(controllers.update_controller, label_name)()
	#if "leaderboard" in label_name:
	#	return getattr(controllers.leaderboard_controller, label_name)()