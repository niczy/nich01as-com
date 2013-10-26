import sys
from reading_parser import ReadingParser
from listening_parser import ListeningParser
from writing_parser import WritingParser
from speaking_parser import SpeakingParser


def main():
    ListeningParser().parse("../exams", "listening")
    ReadingParser().parse("../exams", "reading")
    WritingParser().parse("../exams", "writing")
    SpeakingParser().parse("../exams", "speaking")

if __name__ == "__main__":
    sys.exit(main())
