import webapp2
import jinja2
import os

from handlers.index import IndexHandler
from handlers.debug import SystemInfoHandler

app = webapp2.WSGIApplication([('/', IndexHandler),
                              ('/debug', SystemInfoHandler)],
                              debug=True)
