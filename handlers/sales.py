#coding: utf-8
import webapp2
import datetime
from webapp2_extras import jinja2
from webapp2_extras import users
from model.Sale import Sale
from model.Bid import Bid
from model.Object import Object

class SalesPage(webapp2.RequestHandler):

    def get(self):

        user = users.users.get_current_user()
        login_logout_url = users.users.create_logout_url("/")

        sales = Sale.query()
        sales_recent = list()

        sales_old = list()
        for sal in sales:
            if (sal.finish_date_sale - datetime.date.today()).days < 0 and not sales_old:
                sales_old.append(sal)

        for sale in sales_old:

            sale.sale_delivered = True
            sale.put()

            bids = Bid.query(Bid.id_sale == sale.id_sale).order(-Bid.prize_bid)
            for bid in bids:
                best_bid = bid
                break

            objects = Object.query(Object.name == sale.name_object)
            for obj in objects:
                sale_obj = obj
                break

            sale_obj.login = best_bid.login_bid
            sale_obj.win_on_sale = True
            sale_obj.put()

        for sal in sales:
            if (sal.finish_date_sale - datetime.date.today()).days >= 0 :
                sales_recent.append(sal)

        template_values = {
            "user": user,
            "sales": sales_recent,
            "login_logout_url" :login_logout_url
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("sales.html", **template_values))

app = webapp2.WSGIApplication([
    ('/sales', SalesPage)
], debug=True)
