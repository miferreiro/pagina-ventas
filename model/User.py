from google.appengine.ext import ndb

class User(ndb.Model):
    login = ndb.StringProperty(indexed=True)
    password = ndb.StringProperty(indexed=True)

# def create(usr):
#     toret = User()
#     toret.name = usr.name()
#     return toret
#
# def create_empty_user():
#     return User(name="")
#
# @ndb.transactional
# def update(user):
#     return user.put()
#
# def retrieve(usr):
#     toret = None
#     if usr:
#         usr_name = usr.name()
#         found_users = User.query(User.name == usr_name).order(User.name)
#
#         if found_users.count() == 0:
#             toret = create(usr)
#         else:
#             toret = found_users.iter().next()
#             toret.usr = usr
#
#     return toret