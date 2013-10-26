import logging

import handlers

class SpeakingHandler(handlers.BasePageHandler):

  def get(self):
      self.render('apps/toefl/speaking.html')
