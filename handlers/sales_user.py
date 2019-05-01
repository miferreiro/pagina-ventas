#coding: utf-8
import webapp2
from webapp2_extras import jinja2
from webapp2_extras import users
from model.Sale import Sale
from model.Bid import Bid

class SalesUserPage(webapp2.RequestHandler):

    def get(self):
        user = users.users.get_current_user()
        user_login = user.nickname()
        login_logout_url = users.users.create_logout_url("/")

        bids_user = Bid.query(Bid.login_bid == user_login).order(Bid.prize_bid)
        sales = Sale.query().order(Sale.id_sale)

        sales_user = list()
        best_bids_login = list()
        for sale in sales:
            best_bid = Bid.query(Bid.id_sale == sale.id_sale).order(-Bid.prize_bid).get()
            if best_bid == None:
                best = 0
            else:
                best = best_bid.login_bid
            best_bids_login.append(best)
            for bid in bids_user:
                if bid.id_sale == sale.id_sale:
                    sales_user.append(sale)
                    break

        template_values = {
            "user" : user,
            "sales" : sales_user,
            "best_bids_login" : best_bids_login,
            "login_logout_url" :login_logout_url
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("sales_user.html", **template_values))

app = webapp2.WSGIApplication([
    ('/sales_user', SalesUserPage)
], debug=True)