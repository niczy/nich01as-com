import webapp2
import jinja2
import os
app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
