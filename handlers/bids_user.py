#coding: utf-8
import webapp2
from webapp2_extras import jinja2
from webapp2_extras import users
from model.Bid import Bid

class BidsUserPage(webapp2.RequestHandler):

    def post(self):

        user_login = users.users.get_current_user().nickname()
        login_logout_url = users.users.create_logout_url("/")

        id_sale = self.request.get("id_sale")

        bids = Bid.query(Bid.login_bid == user_login).order(-Bid.prize_bid)
        bids_user = list()
        for bid in bids:
            if bid.id_sale == id_sale:
                bids_user.append(bid)

        template_values = {
            "user": users.users.get_current_user(),
            "bids_user": bids,
            "login_logout_url":login_logout_url
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("bids_user.html", **template_values))

app = webapp2.WSGIApplication([
    ('/bids_user', BidsUserPage)
], debug=True)