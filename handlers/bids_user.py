#coding: utf-8
import webapp2
from webapp2_extras import jinja2
from webapp2_extras import users
from model.Sale import Sale
from model.Bid import Bid

class BidsUserPage(webapp2.RequestHandler):
    def get(self):
        user_login = users.users.get_current_user().nickname()
        login_logout_url = users.users.create_logout_url("/")

        bids_user = Bid.query(Bid.login_bid == user_login).order(Bid.prize_bid)
        sales = Sale.query().order(Sale.id_sale)

        sales_user = list()
        for sale in sales:
            for bid in bids_user:
                if bid.id_sale == sale.id_sale:
                    sales_user.append(sale)

        template_values = {
            "user": users.users.get_current_user(),
            "sales": sales_user,
            "bids_user": bids_user,
            "login_logout_url":login_logout_url
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("bids_user.html", **template_values))

app = webapp2.WSGIApplication([
    ('/bids_user', BidsUserPage)
], debug=True)