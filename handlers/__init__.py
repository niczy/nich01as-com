import os

import jinja2
import webapp2

"""Config the template directory, which is '../template' """
current_dir = os.path.dirname(__file__)
JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.join(current_dir, '..', 'template')))


class BasePageHandler(webapp2.RequestHandler):

  def render(self, template_name, template_values):
    template = JINJA_ENVIRONMENT.get_template(template_name)
    self.response.write(template.render(template_values))






