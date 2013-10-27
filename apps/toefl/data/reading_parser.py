import simplejson as json
from base_parser import BaseParser


class ReadingParser(BaseParser):

  # parse exam
  def parseExam(self, data):
    paragraphs = []
    questions = []
    question_to_paragraph = []
    question_points = []
    title = data[1]
    for index in range(2, len(data)):
      if data[index].startswith("Paragraph 1:"):
        break
      paragraphs.append(data[index])

    parts = self.splitBy(data[index:], r"Paragraph .*")
    index = 0
    for part in parts:
      i = 0
      for line in part:
        if line.startswith("Paragraph"):
          index, content = self.getInitIndex(line.replace("Paragraph ", "", 1))
          paragraphs[index - 1] = content
        else:
          break
        i += 1

      list = self.splitBy(part[i:], r"[0-9][0-9]?\..*")
      for question in list:
        point = 1
        for line in question:
          words = line.split(" ")
          for j in range(1, len(words) - 1):
            if words[j + 1] == "points":
              point = int(words[i])
              break
        question_points.append(point)
        questions.append(question)
        question_to_paragraph.append(index)
    return self.genJson(title, paragraphs, questions, question_to_paragraph, question_points)

  # Generate json
  def genJson(self, title, paragraphs, questions, question_to_paragraph, question_points):
    result = dict()
    result["type"] = "reading"
    result["title"] = title
    result["image"] = ""
    result["paragraphs"] = paragraphs
    question_list = []
    index = 0
    for line in questions:
      question = dict()
      question["type"] = ""
      question["paragraph"] = question_to_paragraph[index]
      question["point"] = question_points[index]
      question["description"] = line[0]
      question["option"] = line[1:]
      question["answer"] = 0
      question_list.append(question)
    result["questions"] = question_list

    return json.dumps(result, indent=2 * ' ')


