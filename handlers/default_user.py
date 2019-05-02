#coding: utf-8
import webapp2
from webapp2_extras import jinja2
from webapp2_extras import users

class DefaultUserManager(webapp2.RequestHandler):

    def get(self):
        user = users.users.get_current_user()
        login_logout_url = users.users.create_logout_url("/")
        jinja = jinja2.get_jinja2(app=self.app)
        template_values = {
            "user": user,
            "login_logout_url":login_logout_url
        }
        self.response.write(jinja.render_template("defaultUser.html", **template_values))

app = webapp2.WSGIApplication([
    ('/default_user', DefaultUserManager)
], debug=True)
