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
        <link rel="alternate" type="application/rss+xml" title="RSS Feed" href="/atomisator.xml" />
    </head>
	<body>
     <a name="top"></a>
     <div id="header">
       <div id="rss"><a href="/atomisator.xml"><img src="/rss.png"/></a></div>
       <a class="noUnderline" href="#">
        <img class="noBorder" src="atomisator-logo.jpg" alt="Atomisator" title="Atomisator">
       </a>
      
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
    <div id="rss"><a href="/atomisator.xml"><img src="/rss.png"/></a></div>

        Atomisator | <a href="#top">Top</a> <!--| <a href="/backoffice">Backoffice</a>-->
     </div>
	</body>
</html>

