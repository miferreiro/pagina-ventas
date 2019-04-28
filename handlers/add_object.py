#coding: utf-8
import time
import webapp2
from webapp2_extras import jinja2
from model.Object import Object
from webapp2_extras import users

class AddObject(webapp2.RequestHandler):

    def post(self):
        user = users.users.get_current_user()
        user_login = user.nickname()
        name_object = self.request.get("name_object")
        desciption_object = self.request.get("descripcion_object")
        login_logout_url = users.users.create_logout_url("/")

        objects = Object.query()
        valid = True
        for object in objects:
            if object.name == name_object:
                valid = False

        if (valid and name_object != "" and desciption_object != ""):

            object = Object(name = name_object, description = desciption_object, login = user_login, win_on_sale = False)
            object.put()
            time.sleep(1)

            user_objects = Object.query(Object.login == user_login)
            template_values = {
                "user": user,
                "user_objects": user_objects,
                "correct" : "El objeto se ha creado correctamente",
                "login_logout_url": login_logout_url
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("objectsUser.html", **template_values))
            return
        else:
            if not valid:
                message = "Ya existe un objeto con el nombre introducido"
            else:
                message = "Se ha producido un error al crear un objeto"

            user_objects = Object.query(Object.login == user_login)

            template_values = {
                "user": user,
                "user_objects": user_objects,
                "error" : message,
                "login_logout_url": login_logout_url
            }
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("objectsUser.html", **template_values))
            return

app = webapp2.WSGIApplication([
    ('/add_object', AddObject)
], debug=True)
