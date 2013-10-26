import simplejson as json
from base_parser import BaseParser


class WritingParser(BaseParser):
  def parseExam(self, exam):
    if len(exam) < 2:
      return

    result = dict()
    result["type"] = "writing"
    questions = []
    first_dict = dict()
    first_dict["topic"] = ""
    first_dict["audio"] = ""
    first_dict["image"] = ""
    questions.append(first_dict)

    second_dict = dict()
    question = ""
    for line in exam[2:]:
      if len(question) > 0:
        question += '\n'
      question += line
    second_dict["question"] = question
    questions.append(second_dict)
    result["questions"] = questions
    return json.dumps(result, indent=2 * ' ')
