import logging
from lxml import etree
import time
import datetime
from pylons import config

from yap.lib.base import *
from atomisator.main.config import AtomisatorConfig

log = logging.getLogger(__name__)

class FrontController(BaseController):

    def index(self):
        
        parser = AtomisatorConfig(config.get('atomisator.file'))
         
        # to export as configuration
        xml = parser.file
        doc = etree.XML(open(xml).read())
        items = doc.xpath('/rss/channel/item')
       
        def _date(value):
            d = time.strptime(value, '%Y-%m-%d %H:%M:%S')
            d = datetime.datetime(*d[:6])
            return d.strftime('%d/%m/%Y')

        def _extract(entry):
            if entry.tag == 'pubDate':
                return entry.tag, _date(entry.text)
            if entry.tag == 'title':
                if len(entry.text) > 100:
                    return 'title', entry.text[:100] + '...'
                return 'title', entry.text
            return entry.tag, entry.text 

        items = [dict([_extract(x)
                      for x in e.getchildren()])
                 for e in items]

        c.entries = items
        c.title = doc.xpath('/rss/channel/title')[0].text
        # Return a rendered template
        #   return render('/some/template.mako')
        # or, Return a response
        return render('/front.mako')

