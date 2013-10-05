from handlers import BasePageHandler

class IndexHandler(BasePageHandler):

  def get(self):
    self.render('index.html', {'greating': 'Hello world'})
