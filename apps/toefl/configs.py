from handlers.reading import ReadingHandler
from handlers.speaking import SpeakingHandler

handlers = [('/toefl/reading', ReadingHandler),
            ('/toefl/speaking', SpeakingHandler)]

