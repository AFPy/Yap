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
        # need to make AtomisatorConfig writeable
        parser = AtomisatorConfig(CONFIG)
        if request.GET.get('title', parser.title) != parser.title:
            parser.title = request.GET.get('title')
        parser.write(open(CONFIG, 'w'))
        redirect_to(action='index')

