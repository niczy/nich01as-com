#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
import re
import json
from optparse import OptionParser

from string import Template
from sets import Set

class Util:

  @staticmethod
  def sentence_similarity(s1, s2):
    return Util.jaccard_sim(Set(s1.split()), Set(s2.split()))

  @staticmethod
  def jaccard_sim(s1, s2):
    return len(s1.intersection(s2)) * 1.0 / len(s1.union(s2))

class Question:
  def __init__(self):
    self.description = ''
    self.options = []
    self.answercount = 1
    self.paragraphs = []
    self.highlight = ''
    self.answer = None
    self.highlight_sentence = ''
    self.id = 0

  def post_process(self, article):
    # paragraph 5
    # paragraph 5 and 6
    # paragraph 5 and paragraph 6
    m = re.search('paragraph (\d+)\.*( and( paragraph)? )?(\d+)?', self.description.lower())
    if m:
      self.add_paragraph(m.group(1))
      self.add_paragraph(m.group(4))
    self.paragraphs.sort()
    m = re.search('The word ["]?(\w+)["]?', self.description)
    if m:
      self.highlight = m.group(1)
    else:
      m = re.search('The phrase "(.*)"', self.description)
      if m:
        self.highlight = m.group(1)
    if 'highlighted sentence' in self.description:
      self.find_highlighted_sentence(article)

  def find_highlighted_sentence(self, article):
    best_score = 0
    best_sentence = ''
    sec_best = 0
    for paragraph in article.paragraphs:
      sentences = paragraph.split('.')
      for s in sentences:
        score = 0
        for o in self.options:
          score += Util.sentence_similarity(s, o)
        if score > best_score:
          if best_score > 0:
            sec_best = best_score
          best_score = score
          best_sentence = s
      # print best_score, sec_best
    self.highlight_sentence = re.sub('^\s*', '', best_sentence)  # THIS IS DONE
    for i in xrange(len(article.paragraphs)):
      if self.highlight_sentence in article.paragraphs[i]:
        sentence = self.highlight_sentence
        if sentence + '.' in article.paragraphs[i]:
          sentence = sentence + '.'
          if article.name == 'tpo20-3':
            print(sentence)
        article.paragraphs[i] = article.paragraphs[i].replace(
          sentence, Article.highlight_template.substitute(Article.highlight_template, word = sentence, qidx = self.id + 1))

  def add_paragraph(self, p):
    if not p: return
    p = int(p)
    if p not in self.paragraphs: self.paragraphs.append(p)

class Answer:
  def __init__(self):
    self.choices = []
    # For Two-classes classification problems.
    self.choices2 = []

  @staticmethod
  def from_string(text):
    text = text[(text.find('.') + 1):]
    if text.endswith(','): text = text[:-1]
    a = Answer()
    if ';' in text:
      text, text2 = text.split(';')
      a.choices2 = [int(c) for c in text2.split(':')]
    a.choices = [int(c) for c in text.split(':')]
    return a

class Article:
  highlight_template = Template('<span class="question-highlight-$qidx">$word</span>')

  def __init__(self):
    self.name = ""
    self.title = ""
    self.paragraphs = []
    self.questions = []
  
  def to_json(self):
    return json.dumps(self.__dict__, indent=4)

  def post_process(self):
    for i in xrange(len(self.questions)):
      q = self.questions[i]
      q.id = i
      if i > 0 and len(q.paragraphs) == 0:
        q.paragraphs = self.questions[i - 1].paragraphs
      q.post_process(self)
      if q.highlight and q.paragraphs:
        pidx = q.paragraphs[0]
        self.paragraphs[pidx - 1] = self.paragraphs[pidx - 1].replace(
            q.highlight, Article.highlight_template.substitute(Article.highlight_template, word = q.highlight, qidx = i+1))

def post_process_question(previous_question, question, paragraphs):
  if paragraphs:
    question.paragraphs = paragraphs
    return
  question.post_process()
  if previous_question and len(question.paragraphs) == 0:
        question.paragraphs = previous_question.paragraphs


