from sqlalchemy import *

db = create_engine('sqlite:///week6.db')

db.echo = True

metadata = BoundMetaData(db)

users = Table('users', metadata, autoload=True)
emails = Table('emails', metadata, autoload=True)


class User(object):
    pass
class Email(object):
    pass

usermapper = mapper(User, users)
emailmapper = mapper(Email, emails)

session = create_session()

garrison = session.query(User).selectfirst(users.c.name=='Garrison')
garrison.age += 1

session.flush()

sarah = User()
sarah.name = 'Sarah'
sarah.age = 37

print ("About to flush() without a save()...")
session.flush()  # Will *not* save Sarah's data yet

session.save(sarah)
print ("Just called save(). Now flush() will actually do something.")
session.flush()  # Now Sarah's data will be saved

session.delete(sarah)
session.flush()