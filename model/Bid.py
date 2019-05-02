from google.appengine.ext import ndb

class Bid(ndb.Model):
    id_sale = ndb.IntegerProperty()
    prize_bid = ndb.IntegerProperty()
    login_bid = ndb.StringProperty()
    moment_bid = ndb.DateTimeProperty(required=True, indexed=True, auto_now_add=True)
