#coding: utf-8
import webapp2
import hashlib
from webapp2_extras import jinja2
from model.User import User

class RegistryPage(webapp2.RequestHandler):
    def get(self):
        template_values ={
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("registry.html", **template_values))

    def post(self):
        login = self.request.get("login")
        password = self.request.get("password")

        if len(login.strip()) == 0 or len(password.strip()) == 0:
            template_values = {
                "error": 'Los campos no pueden ser vacios'
            }
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("registry.html", **template_values))
            return

        usuario = User.query().order(-User.login)
        isRegistered = True

        for usr in usuario:
            if usr.login == login:
                isRegistered = False

        if isRegistered:

            nuevo_usr = User(login=login,password= str(hashlib.new("sha1", password)))
            nuevo_usr.put()

            jinja = jinja2.get_jinja2(app=self.app)
            template_values = {
                "correct": 'El usuario con login ( ' + login + ' ) ha sido registrado'
            }
            self.response.write(jinja.render_template("index.html", **template_values))
            return
        else:
            template_values = {
                "error": 'Ya existe un usuario registrado con ese login'
            }
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("registry.html", **template_values))
            return

app = webapp2.WSGIApplication([
    ('/registry', RegistryPage)
], debug=True)
