from handlers.edit_reading import EditReadingHandler
from handlers.reading import ReadingHandler
from handlers.speaking import SpeakingHandler

handlers = [('/toefl/reading', ReadingHandler),
            ('/toefl/speaking', SpeakingHandler),
            ('/toefl/edit_reading', EditReadingHandler)]

