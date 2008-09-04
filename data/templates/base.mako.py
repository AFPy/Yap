from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1220523256.198565
_template_filename=u'/Volumes/MacDev/svn.afpy.org/atomisator.afpy.org/packages/Yap/trunk/yap/templates/base.mako'
_template_uri=u'/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        self = context.get('self', UNDEFINED)
        # SOURCE LINE 2
        context.write(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en" dir="ltr">\n\t<head>\n')
        # SOURCE LINE 5
        if c.title:
            # SOURCE LINE 6
            context.write(u'\t\t<title>')
            context.write(unicode(c.title))
            context.write(u'</title>\n')
        # SOURCE LINE 8
        context.write(u'        <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>\n\t\t')
        # SOURCE LINE 9
        context.write(unicode(h.rails.stylesheet_link_tag('/main.css')))
        context.write(u'\n        ')
        # SOURCE LINE 10
        context.write(unicode(h.rails.javascript_include_tag('/jquery.js')))
        context.write(u'\n        <link rel="alternate" type="application/rss+xml" title="RSS Feed" href="/atomisator.xml" />\n    </head>\n\t<body>\n     <a name="top"></a>\n     <div id="header">\n       <div id="rss"><a href="/atomisator.xml"><img src="/rss.png" alt="rss"/></a></div>\n')
        # SOURCE LINE 17
        if c.title:
            # SOURCE LINE 18
            context.write(u'      <div id="title">\n        ')
            # SOURCE LINE 19
            context.write(unicode(c.title))
            context.write(u'\n      </div>\n')
        # SOURCE LINE 22
        context.write(u'     </div>\n     <div id="content">\n        ')
        # SOURCE LINE 24
        context.write(unicode(self.body()))
        context.write(u'\n     </div>\n     <div id="footer">\n    <div id="rss"><a href="/atomisator.xml"><img src="/rss.png" alt="rss"/></a></div>\n\n        <a href="http://atomisator.ziade.org">Powered by Atomisator</a> | <a href="#top">Top</a> <!--| <a href="/backoffice">Backoffice</a>-->\n     </div>\n\t</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


