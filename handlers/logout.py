#coding: utf-8
import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2


class LogOutPage(webapp2.RequestHandler):
    def post(self):

        users.create_logout_url("index.html")

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html"))


app = webapp2.WSGIApplication([
    ('/logout', LogOutPage)
], debug=True)
