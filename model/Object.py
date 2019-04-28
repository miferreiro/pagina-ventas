from google.appengine.ext import ndb

class Object(ndb.Model):
    name = ndb.StringProperty(indexed=True)
    description = ndb.StringProperty(indexed=True)
    login = ndb.StringProperty(indexed=True)
    win_on_sale = ndb.BooleanProperty(indexed=True)
