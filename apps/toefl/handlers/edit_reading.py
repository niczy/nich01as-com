import logging

import handlers

class EditReadingHandler(handlers.BasePageHandler):

  def get(self):
    self.render('apps/toefl/edit_reading.html', {})
