# -*- encoding: utf-8 -*-
# (C) Copyright 2008 Tarek Ziadé <tarek@ziade.org>
#
import logging
from lxml import etree
import time
import datetime
from pylons import config
from sgmllib import SGMLParser

from yap.lib.base import *
from atomisator.main.config import AtomisatorConfig

log = logging.getLogger(__name__)

class Html2Txt(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.pieces = []

    def handle_data(self, text):
        self.pieces.append(text)

    def handle_entityref(self, ref):
        if ref == 'amp':
            self.pieces.append("&")

    def output(self):
        return ' '.join(self.pieces).replace('<br/>', '')

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
        
        # building an extract
        def _extract(html, title):
            parser = Html2Txt()
            parser.reset()
            parser.feed(html)
            parser.close()
            res = parser.output().strip()
            size = 160 - len(title)
            return res[:size] + '...'            

        for i in items:
            i['extract'] = _extract(i['description'], i['title'])
 
        c.entries = items
        c.title = doc.xpath('/rss/channel/title')[0].text
        # Return a rendered template
        #   return render('/some/template.mako')
        # or, Return a response
        return render('/front.mako')

