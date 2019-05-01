#coding: utf-8
import time
import webapp2
from webapp2_extras import jinja2
from webapp2_extras import users
from model.Object import Object
from model.Sale import Sale

class DeleteObject(webapp2.RequestHandler):

    def post(self):
        user = users.users.get_current_user()
        user_login = users.users.get_current_user().nickname()
        name_object = self.request.get("object_name")
        login_logout_url = users.users.create_logout_url("/")

        sales = Sale.query(Sale.name_object == name_object)

        if (name_object != "" and user_login != "" and len(list(sales)) == 0):
            objects = Object.query()
            for obj in objects:
                if obj.name == name_object and obj.login == user_login:
                    obj_delete = obj

            obj_delete.key.delete()

            user_objects = Object.query(Object.login == user_login)
            template_values = {
                "user": user,
                "user_objects": user_objects,
                "correct": "El objeto \"" + name_object + "\" se ha eliminado correctamente",
                "login_logout_url": login_logout_url
            }
            jinja = jinja2.get_jinja2(app=self.app )
            self.response.write(jinja.render_template("objectsUser.html", **template_values))
        else:

            user_objects = Object.query(Object.login == user_login)
            template_values = {
                "user": user,
                "user_objects": user_objects,
                "error": "El objeto \"" + name_object + "\" no se ha podido eliminar",
                "login_logout_url": login_logout_url
            }
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("objectsUser.html", **template_values))


app = webapp2.WSGIApplication([
    ('/delete_object', DeleteObject)
], debug=True)
