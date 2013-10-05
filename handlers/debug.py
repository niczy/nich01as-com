import handlers

class SystemInfoHandler(handlers.BasePageHandler):

  def get(self):
    self.response.write('System info:\n')
    self.response.write(__file__)
    

