# -*- coding: utf-8 -*-
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en" dir="ltr">
	<head>
        %if c.title:
		<title>${c.title}</title>
        %endif
        <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
		${h.rails.stylesheet_link_tag('/main.css')}
        ${h.rails.javascript_include_tag('/jquery.js')}
        ${h.rails.javascript_include_tag('/jquery.hotkeys.js')}
        ${h.rails.javascript_include_tag('/jquery.scrollTo.js')}
        ${h.rails.javascript_include_tag('/jquery.localscroll.js')}
        
        <link rel="alternate" type="application/rss+xml" title="RSS Feed" href="${h.url_for('/rss.xml')}" />
    </head>
	<body>
     <a name="top"></a>
     <div id="header">
       <div id="rss"><a href="${h.url_for('/rss.xml')}"><img src="${h.url_for('/rss.png')}" alt="rss"/></a></div>
      %if c.title:
      <div id="title">
        ${c.title}
      </div>
      %endif
     </div>
     <div id="content">
        ${self.body()}
     </div>
     <div id="footer">
        <div id="rss"><a href="${h.url_for('/rss.xml')}"><img src="${h.url_for('/rss.png')}" alt="rss"/></a></div>
        <a href="http://atomisator.ziade.org">Powered by Atomisator</a> | <a href="#top">Top</a> | <a href="/backoffice">Backoffice</a>
     </div>
	</body>
</html>

