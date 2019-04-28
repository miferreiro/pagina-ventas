#coding: utf-8
import webapp2
from webapp2_extras import jinja2
from model.Object import Object
from webapp2_extras import users

class ObjectsUserPage(webapp2.RequestHandler):

    def get(self):
        user = users.users.get_current_user()
        user_objects = Object.query(Object.login == user.nickname())
        login_logout_url = users.users.create_logout_url("/")

        template_values = {
            "user": user,
            "user_objects": user_objects,
            "login_logout_url": login_logout_url
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("objectsUser.html", **template_values))

app = webapp2.WSGIApplication([
    ('/objects_user', ObjectsUserPage)
], debug=True)
