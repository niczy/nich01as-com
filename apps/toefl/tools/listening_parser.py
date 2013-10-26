import simplejson as json
from base_parser import BaseParser


class ListeningParser(BaseParser):
  def parseExam(self, exam):
    questions = self.splitBy(exam, r"[0-9][0-9]?\..*")
    result = dict()
    result["type"] = "listening"
    result["image"] = "xxx.jpg"
    result["audio"] = "yyy"
    result["section"] = questions[0][0] + " " + questions[0][1]
    question_list = list()
    for question in questions[1:]:
      question_dict = dict()
      question_dict["type"] = "multichoice/classify/ordering"
      question_dict["points"] = 1
      question_dict["description"] = question[0]
      question_dict["options"] = question[1:]
      question_dict["answers"] = list()
      question_dict["audio"] = ""
      question_dict["replay_audio"] = ""
      question_list.append(question_dict)
    result["questions"] = question_list

    return json.dumps(result, indent=2 * ' ')

