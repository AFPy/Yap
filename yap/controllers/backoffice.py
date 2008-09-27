# -*- encoding: utf-8 -*-
# (C) Copyright 2008 Tarek Ziadé <tarek@ziade.org>
#
from os.path import join
import os
import logging
from routes.util import redirect_to

from yap.lib.base import *
from atomisator.main.config import AtomisatorConfig
from pylons import request

root = os.path.split(os.path.dirname(__file__))[0] 
CONFIG = join(root, 'atomisator.cfg')
log = logging.getLogger(__name__)

class BackofficeController(BaseController):

    def _get_values(self, parser):
        rss = dict(parser.outputs)['rss']
        file_ = rss[0]
        if len(rss) > 1:
            link = rss[1]
        else:
            link = ''
        if len(rss) > 2:
            title = rss[2]
        else:
            title = ''
        if len(rss) > 3:
            description = rss[3]
        else:
            description = ''
        return file_, link, title, description
  
    def _set_values(self, parser, file_, link, title, description):
        parser.outputs = [('rss', (file_, link, title, description))]

    def index(self):
        c.title = 'Backoffice'
        parser = AtomisatorConfig(CONFIG)
        c.atomisator = {}

        # getting parameters for the rss output
        file_, link, title, description = self._get_values(parser)
        c.atomisator['title'] = title
        s = [s[0] + ' ' + ' '.join(s[1]) 
             for s in parser.sources]

        c.atomisator['sources'] = '\n'.join(s)
        c.atomisator['database'] = parser.database
        c.atomisator['description'] = description
        c.atomisator['link'] = link
        
        s = [s[0] + ' ' + ' '.join(s[1]) 
             for s in parser.filters]
        c.atomisator['filters'] = '\n'.join(s)    
 
        s = [s[0] + ' ' + ' '.join(s[1]) 
             for s in parser.enhancers]
        
        c.atomisator['enhancers'] = '\n'.join(s)    
 
        return render('/backoffice.mako')

    
    def update(self):
        parser = AtomisatorConfig(CONFIG)
        # getting parameters for the rss output
        file_, link, title, description = self._get_values(parser)
      
        # TODO make atomisator cfg file read/writeable by text
        # to avoid all this crappy parsing
        _get = request.GET.get
        title = _get('title', title)
        link = _get('link', link)
        description = _get('description', description)
        self._set_values(parser, file_, link, title, description)

        parser.database = _get('database', parser.database)

        current = ['%s %s'.strip() % (p[0], ' '.join(p[1])) 
                   for p in parser.filters]
        
        filters = _get('filters', '\n'.join(current))
        filters = [f for f in [s.strip() 
                   for s in filters.split('\n')] if f != '']
        filters = [(u[0], tuple(u[1:])) 
                   for u in [f.split() for f in filters]]
        if filters != parser.filters:
            parser.filters = filters

        current = ['%s %s'.strip() % (p[0], ' '.join(p[1])) 
                   for p in parser.enhancers]
        
        enhancers = _get('enhancers', '\n'.join(current))
        enhancers = [f for f in [s.strip() 
                     for s in enhancers.split('\n')]
                    if f != '']
        enhancers = [(u[0], tuple(u[1:])) 
                     for u in [f.split() for f in enhancers]]

        if enhancers != parser.enhancers:
            parser.enhancers = enhancers

        current = ['%s %s'.strip() % (p[0], ' '.join(p[1])) 
                   for p in parser.sources]
        sources = _get('sources', '\n'.join(current))
        sources = [f for f in 
                    [s.strip() for s in sources.split('\n')]
                   if f != '']
        sources = [(u[0], tuple(u[1:])) for u in [f.split() for f in sources]]

        parser.sources = sources
        parser.write()
        redirect_to(action='index')

