from model import firebase_token as token
import web
import pyrebase

render=web.template.render('./views/')

class Index:
    def GET(self):
        #Redireccionar al archivo index.html
        try:
            return render.index()
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result

    def POST(self):
        try:
            print("check")
            #obtener datos del formulario de index.html
            data=web.input()
            email = str(data.email)
            password = str(data.password)
            print(email)
            print(password)
            #creacion de objeto tipo firebase inicializado con la configuracion del archivo model/firebase_token.py
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            #Objeto para obtener los datos del usuario  
            print(firebase)
            auth = firebase.auth()
            #Realizar el metodo de autenticacion por email y contraseña
            user = auth.sign_in_with_email_and_password(email, password)
            #verificacion en consola
            print(user)
            #Redireccionar al archivo agenda.html
            return web.seeother('/list')

        #Condicion para error
        except Exception as error:
            print("Error :{}".format(error.args[1]))
            #Redireccionar al archivo advertencia.html
            return render.advertencia()