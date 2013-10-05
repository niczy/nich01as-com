
class MainPage(BasePageHandler):

  def get(self):
    self.render('index.html', {'greating': 'Hello world'}


