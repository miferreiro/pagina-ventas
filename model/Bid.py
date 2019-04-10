from google.appengine.ext import ndb

class Bid(ndb.Model):
    objetos = ndb.StringProperty()
    pujas = ndb.StringProperty()