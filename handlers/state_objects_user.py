#coding: utf-8
import webapp2
import datetime
from webapp2_extras import jinja2
from model.Object import Object
from model.Sale import Sale
from webapp2_extras import users

class StatusObjectsUserPage(webapp2.RequestHandler):

    def get(self):

        user_login = users.users.get_current_user().nickname()
        login_logout_url = users.users.create_logout_url("/")

        user_objects = Object.query(Object.login == user_login)
        sales_objects = Sale.query(Sale.login_sale == user_login)
        sales_objects_active_list = []

        for sale in sales_objects:
            if sale.finish_date_sale < datetime.date.today():
                sales_objects_active_list.append(sale)

        objects_in_sale =[]
        for object in user_objects:
            for sale in sales_objects:
                if object.name == sale.name_object:
                    objects_in_sale.append(object)

        template_values = {
            "user": users.users.get_current_user(),
            "user_objects": objects_in_sale,
            "sales_objects": sales_objects,
            "sales_objects_active" : sales_objects_active_list,
            "login_logout_url": login_logout_url
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("status_objects_user.html", **template_values))

app = webapp2.WSGIApplication([
    ('/status_objects_user', StatusObjectsUserPage)
], debug=True)