#coding: utf-8
import time
import webapp2
import datetime
from webapp2_extras import jinja2
from webapp2_extras import users
from model.Sale import Sale
from model.Object import Object

class AddSale(webapp2.RequestHandler):

    def post(self):

        user = users.users.get_current_user()
        user_login = user.nickname()
        name_object = self.request.get("name_object")
        initial_sale_prize = int(self.request.get("initial_sale_prize"))
        finish_date_sale = str(self.request.get("finish_date_sale"))
        login_logout_url = users.users.create_logout_url("/")

        finish_date_sale = datetime.datetime.strptime(finish_date_sale, "%Y-%m-%d")
        finish_date_sale = datetime.date(finish_date_sale.year, finish_date_sale.month, finish_date_sale.day)

        sale = list(Sale.query(Sale.name_object == name_object))

        if len(sale) != 0:

            user_objects = Object.query(Object.login == user_login)

            template_values = {
                "user": user,
                "user_objects": user_objects,
                "error" : "Ya existe la venta para el objeto: " + name_object,
                "login_logout_url": login_logout_url
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("objectsUser.html", **template_values))
            return

        if name_object != "" and initial_sale_prize != "" and  initial_sale_prize > 0 and finish_date_sale != "" and finish_date_sale >= datetime.date.today():

            sales = Sale.query().order(-Sale.id_sale)
            next_id = 0
            for i in sales:
                next_id = i.id_sale
                break
            next_id = int(next_id) + 1
            sale = Sale(id_sale = next_id, name_object = name_object, initial_sale_prize = initial_sale_prize, finish_date_sale = finish_date_sale,best_bid = initial_sale_prize, login_sale = user_login, sale_delivered = False)
            sale.put()
            time.sleep(1)

            user_objects = Object.query(Object.login == user_login)

            template_values = {
                "user": user,
                "user_objects": user_objects,
                "correct" : "Se ha creado la venta para el objeto: " + name_object,
                "login_logout_url": login_logout_url
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("objectsUser.html", **template_values))
            return

        else:
            error = ""
            if initial_sale_prize <= 0:
                error = "El precio inicial de venta no puede ser negativo"
            elif finish_date_sale < datetime.date.today():
                error = "No se puede crear una venta con una fecha anterior a la actual"
            else:
                error = "Se ha producido un error, no se ha creado la venta"

            jinja = jinja2.get_jinja2(app=self.app)

            sale = Sale.query(Sale.name_object == name_object)

            template_values = {
                "user": user,
                "object_name": name_object,
                "sale": sale,
                "error": error,
                "login_logout_url":login_logout_url
            }
            self.response.write(jinja.render_template("add_sale.html", **template_values))

app = webapp2.WSGIApplication([
    ('/add_sale', AddSale)
], debug=True)
