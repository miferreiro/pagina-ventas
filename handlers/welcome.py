#coding: utf-8
import webapp2
from webapp2_extras import jinja2
from webapp2_extras import users

class WelcomePage(webapp2.RequestHandler):
    def get(self):

        usr = users.users.get_current_user()
        users.users.is_current_user_admin()  # es admin
        if usr:
            login_logout_url = users.users.create_logout_url("/")
        else:
            login_logout_url = users.users.create_login_url("/default_user")
        template_values ={
            "login_logout_url": login_logout_url,
            "usr":usr
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html", **template_values))

app = webapp2.WSGIApplication([
    ('/', WelcomePage)
], debug=True)
