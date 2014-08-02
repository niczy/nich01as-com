from test.api.base_model_test import ModelTestCase
from api import storage
from api.api_model import Tag
from api.api_model import TagCollection
from api.api_model import Butter
from api.api_model import ButterCollection

from api import models

class StorageTest(ModelTestCase):

    def testAddTag(self):
        tag = Tag(name = 'tag')
        self.assertEquals('tag', storage.add_tag_(tag).name)

        tag = Tag(name = 'tag')
        storage.add_tag_(tag)

        tags = models.Tag.query().fetch()
        self.assertEquals(1, len(tags))

    def testAddButter(self):
        tag1 = Tag(name = 'tag1')
        tag2 = Tag(name = 'tag2')
        tag_collection = TagCollection(items = [tag1, tag2]) 
        butter = Butter(content = 'hello', tags = tag_collection)
        model_butter = storage.add_butter_(butter)
        self.assertEquals(2, len(model_butter.tags))
        model_butters = storage.get_butters_by_tag_name_('tag1')
        self.assertEquals(1, len(model_butters))

        tag1 = Tag(name = 'tag1')
        tag2 = Tag(name = 'tag3')
        tag_collection = TagCollection(items = [tag1, tag2]) 
        butter = Butter(content = 'hello', tags = tag_collection)
        model_butter = storage.add_butter_(butter)
        model_butters = storage.get_butters_by_tag_name_('tag1')
        self.assertEquals(2, len(model_butters))

        model_butters = storage.get_butters_by_tag_name_('tag2')
        self.assertEquals(1, len(model_butters))

    def testAddUser(self):
        user_name = 'nicholas'
        storage.add_user_(user_name)
        model_user = storage.get_user_by_name_(user_name)
        self.assertEquals(user_name, model_user.name)

    def testFollowTag(self):
        user_name = 'nicholas'
        storage.add_user_(user_name)
        model_user = storage.get_user_by_name_(user_name)
        self.assertEquals(user_name, model_user.name)

        tag = Tag(name = 'tag1')
        storage.add_tag_(tag)

        storage.follow_tag(user_name, 'tag1')

        model_tags = storage.get_following_tags_by_user_name_(user_name)
        self.assertEquals(1, len(model_tags))
        tags = storage.get_following_tags_by_user_name(user_name)
        self.assertEquals(1, len(tags))

    def testGetButtersByUser(self):
        user_name = 'nicholas'
        storage.add_user_(user_name)
        model_user = storage.get_user_by_name_(user_name)
        self.assertEquals(user_name, model_user.name)

        tag = Tag(name = 'tag1')
        storage.add_tag_(tag)

        storage.follow_tag(user_name, 'tag1')

        tag1 = Tag(name = 'tag1')
        tag2 = Tag(name = 'tag3')
        tag_collection = TagCollection(items = [tag1, tag2]) 
        expected_butter0 = Butter(content = 'hello', tags = tag_collection)
        model_butter = storage.add_butter_(expected_butter0)

        tag_collection = TagCollection(items = [tag1]) 
        expected_butter1 = Butter(content = 'hello3', tags = tag_collection)
        model_butter = storage.add_butter_(expected_butter1)

        model_butters = storage.get_butters_by_user_name_(user_name)
        self.assertEquals(2, len(model_butters))

        butters = storage.get_butters_by_user_name(user_name)
        self.assertEquals(2, len(butters))
        butter0 = butters[0]
        butter1 = butters[1]
        self.assertEquals(butter0, expected_butter0)
        self.assertEquals(butter1, expected_butter1)










