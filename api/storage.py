
from api.api_model import Tag
from api.api_model import TagCollection
from api.api_model import Butter
from api.api_model import ButterCollection
from api.api_model import User

from api import models 


def add_butter(butter):
    model_butter = add_butter_(butter)
    return to_butter_(model_butter)

def follow_tag(user_name, tag_name):
    model_user = get_user_by_name_(user_name) 
    model_tag = get_tag_by_name_(tag_name)
    if not model_tag.key in model_user.following_tags:
        model_user.following_tags.append(model_tag.key)
        model_user.put()

def get_following_tags_by_user_name(user_name):
    model_tags = get_following_tags_by_user_name_(user_name)
    return [Tag(name = model_tag.name) for model_tag in model_tags]


def get_butters_by_user_name(user_name):
    model_butters = get_butters_by_user_name_(user_name)
    butters = []
    for model_butter in model_butters:
        butters.append(to_butter_(model_butter))
    return butters

def to_butter_(model_butter): 
    tags = []
    for tag_key in model_butter.tags:
        model_tag = tag_key.get()
        tags.append(to_tag_(model_tag))
    return Butter(content = model_butter.content, tags = TagCollection(items = tags))

def to_tag_(model_tag):
    return Tag(name = model_tag.name)

'''
    Return a list of butters stored in db.
'''
def get_butters_by_user_name_(user_name):
    model_butters = []
    model_user = get_user_by_name_(user_name)
    for tag_key in model_user.following_tags:
        model_tag = tag_key.get()
        model_butters.extend(get_butters_by_tag_name_(model_tag.name))
    return model_butters

def add_user(user_name):
    return to_user_(add_user_(user_name))

def add_user_(user_name):
    return models.User(name = user_name).put().get()

def to_user_(model_user):
    return User(name = model_user.name)

def get_following_tags_by_user_name_(user_name):
    model_tags = []
    model_user = get_user_by_name_(user_name)
    if model_user:
        for tag_key in model_user.following_tags:
            model_tags.append(tag_key.get())

    return model_tags


def get_user_by_name_(user_name):
    model_users = models.User.query(models.User.name == user_name).fetch()
    if model_users:
        return model_users[0]
    return None


def add_butter_(butter):
    keys = []
    for tag in butter.tags.items:
        keys.append(add_tag_(tag).key)
    db_butter = models.Butter(content = butter.content, tags = keys)
    key = db_butter.put()
    return key.get()

def add_tag_(tag):
    model_tag = get_tag_by_name_(tag.name) 
    if model_tag:
        return model_tag 
    else:
        db_tag = models.Tag(name = tag.name)
        return db_tag.put().get()

def get_tag_by_name(tag_name):
    return to_tag_(get_tag_by_name_(tag_name))
def get_tag_by_name_(name):
    model_tags = models.Tag.query(models.Tag.name == name).fetch()
    if len(model_tags) > 0:
        return model_tags[0]
    return None

def get_butters_by_tag_name_(tag_name):    
    model_tag = get_tag_by_name_(tag_name)
    if model_tag:
        return models.Butter.query(models.Butter.tags == model_tag.key).fetch()
    else:
        return [] 

        