def output(articles):
  value_index = ['X', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
  paragraph_template = Template('<p><span class="$questions paragraph-indicator hidden">&#9733;</span>$paragraph</p>\n')
  question_des_template = Template('<span class="description">$description</span>\n')
  option_template = Template('''
   <li class="choice">
      <input type="$input_type" $right_answer_class name="$name" value="$value">
        $option
      </input>
    </li>''')
  paragraph_indicator_template = Template('')
  options_template = Template('''<ul>$options\n</ul>\n\n''')
  for article in articles:
    with open("reading_" + article.name, "w") as output_file:
      output_file.write(article.title + '\n')
      paragraphidx = 0
      for paragraph in article.paragraphs:
        paragraphidx = paragraphidx + 1
        questions = ''
        questionidx = 0
        for question in article.questions:
          questionidx = questionidx + 1
          if paragraphidx in question.paragraphs:
            if questions: questions = questions + ' '
            questions = questions + 'question-' + str(questionidx)
        output_file.write(paragraph_template.substitute(paragraph = paragraph, questions = questions))

    with open('reading_question_' + article.name, "w") as output_file:
      answerid = 0;
      for question in article.questions:
        answerid = answerid + 1
        output_file.write(question_des_template.substitute(description = question.description))
        options = ''
        optionid = 0
        for option in question.options:
          optionid = optionid + 1
          right_answer_class = 'class="right-answer"' if question.answer and optionid in question.answer.choices else ''
          input_type = 'radio'
          "TODO(charlie): the answer is missing"
          if question.answer:
            input_type = 'radio' if len(question.answer.choices) == 1 else 'checkbox'
          options = options + option_template.substitute(
              option = option, name = 'answer-' + str(answerid), value = value_index[optionid], right_answer_class = right_answer_class, input_type = input_type)
        output_file.write(options_template.substitute(options = options))

def parse_articles(filename):
  article = None
  question = None
  articles = []
  state = "init"
  paragraphs = []
  ignored_paragraph = ''

  intert_template = Template('<span class="question-$questionid question-highlight-$questionid hidden">$value</span>')
  values = ['A', 'B', 'C', 'D']
  with open(filename) as input_file:
    for line in input_file.readlines():
      line = line.strip().replace('．', '. ').replace('”', '"').replace('“', '"').replace('：', ':')
        
      if  re.match('TPO\d+-\d:?', line, re.IGNORECASE):
        if article:
          if question:
            article.questions.append(question)
            question = None
          articles.append(article)
        article = Article()
        article.name = line.replace(':', '').lower()
        state = 'name'
      elif state == 'name':
        article.title = line
        state = 'title'
      elif (line.startswith('○') or line.startswith('O') and len(line) > 4) and state in ['question', 'option', 'ignore']:
        state = 'option'
        line = line.replace('○', '')
        line = re.sub('^[O]?\s*', '', line)
        question.options.append(line)
      elif '●' in line or ('O ' in line and len(line) < 4):
        question.answercount = question.answercount + 1
      elif 'Look at the four squares' in line and state in ['option', 'ignore', 'paragraph']:
        state = 'intertion-1'
        if question:
          article.questions.append(question)
        m = re.search('\s*Paragraph (\d+):\s*', ignored_paragraph)
        if m:
          block = '■'
          if '█' in ignored_paragraph:
            block = '█'
          elif '【】' in ignored_paragraph:
            block = '【】'
          line = line.replace('█', 'A').replace('■', 'A').replace('[A]', 'A').replace('【】', 'A').replace('HI', 'A').replace('[Ⓐ] [Ⓑ] [Ⓒ] and [Ⓓ]', 'A').replace('III', 'A')
          questionid = len(article.questions) + 1
          for i in xrange(4):
            ignored_paragraph = ignored_paragraph.replace(block, intert_template.substitute(questionid = questionid, value = values[i]), 1)
          paragraphidx = int(m.group(1))
          ignored_paragraph = re.sub('\s*Paragraph (\d+):\s*', '', ignored_paragraph)
          article.paragraphs[paragraphidx - 1] = ignored_paragraph
        
        question = Question()
        question.paragraphs = paragraphs
        question.options.append('A')
        question.options.append('B')
        question.options.append('C')
        question.options.append('D')
        paragraphs = []
        line = re.sub('^[\s]*\d+\.?\s*', '', line)
        question.description = line
        
      elif state == 'intertion-1':
        state = 'intertion-2'
        question.description = question.description + '\n<quote><b>' + line + '</b></quote>'
      elif state == 'intertion-2':
        state = 'option'
        question.description = question.description + '\n' + line
      elif re.match('Paragraph \d+.*', line):
        state = "ignore"
        if re.match('Paragraph (\d+)—(\d+).*', line):
          m = re.search('Paragraph (\d+)—(\d+).*', line)
          for x in xrange(int(m.group(1)), int(m.group(2)) + 1):
            paragraphs.append(x)
        else:
          paragraphs.append(int(re.search('Paragraph (\d+).*', line).group(1)))
        ignored_paragraph = line
      elif line.isspace():
        state = "ignore"
      elif re.match('\d+[\.].*', line) and state in ['ignore', 'paragraph', 'option', 'intertion-3']:
        if question:
          article.questions.append(question)
        question = Question()
        question.paragraphs = paragraphs
        paragraphs = []
        if state != 'question':
          line = re.sub('^[\s]*\d+\.?\s*', '', line)
        question.description = line
        state = 'question'
      elif re.match('Paragraph \d+.*', line) or line.isspace():
        state = "ignore"
      elif state == 'question':
        question.description = question.description + '<p>' + line + '</p>'
      elif state == 'title' or state == 'paragraph':
        article.paragraphs.append(line)
        state = 'paragraph'

  if article:
    if question:
      article.questions.append(question)
    articles.append(article)

  [a.post_process() for a in articles]
  return articles

def sanity_check_answers(answers):
  idx = 0
  if len(answers) < 13 or len(answers) > 14:
    return False
  for a in answers:
    idx += 1
    if not (a.startswith(str(idx) + '.') or a.startswith(str(idx) + '-')):
      return False
  return True

def parse_answers(filename, articles):
  f = open(filename)
  text = f.read()
  f.close()
  tpos = text.split('TPO')[1:]
  answer_sets = []
  for t in tpos:
    answers = [a for a in t.split('--') if len(a) > 0][:3]
    for a in answers:
      answer_sets.append(a)

  idx = -1
  for answer_set in answer_sets:
    idx += 1
    name = "tpo%d-%d" % ((idx / 3) + 1, idx % 3 + 1)
    answers = [a for a in answer_set.split() if len(a) > 0 and '.' in a]
    assert sanity_check_answers(answers), "Wrong answer format:" + str(answers)
    matches = [a for a in articles if a.name == name]
    if len(matches) == 0:
      print "ERROR: Can't find article for " + name
      continue
    article = matches[0]
    # TODO assert len(article.questions) == len(answers)

    # TODO
    for qid in xrange(min(len(answers), len(article.questions))):
        article.questions[qid].answer = Answer.from_string(answers[qid])

  return articles


def to_json(o):
  dic = o.__dict__
  dic['__type__'] = o.__class__.__name__
  return dic

def from_json(dct):
  y = eval(dct['__type__'])()
  del dct['__type__']
  y.__dict__ = dct
  return y
        
if __name__ == '__main__':
  parser = OptionParser()
  parser.add_option("-f", "--file", dest="filename", default='articles.txt',
                    help="input file. e.g. articles.txt")
  parser.add_option("-j", "--json", dest="jsonfile", default='articles.json',
                    help="output JSON file. e.g. articles.json")
  parser.add_option("-w", "--answers", dest="answers", default='answers.txt',
                    help="input file for answers.")
  parser.add_option("-a", "--action", dest="action", default='json',
                    help="json|html")

  (options, args) = parser.parse_args()
  if options.action == 'json':
    articles = parse_articles(options.filename)
    articles = parse_answers(options.answers, articles)
    with open(options.jsonfile, 'w') as f:
      f.write(json.dumps(articles, default=to_json, indent=4, encoding='utf-8'))
  else:
    with open(options.jsonfile) as f:
      articles = json.loads(f.read(), object_hook=from_json, encoding='utf-8')
      output(articles)
