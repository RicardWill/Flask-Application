from flask import Flask, render_template, request, redirect, session
#import models.user_model
#import entities.User

app = Flask(__name__)
app.secret_key = '123'

def portal():
    return render_template('portal.html')


#def login_verify():
    #_email = str(request.form['inputEmail'])
    #_password = str(request.form['inputPassword'])
    #user_id = models.user_model.get_user(_email, _password)
    #if user_id != "":
    #    session['user_id'] = user_id
    #    return redirect("/", code=302)
    #else:
    #    return render_template('home.html')


#def login_logout():
    #session.pop('user_id', None)
    #return redirect("/", code=302)