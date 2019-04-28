#coding: utf-8
import webapp2
from webapp2_extras import jinja2
from webapp2_extras import users
from model.Sale import Sale

class FormAddManager(webapp2.RequestHandler):

    def post(self):

        object_name = self.request.get("object_name")
        login_logout_url = users.users.create_logout_url("/")
        jinja = jinja2.get_jinja2(app=self.app)

        sale = Sale.query(Sale.name_object == object_name)

        template_values = {
            "user":  users.users.get_current_user(),
            "object_name": object_name,
            "sale": list(sale),
            "login_logout_url": login_logout_url
        }

        self.response.write(jinja.render_template("add_sale.html", **template_values))

app = webapp2.WSGIApplication([
    ('/form_add_sale', FormAddManager)
], debug=True)
