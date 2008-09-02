import logging

from yap.lib.base import *

log = logging.getLogger(__name__)

class BackofficeController(BaseController):

    def index(self):
        c.title = 'Backoffice'
        return render('/backoffice.mako')

