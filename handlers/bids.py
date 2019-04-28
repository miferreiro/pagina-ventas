#coding: utf-8
import webapp2
from webapp2_extras import jinja2
from webapp2_extras import users
from model.Bid import Bid

class BidsPage(webapp2.RequestHandler):

    def post(self):

        id_sale = self.request.get("id_sale")
        best_bid = self.request.get("best_bid")
        login_logout_url = users.users.create_logout_url("/")

        bids = Bid.query(Bid.id_sale == int(id_sale)).order(-Bid.prize_bid)

        template_values = {
            "user": users.users.get_current_user(),
            "id_sale": id_sale,
            "bids": bids,
            "best_bid": int(best_bid),
            "login_logout_url":login_logout_url
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("bids.html", **template_values))

app = webapp2.WSGIApplication([
    ('/bids', BidsPage)
], debug=True)