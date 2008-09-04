from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1220523256.17191
_template_filename='/Volumes/MacDev/svn.afpy.org/atomisator.afpy.org/packages/Yap/trunk/yap/templates/front.mako'
_template_uri='/front.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 1
        context.write(u'\n\n<script type="text/javascript">\n$(document).ready(function(){\n\n')
        # SOURCE LINE 6
        for id_, entry in enumerate(c.entries):  
            # SOURCE LINE 7
            context.write(u'\n div_')
            # SOURCE LINE 8
            context.write(unicode(id_))
            context.write(u' = "#e')
            context.write(unicode(id_))
            context.write(u'";\n $(div_')
            # SOURCE LINE 9
            context.write(unicode(id_))
            context.write(u').hide();\n button_')
            # SOURCE LINE 10
            context.write(unicode(id_))
            context.write(u' = "#e')
            context.write(unicode(id_))
            context.write(u'_sh";\n \n $(button_')
            # SOURCE LINE 12
            context.write(unicode(id_))
            context.write(u').click(\n    function() {\n      var current = $(div_')
            # SOURCE LINE 14
            context.write(unicode(id_))
            context.write(u');\n      if (!current.is(\':visible\')) {\n        $("div.feedBody").hide(\'slow\');\n      }\n      current.slideToggle(\'slow\');\n    }\n  );\n\n')
        # SOURCE LINE 23
        context.write(u' \n });\n\n</script>\n\n')
        # SOURCE LINE 28
        for id_, entry in enumerate(c.entries): 
            # SOURCE LINE 29
            context.write(u'<div class="feedEntry">\n <div class="feedTitle clickable" id="e')
            # SOURCE LINE 30
            context.write(unicode(id_))
            context.write(u'_sh">\n   ')
            # SOURCE LINE 31
            context.write(unicode(entry['title']))
            context.write(u'  \n   <a target="_blank" class="linker" href="')
            # SOURCE LINE 32
            context.write(unicode(entry['link']))
            context.write(u'"><img class="noBorder" src="link.png" alt="link"/></a>\n   <span class="extract">')
            # SOURCE LINE 33
            context.write(unicode(entry['extract']))
            context.write(u'</span>\n </div>\n \n <div class="feedBody" id="e')
            # SOURCE LINE 36
            context.write(unicode(id_))
            context.write(u'">\n  <strong>Date: ')
            # SOURCE LINE 37
            context.write(unicode(entry['pubDate']))
            context.write(u'</strong>\n  ')
            # SOURCE LINE 38
            context.write(unicode(entry['description']))
            context.write(u'\n </div>\n</div>\n')
        # SOURCE LINE 42
        context.write(u'\n\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


