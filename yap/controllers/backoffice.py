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

    def index(self):
        c.title = 'Backoffice'
        parser = AtomisatorConfig(CONFIG)
        c.atomisator = {}
        c.atomisator['title'] = parser.title
        s = [s[0] + ' ' + ' '.join(s[1]) for s in parser.sources]

        c.atomisator['sources'] = '\n'.join(s)
        c.atomisator['database'] = parser.database
        c.atomisator['description'] = parser.description
        c.atomisator['link'] = parser.link
        
        s = [s[0] + ' ' + ' '.join(s[1]) for s in parser.filters]
        c.atomisator['filters'] = '\n'.join(s)    
 
        s = [s[0] + ' ' + ' '.join(s[1]) for s in parser.enhancers]
        c.atomisator['enhancers'] = '\n'.join(s)    
 
        return render('/backoffice.mako')

    
    def update(self):
        parser = AtomisatorConfig(CONFIG)
       
        # TODO make atomisator cfg file read/writeable by text
        # to avoid all this crappy parsing
        if request.GET.get('title', parser.title) != parser.title:
            parser.title = request.GET.get('title')
        
        if request.GET.get('link', parser.link) != parser.link:
            parser.link = request.GET.get('link')
        
        if request.GET.get('database', parser.database) != parser.database:
            parser.database = request.GET.get('database')

        current = ['%s %s'.strip() % (p[0], ' '.join(p[1])) 
                   for p in parser.filters]
        
        filters = request.GET.get('filters', '\n'.join(current))
        filters = [f for f in [s.strip() for s in filters.split('\n')]
                   if f != '']
        filters = [(u[0], tuple(u[1:])) for u in [f.split() for f in filters]]

        if filters != parser.filters:
            parser.filters = filters

        current = ['%s %s'.strip() % (p[0], ' '.join(p[1])) 
                   for p in parser.enhancers]
        
        enhancers = request.GET.get('enhancers', '\n'.join(current))
        enhancers = [f for f in [s.strip() for s in enhancers.split('\n')]
                   if f != '']
        enhancers = [(u[0], tuple(u[1:])) for u in [f.split() for f in enhancers]]

        if enhancers != parser.enhancers:
            parser.enhancers = enhancers

        current = ['%s %s'.strip() % (p[0], ' '.join(p[1])) 
                   for p in parser.sources]
        sources = request.GET.get('sources', '\n'.join(current))
        sources = [f for f in [s.strip() for s in sources.split('\n')]
                   if f != '']
        sources = [(u[0], tuple(u[1:])) for u in [f.split() for f in sources]]

        if sources != parser.sources:
            parser.sources = sources


        parser.write()
        redirect_to(action='index')

