from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1220245224.717283
_template_filename='/Volumes/MacDev/svn.afpy.org/atomisator.afpy.org/packages/atomisator.backoffice/trunk/yap/templates/serverinfo.mako'
_template_uri='/serverinfo.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        request = context.get('request', UNDEFINED)
        # SOURCE LINE 1
        context.write(u'<h2>\nServer info for ')
        # SOURCE LINE 2
        context.write(unicode(request.host))
        context.write(u'\n</h2>\n\n<p>\nThe URL you called: ')
        # SOURCE LINE 6
        context.write(unicode(h.url_for()))
        context.write(u'\n</p>\n\n<p>\nThe name you set: ')
        # SOURCE LINE 10
        context.write(unicode(c.name))
        context.write(u'\n</p>\n\n<p>The WSGI environ:<br />\n<pre>')
        # SOURCE LINE 14
        context.write(unicode(c.pretty_environ))
        context.write(u'</pre>\n</p>\n        \n')
        return ''
    finally:
        context.caller_stack.pop_frame()


