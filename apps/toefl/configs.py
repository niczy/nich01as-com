from handlers.edit_reading import EditReadingHandler
from handlers.reading import ReadingHandler
from handlers.reading import ReadingListHandler
from handlers.speaking import SpeakingHandler

handlers = [('/toefl/reading', ReadingListHandler),
            ('/toefl/reading/(tpo.*)', ReadingHandler),
            ('/toefl/speaking', SpeakingHandler),
            ('/toefl/edit_reading', EditReadingHandler)]

