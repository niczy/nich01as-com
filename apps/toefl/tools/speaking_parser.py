import simplejson as json
from base_parser import BaseParser


class SpeakingParser(BaseParser):
  def parseExam(self, exam):
    questions = self.splitBy(exam, r"Task[0-9][0-9]?.*")
    result = dict()
    result["type"] = "listening"
    questions_list = []
    for question in questions[1:]:
      # pre organize each line
      for index in range(0, len(question) - 1):
        if question[index] == "Question" or question[index] == "Question:":
          question[index + 1] = question[index] + question[index + 1]

      for index in range(0, len(question) - 1):
        if question[index] == "Question" or question[index] == "Question:":
          del question[index]

      question_dict = dict()
      if question[1].startswith("Reading materials"):
        question_dict["audio1"] = "audio_key_xxx"
        question_dict["passage_title"] = question[2]
        question_dict["passage"] = question[3]
        question_dict["audio2"] = "audio_key_xxx"
        question_dict["image"] = "image_url"
        question_dict["question"] = question[4]
        question_dict["audio3"] = "audio_key_xxx"
      elif question[1].startswith("Question"):
        question_dict["audio1"] = "audio_key_xxx"
        question_dict["image"] = "image_url"
        question_dict["question"] = question[1]
        question_dict["audio2"] = "audio_key_xxx"
      else:
        question_dict["topic"] = "question[1]"
        question_dict["audio"] = "audio_key_xxx"
      questions_list.append(question_dict)
    result["questions"] = questions_list

    return json.dumps(result, indent=2 * ' ')
