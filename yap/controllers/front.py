import logging
from lxml import etree
import time
import datetime

from yap.lib.base import *

log = logging.getLogger(__name__)

class FrontController(BaseController):

    def index(self):
        
        # to export as configuration
        xml = '/Volumes/MacDev/svn.afpy.org/atomisator.afpy.org/buildout/afpy.xml'
        
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

