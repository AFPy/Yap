from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 2
_modified_time = 1220793708.6175411
_template_filename=u'/home/gawel/wsgi.afpy.org/Yap/yap/templates/base.mako'
_template_uri=u'/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en" dir="ltr">\n\t<head>\n')
        # SOURCE LINE 5
        if c.title:
            # SOURCE LINE 6
            __M_writer(u'\t\t<title>')
            __M_writer(unicode(c.title))
            __M_writer(u'</title>\n')
        # SOURCE LINE 8
        __M_writer(u'        <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>\n\t\t')
        # SOURCE LINE 9
        __M_writer(unicode(h.rails.stylesheet_link_tag('/main.css')))
        __M_writer(u'\n        ')
        # SOURCE LINE 10
        __M_writer(unicode(h.rails.javascript_include_tag('/jquery.js')))
        __M_writer(u'\n        ')
        # SOURCE LINE 11
        __M_writer(unicode(h.rails.javascript_include_tag('/jquery.hotkeys.js')))
        __M_writer(u'\n        ')
        # SOURCE LINE 12
        __M_writer(unicode(h.rails.javascript_include_tag('/jquery.scrollTo.js')))
        __M_writer(u'\n        ')
        # SOURCE LINE 13
        __M_writer(unicode(h.rails.javascript_include_tag('/jquery.localscroll.js')))
        __M_writer(u'\n        \n        <link rel="alternate" type="application/rss+xml" title="RSS Feed" href="')
        # SOURCE LINE 15
        __M_writer(unicode(h.url_for('/atomisator.xml')))
        __M_writer(u'" />\n    </head>\n\t<body>\n     <a name="top"></a>\n     <div id="header">\n       <div id="rss"><a href="')
        # SOURCE LINE 20
        __M_writer(unicode(h.url_for('/atomisator.xml')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(h.url_for('/rss.png')))
        __M_writer(u'" alt="rss"/></a></div>\n')
        # SOURCE LINE 21
        if c.title:
            # SOURCE LINE 22
            __M_writer(u'      <div id="title">\n        ')
            # SOURCE LINE 23
            __M_writer(unicode(c.title))
            __M_writer(u'\n      </div>\n')
        # SOURCE LINE 26
        __M_writer(u'     </div>\n     <div id="content">\n        ')
        # SOURCE LINE 28
        __M_writer(unicode(self.body()))
        __M_writer(u'\n     </div>\n     <div id="footer">\n        <div id="rss"><a href="')
        # SOURCE LINE 31
        __M_writer(unicode(h.url_for('/atomisator.xml')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(h.url_for('/rss.png')))
        __M_writer(u'" alt="rss"/></a></div>\n        <a href="http://atomisator.ziade.org">Powered by Atomisator</a> | <a href="#top">Top</a> <!--| <a href="/backoffice">Backoffice</a>-->\n     </div>\n\t</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


