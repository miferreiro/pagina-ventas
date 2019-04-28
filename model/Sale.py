from google.appengine.ext import ndb

class Sale(ndb.Model):
    id_sale = ndb.IntegerProperty()
    name_object = ndb.StringProperty()
    initial_sale_prize = ndb.IntegerProperty()
    finish_date_sale = ndb.DateProperty()
    best_bid = ndb.IntegerProperty()
    login_sale = ndb.StringProperty()
    sale_delivered = ndb.BooleanProperty()

