from model import firebase_token as token
import web
import pyrebase

render=web.template.render('./views/')

class Agenda:
    def GET(self):
        try:
            #creacion de objeto tipo firebase inicializado con la configuracion del archivo
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            #Concexion a la base de datos
            db = firebase.database()

            #Obtener datos
            agenda = db.child("agenda").get()
            result={}
            for agenda in agenda.each():
                result[agenda.key()] = agenda.val()
            dic=[]
            mail=0
            name=0
            for n in range(len(result)-1):
                n=n+1
                mail=result[n]["email"]
                dic.append(mail)
                name=result[n]["nombre"]
                dic.append(name)
            print(dic)
            if n%2==0:
                print("ok", n)
            else:
                print("no", n)

            print(result)
            
            return render.agenda(dic, 0, 1)

        #Condicion para error
        except Exception as error:
            print("Error :{}".format(error.args[1]))

    def POST(self):
        try:
            return web.seeother('/insert')

        #Condicion para error
        except Exception as error:
            print("Error :{}".format(error.args[1]))