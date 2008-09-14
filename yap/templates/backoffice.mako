<%inherit file="/base.mako" />
${h.form(h.url(action='update'), method='get')}
<table>
  <tr>
    <td>Title</td>
    <td>${h.text_field('title', value=c.atomisator['title'])}</td>
  </tr>
  <tr>
    <td>Sources</td>
    <td>${h.text_area('sources', c.atomisator['sources'], size="100x18")}</td>
  </tr>
  <tr>
    <td>Database</td>
    <td>${h.text_field('database', value=c.atomisator['database'], 
                       size=50)}</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>${h.text_field('description', value=c.atomisator['description'], size=50)}</td>
  </tr>
  <tr>
    <td>Link</td>
    <td>${h.text_field('link', value=c.atomisator['link'], size=50)}</td>
  </tr>
  <tr>
    <td>Filters</td>
    <td>${h.text_area('filters', c.atomisator['filters'], size="50x10")}</td>
  </tr>
  <tr>
    <td>Enhancers</td>
    <td>${h.text_area('enhancers', c.atomisator['enhancers'], size="50x10")}</td>
  </tr>
  <tr>
   <td colspan="2">${h.submit('Submit')}</td>
  </tr>
</table>

${h.end_form()}
 
<div>
 <a href="/">Back To Front</a>
</div>
