# -*- encoding: utf-8 -*-
# (C) Copyright 2008 Tarek Ziadé <tarek@ziade.org>
#
import logging
import os
from os.path import join
import shutil
from lxml import etree
import time
import datetime
from pylons import config
from sgmllib import SGMLParser

from yap.lib.base import *
from atomisator.main.config import AtomisatorConfig

TITLESIZE = 70
MAXSIZE = 150
log = logging.getLogger(__name__)
root = os.path.split(os.path.dirname(__file__))[0]
PUBLIC_RSS = os.path.realpath(join(root, 'public', 'rss.xml'))
CONFIG = join(root, 'atomisator.cfg')

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
        parser = AtomisatorConfig(CONFIG)
        
        # getting parameters for the rss output
        rss = dict(parser.outputs)['rss']

        # getting the target xml file
        rss_file = rss[0]
        xml = os.path.realpath(rss_file)
        if not os.path.exists(xml):
            xml = os.path.realpath(join(root, rss_file))
            if not os.path.exists(xml):
                raise ValueError('File %s not found' % xml)

        # if not under public, we need to copy it to public/rss.xml
        if xml != PUBLIC_RSS:
            shutil.copyfile(xml, PUBLIC_RSS)

        doc = etree.XML(open(xml).read())
        items = doc.xpath('/rss/channel/item')
       
        def _date(value):
            d = time.strptime(value.split('.')[0], '%Y-%m-%d %H:%M:%S')
            d = datetime.datetime(*d[:6])
            return d.strftime('%d/%m/%Y')

        def _extract(entry):
            if entry.tag == 'pubDate':
                return entry.tag, _date(entry.text)
            if entry.tag == 'title':
                if len(entry.text) > TITLESIZE:
                    return 'title', entry.text[:TITLESIZE] + '...'
                return 'title', entry.text
            return entry.tag, entry.text 

        items = [dict([_extract(x)
                      for x in e.getchildren()])
                 for e in items]
        
        # building an extract
        def _extract(html, title):
            if isinstance(html, unicode):
                try:
                    html = html.decode('utf8')
                except:
                    html = str(type(html))
            parser = Html2Txt()
            parser.reset()
            parser.feed(html)
            parser.close()
            res = parser.output().strip()
            size = MAXSIZE - len(title)
            if size < 0:
                return ''
            return res[:size] + '...'            

        for i in items:
            i['extract'] = _extract(i['description'], i['title'])
 
        c.entries = items
        c.title = doc.xpath('/rss/channel/title')[0].text
        return render('/front.mako')

