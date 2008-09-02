from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1220257331.1973431
_template_filename='/Volumes/MacDev/svn.afpy.org/atomisator.afpy.org/packages/atomisator.backoffice/trunk/yap/templates/backoffice.mako'
_template_uri='/backoffice.mako'
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
        # SOURCE LINE 1
        context.write(u'\n<h1>Atomisator configuration</h1>\n\nXXX put here a form for configuration\n(atomisator .cfg file)\n\n<div>\n <a href="/">Back To Front</a>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


