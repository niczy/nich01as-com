import logging

import handlers

class ReadingHandler(handlers.BasePageHandler):

  def get(self):
    tpo1_reading = open('apps/toefl/data/tpo1/reading1_article')
    reading_lines = tpo1_reading.readlines()
    title = reading_lines[0].decode('utf-8').strip()
    tpo1_questions = open('apps/toefl/data/tpo1/reading1_questions')
    questions = [line.decode('utf-8').strip() for line in tpo1_questions.readlines()]
    paragraphs = [line.decode('utf-8').strip() for line in reading_lines[1:]]
    self.render('apps/toefl/reading.html', {'title': title, 'paragraphs': paragraphs, 'questions': questions})
  
