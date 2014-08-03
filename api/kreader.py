import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from api.api_model import Tag
from api.api_model import TagCollection
from api.api_model import Butter
from api.api_model import ButterCollection
from api.api_model import User
from api import following_tags
from api import butters_in_tag
from api import storage

package = "kreader"


@endpoints.api(name='kreaderservice', version='v1')    
class KReaderApi(remote.Service):

    @endpoints.method(User, User, path='/users', http_method='POST', name='add_user')
    def add_user(sell, request):
        return storage.add_user(request.name)

    @endpoints.method(Butter, Butter, path='/butter', http_method='POST', name='post_butter')
    def post_butter(self, request): 
        return storage.add_butter(request)

    FOLLOW_METHOD_RESOURCE = endpoints.ResourceContainer(
            Tag,
            user_name = messages.StringField(2, variant=messages.Variant.STRING, required=True))
    @endpoints.method(FOLLOW_METHOD_RESOURCE, Tag, path='/{user_name}/tag/follow', http_method='POST', name='follow_tag')
    def follow_tag(self, request):
        storage.follow_tag(request.user_name, request.name)
        return storage.get_tag_by_name(request.name) 

    GET_BUTTERS_METHOD_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            user_name = messages.StringField(2, variant=messages.Variant.STRING, required=True))
    @endpoints.method(GET_BUTTERS_METHOD_RESOURCE, ButterCollection, path='/{user_name}/butters', http_method='GET', name='get_butters_by_user_name')
    def get_butters_by_user_name(self, request):
        return ButterCollection(items = storage.get_butters_by_user_name(request.user_name))

    LIST_FOLLOW_TAG_METHOD_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            user_name = messages.StringField(2, variant=messages.Variant.STRING, required=True))
    @endpoints.method(LIST_FOLLOW_TAG_METHOD_RESOURCE, TagCollection, path='/{user_name}/tags', http_method='GET', name='list_following_tags')
    def list_following_tags(self, request):
        tags = storage.get_following_tags_by_user_name(request.user_name)
        return TagCollection(items = tags)

