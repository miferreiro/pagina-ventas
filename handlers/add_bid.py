#coding: utf-8
import time
import webapp2
from webapp2_extras import jinja2
from webapp2_extras import users
from model.Bid import Bid
from model.Sale import Sale

class AddBid(webapp2.RequestHandler):

    def post(self):

        user = users.users.get_current_user()
        login_bid = user.nickname()
        login_logout_url = users.users.create_logout_url("/")

        id_sale = self.request.get("id_sale")
        prize_bid = self.request.get("prize_bid")
        best_bid = self.request.get("best_bid")

        sale = Sale.query(Sale.id_sale == int(id_sale)).get()
        sale_login = sale.login_sale

        if login_bid != "" and prize_bid != "" and id_sale != "" and int(best_bid) < int(prize_bid) and not sale_login == login_bid :
            bid = Bid(id_sale = int(id_sale), prize_bid = int(prize_bid), login_bid = login_bid)
            bid.put()
            time.sleep(1)

            sale = Sale.query(Sale.id_sale == int(id_sale)).get()
            sale.best_bid = int(prize_bid)

            Sale.put(sale)

            time.sleep(1)
            bids = Bid.query(Bid.id_sale == int(id_sale)).order(-Bid.prize_bid)
            template_values = {
                "user": user,
                "id_sale": id_sale,
                "bids": bids,
                "best_bid": int(prize_bid),
                "login_logout_url":login_logout_url,
                "correct" : "La puja ha sido aceptada"
            }
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("bids.html", **template_values))
        else:
            error = "Se ha producido un error a la hora de pujar"

            if sale_login == login_bid:
                error = "El propietario de la venta no puede realizar pujas"
            elif int(best_bid) >= int(prize_bid):
                error = "No se puede pujar con un valor menor o igual al de la mejor puja"

            bids = Bid.query(Bid.id_sale == int(id_sale)).order(-Bid.prize_bid)

            template_values = {
                "user": user,
                "id_sale": id_sale,
                "bids": bids,
                "best_bid": int(best_bid),
                "login_logout_url":login_logout_url,
                "error" : error
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("bids.html", **template_values))

app = webapp2.WSGIApplication([
    ('/add_bid', AddBid)
], debug=True)
