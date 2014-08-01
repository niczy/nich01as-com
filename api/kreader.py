import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

package = "kreader"

class Article(messages.Message):

    title = messages.StringField(1)

    content = messages.StringField(2)

    tag = messages.StringField(3, repeated = True)

@endpoints.api(name='article', version='v1')    
class KReaderApi(remote.Service):

    @endpoints.method(message_types.VoidMessage, Article, path='/article', http_method='GET', name='article')
    def article(sell, unused_request):
        return Article(content = 'Hello world')

