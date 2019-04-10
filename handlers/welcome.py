#coding: utf-8
import webapp2
import hashlib
from webapp2_extras import jinja2
from model.User import User


class WelcomePage(webapp2.RequestHandler):
    def get(self):
        template_values ={
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html", **template_values))

    def post(self):

        user_login = self.request.get("login")
        user_password = self.request.get("password")

        if len(user_login.strip()) == 0 or len(user_password.strip()) == 0:
            template_values = {
                "error": 'Los campos no pueden ser vacios'
            }
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("index.html", **template_values))
            return

        usuario = User.query(User.login == user_login and User.password == str(hashlib.new("sha1", user_password)))

        if usuario.count != 0:
            jinja = jinja2.get_jinja2(app=self.app)
            template_values = {
                "login": user_login
            }
            self.response.write(jinja.render_template("defaultUser.html", **template_values))
            return
        else:
            template_values = {
                "error": 'Los campos introducidos no son correctos'
            }
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("index.html", **template_values))
            return

app = webapp2.WSGIApplication([
    ('/', WelcomePage)
], debug=True)
