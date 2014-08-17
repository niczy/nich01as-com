import webapp2
import g_search
import json

class ListArticleHandler(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'application/json'  
        keywords = self.request.get('q').split(',')
        self.response.write(json.dumps(g_search.search(keywords)))

