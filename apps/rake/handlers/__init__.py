import logging
import handlers
from third_party.rake import rake

my_rake = rake.Rake('./third_party/rake/SmartStoplist.txt')

class IndexHandler(handlers.BasePageHandler):

    def get(self):
        self.render('apps/rake/index.html')

    def post(self):
        content = self.request.get('content')
        sorted_keywords = my_rake.run(content)
        self.render('apps/rake/index.html', {'tags': sorted_keywords})

