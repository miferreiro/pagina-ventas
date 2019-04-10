#coding: utf-8
import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users

class DefaultUserManager(webapp2.RequestHandler):
    def get(self):
        pass


app = webapp2.WSGIApplication([
    ('/default_user', DefaultUserManager)
], debug=True)
