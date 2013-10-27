#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
import re

from string import Template


class Question:
  def __init__(self):
    self.description = ""
    self.options = []
    self.answercount = 1

class Article:

  def __init__(self):
    self.name = ""
    self.title = ""
    self.paragraphs = []
    self.questions = []

def output(articles):
  value_index = ['X', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
  paragraph_template = Template('<p>$paragraph</p>\n')
  question_des_template = Template('<span class="description">$description</span>\n')
  option_template = Template('''
   <li class="choice">
      <input type="radio" name="$name" value="$value">
        $option
      </input>
    </li>''')
  options_template = Template('''<ul>$options\n</ul>\n\n''')
  for article in articles:
    with open("reading_" + article.name, "w") as output_file:
      output_file.write(article.title + '\n')
      for paragraph in article.paragraphs:
        output_file.write(paragraph_template.substitute(paragraph = paragraph))

    with open('reading_question_' + article.name, "w") as output_file:
      for question in article.questions:
        output_file.write(question_des_template.substitute(description = question.description))
        options = '';
        answerid = 0;
        for option in question.options:
          answerid = answerid + 1
          options = options + option_template.substitute(option = option, name = 'answer-' + str(answerid), value = value_index[answerid])
        output_file.write(options_template.substitute(options = options))
        

def main(filename):
  article = None
  question = None
  articles = []
  state = "init"
  with open(filename) as input_file:
    for line in input_file.readlines():
      line = line.strip().replace('．', '. ') 
        
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
      elif '●' in line or ('O ' in line and len(line) < 2):
        question.answercount = question.answercount + 1
      elif 'Look at the four squares' in line and state in ['option', 'ignore', 'paragraph']:
        state = 'intertion-1'
        if question:
          article.questions.append(question)
        question = Question()
        question.description = line
      elif state == 'intertion-1':
        state = 'intertion-2'
        question.description = question.description + line
      elif state == 'intertion-2':
        state = 'option'
        question.description = question.description + line
      elif re.match('\d+[\.].*', line) and state in ['ignore', 'paragraph', 'option', 'intertion-3']:
        state = 'question'
        if question:
          article.questions.append(question)
        question = Question()
        question.description = line
      elif (line.startswith('○') or 'O ' in line) and state in ['question', 'option', 'ignore']:
        state = 'option'
        question.options.append(line)
      elif re.match('Paragraph \d+.*', line) or line.isspace():
        state = "ignore"
      elif state == 'question':
        question.description = question.description + line
      elif state == 'title' or state == 'paragraph':
        article.paragraphs.append(line)
        state = 'paragraph'

  if article:
    if question:
      article.questions.append(question)
    articles.append(article)

  output(articles)

if __name__ == '__main__':
  main("articles.txt")
