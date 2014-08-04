from google.appengine.ext import ndb

class Tag(ndb.Model):

    name = ndb.StringProperty()

class Butter(ndb.Model):

    content = ndb.StringProperty(indexed = False)

    tags = ndb.KeyProperty(repeated = True, kind = Tag)

class User(ndb.Model):

    name = ndb.StringProperty()

    following_tags = ndb.KeyProperty(repeated = True, kind = Tag)
    
