import re
import os
import glob


class BaseParser:

  _SPECIAL_ = {"\\uc0\\u9675": "",
         "\\uc0\\u9608": "<BLOCK>",
         "\\ul": "<b q=\"\">",
         "\\ulnone": "</b>",
         "\\cb2": "<hl>",
         "\\cb1": "</hl>",
         "\\'92": "'",
         "\\'93": ' \"',
         "\\'94": '\" ',
         "\\'97": "--"}

  # filter some unnecessary chars and prepare for parsing
  def prepare(self, data):
    new_data = []
    for line in data:
      line = self.forwardUlnone(line)

      if line.startswith("{\\") or len(line) == 0:
        continue
      for key in self._SPECIAL_:
        if key in line:
          line = line.replace(key, self._SPECIAL_[key])

      words = line.split(" ")
      new_line = ""
      for word in words:
        if word.startswith("\\"):
          continue
        if len(word) != 0:
          new_line += " " + word
      new_line = new_line.strip()
      if len(new_line) == 0:
        continue
      if new_line.endswith("\\"):
        new_line = new_line[:-1]
      new_data.append(new_line)
    return new_data

  # parse: section=listening/reading/writing/speaking
  def parse(self, folder, section):
    os.chdir(folder)
    files = glob.glob(section + "_*.rtf")
    for filename in files:
      print "Open %s" % filename
      with open(filename) as file:
        output_file = open(filename + ".json", "w")
        data = file.readlines()
        data = self.prepare(data)

        exams = self.splitBy(data, "TPO")
        for exam in exams:
          output = self.parseExam(exam)
          if output is not None:
            output_file.write(output)
        output_file.close()

  def parseExam(self, exam):
    print "need to be override!"

  # Divide data by lines which matches regex
  def splitBy(self, data, regex):
    list = []
    part = []
    for line in data:
      if re.match(regex,line):
        if len(part) > 0:
          list.append(part)
          part = []
      part.append(line)
    if len(part) > 0:
      list.append(part)
    return list

  # Move \ulnone forward if the previous character is in _SPECIAL_
  def forwardUlnone(self, line):
    for m in re.finditer("ulnone", line):
      left = line[:m.start() - 1]
      right = line[m.start() - 1:]

      for key in self._SPECIAL_:
        while left.endswith(" "):
          left = left[:-1]
        if left.endswith(key):
          line = left[::-1].replace(key[::-1], "\\ulnone"[::-1], 1)[::-1] + \
            right.replace("\\ulnone", key, 1)
    return line

  # Parse the index in format of "[0-9][0-9]?."
  def getInitIndex(self, line):
    parts = line.split(":")
    if re.match("[0-9][0-9]?", parts[0]):
      return int(parts[0]), parts[1].strip()

