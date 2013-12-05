import logging

import handlers

class ReadingListHandler(handlers.BasePageHandler):

  def get(self):
    names = []
    for i in xrange(1, 25):
      for j in xrange(1, 4):
        names.append('tpo%d-%d' % (i, j))
    self.render('apps/toefl/reading_list.html', {'names': names, 'mobileApp': self.request.get('mobileApp') == 'True'})

class ReadingHandler(handlers.BasePageHandler):

  def get(self, name):
    tpo1_reading = open('apps/toefl/data/reading/reading_%s.data' % name)
    reading_lines = tpo1_reading.readlines()
    title = reading_lines[0].decode('utf-8').strip()
    tpo1_questions = open('apps/toefl/data/reading/reading_question_%s.data' % name)
    question = ''
    questions = []
    for question_line in tpo1_questions.readlines():
      if question_line.isspace():
        if not question.isspace():
          questions.append(question.decode('utf-8').strip())
          question = ''
      else:
        question = question + question_line
    if len(question) > 0:
      questions.append(question.decode('utf-8').strip())
    paragraphs = [line.decode('utf-8').strip() for line in reading_lines[1:]]
    tpo1_reading.close()
    tpo1_questions.close()
    self.render('apps/toefl/reading.html',
        {'title': title, 'paragraphs': paragraphs, 'questions': questions, 'mobileApp': self.request.get('mobileApp') == 'True'})
        
