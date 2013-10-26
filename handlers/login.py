from handlers import BasePageHandler

class LoginHandler(BasePageHandler):

  def get(self):
    self.render('login.html', {'form_url': 'http://www.google.com'})

  def post(self):
    pass
