from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 2
_modified_time = 1220793708.5395219
_template_filename='/home/gawel/wsgi.afpy.org/Yap/yap/templates/front.mako'
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
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<script type="text/javascript">\n\ncurrentArticle = 0;\nsize = 50;\n\nfunction nextArticle() {\n  if (currentArticle<size) { \n    currentArticle+=1;\n  }\n  showCurrent(); \n}\n\nfunction previousArticle() {\n  if (currentArticle>0) {\n    currentArticle-=1; \n  }\n  showCurrent();\n}\n\nfunction showCurrent() {\n  showArticle(currentArticle);\n}\n\nfunction showArticle(id) {\n  var current = $(\'#e\'+id);\n  if (!current.is(\':visible\')) {\n        $("div.feedBody").hide(\'slow\');\n  }\n  current.slideToggle(\'slow\');\n  /*$(document).scrollTo(\'#e\'+id+\'_sh\', {duration: 1000, margin:true});*/\n  currentArticle = id;\n}\n\n$(document).bind(\'keydown\', \'j\', nextArticle);\n$(document).bind(\'keydown\', \'k\', previousArticle);\n$(document).bind(\'keydown\', \'right\', nextArticle);\n$(document).bind(\'keydown\', \'left\', previousArticle);\n\n$(document).ready(function() {\n\n')
        # SOURCE LINE 43
        for id_, entry in enumerate(c.entries): 
            # SOURCE LINE 44
            __M_writer(u' $("#e')
            __M_writer(unicode(id_))
            __M_writer(u'").hide(); \n $("#e')
            # SOURCE LINE 45
            __M_writer(unicode(id_))
            __M_writer(u'_sh").click(function() {showArticle(')
            __M_writer(unicode(id_))
            __M_writer(u')});\n')
        # SOURCE LINE 47
        __M_writer(u'\nshowCurrent();\n \n });\n\n</script>\n\n<table id="entries">\n')
        # SOURCE LINE 55
        for id_, entry in enumerate(c.entries):
            # SOURCE LINE 56
            __M_writer(u'<tr class="feedEntry"> \n  <td class="feedTitle clickable" id="e')
            # SOURCE LINE 57
            __M_writer(unicode(id_))
            __M_writer(u'_sh"> \n    ')
            # SOURCE LINE 58
            __M_writer(unicode(entry['title']))
            __M_writer(u'  \n    <span class="extract">')
            # SOURCE LINE 59
            __M_writer(unicode(entry['extract']))
            __M_writer(u'</span> \n </td>\n <td class="feedDate">\n   ')
            # SOURCE LINE 62
            __M_writer(unicode(entry['pubDate']))
            __M_writer(u'\n </td>\n <td class="feedLink">\n    <a target="_blank" class="linker" \n    href="')
            # SOURCE LINE 66
            __M_writer(unicode(entry['link']))
            __M_writer(u'"><img class="noBorder" src="link.png" \n    alt="link"/>\n   </a>\n </td>\n</tr>\n<tr>\n <td class="feedBodyContainer" colspan="3">\n  <div id="e')
            # SOURCE LINE 73
            __M_writer(unicode(id_))
            __M_writer(u'" class="feedBody">\n    ')
            # SOURCE LINE 74
            __M_writer(unicode(entry['description']))
            __M_writer(u'\n  </div>\n </td>\n</tr>\n')
        # SOURCE LINE 79
        __M_writer(u'</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


