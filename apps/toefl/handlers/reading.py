import logging

import handlers

class ReadingHandler(handlers.BasePageHandler):

  def get(self):
    name = self.request.get('name')
    if name:
      tpo1_reading = open('apps/toefl/data/reading_%s' % name)
      reading_lines = tpo1_reading.readlines()
      title = reading_lines[0].decode('utf-8').strip()
      tpo1_questions = open('apps/toefl/data/reading_question_%s' % name)
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
      self.render('apps/toefl/reading.html', {'title': title, 'paragraphs': paragraphs, 'questions': questions})
    else:
      names = []
      for i in xrange(23):
        for j in xrange(1, 4):
          names.append('tpo%d-%d' % (i, j))
      self.render('apps/toefl/reading_list.html', {'names': names})
  
