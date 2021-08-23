from model import firebase_token as token
import web
import pyrebase

render=web.template.render('./views/')

class Insert:
    def GET(self):
        #Redireccionar al archivo insert.html
        try:
            return render.insert()
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result

    def POST(self):
        try:
             #creacion de objeto tipo firebase inicializado con la configuracion del archivo
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            #Concexion a la base de datos
            db = firebase.database()

            #obtener datos del formulario de insert.html
            data=web.input()
            nombre = str(data.nombre)
            email = str(data.email)
            print(email)
            print(nombre)

            #obtener id
            agenda = db.child("agenda").get()
            r=0
            for agenda in agenda.each():
                r=int(agenda.key())
            r=r+1
            print(r)

            send_data={"nombre": nombre, "email": email}
            print(send_data)
            
            #Enviar datos con id
            db.child("agenda").child(r).set(send_data)

            return web.seeother('/list')

        #Condicion para error
        except Exception as error:
            print("Error :{}".format(error.args[1]))