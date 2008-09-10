<%inherit file="/base.mako" />

<script type="text/javascript">

currentArticle = 0;
size = 50;

function nextArticle() {
  hideArticle(currentArticle);
  if (currentArticle<size) { 
    currentArticle+=1;
  }
  showArticle(currentArticle, false);
}

function previousArticle() {
  hideArticle(currentArticle);
  if (currentArticle>0) {
    currentArticle-=1;
  }
  showArticle(currentArticle, false);
}

function hideArticle(id) {
  $('#e'+id).hide();
  $('#e'+id+'_ex').show();
}

function showArticle(id, noscroll) {
  var current = $('#e'+id);
  current.slideToggle('slow');
  if (!noscroll) {
    $.scrollTo($('#e'+id+'_sh'), {duration: 750, easing: 'swing', 
                           margin: true, offset: -10});
  }
  $('#e'+id+'_ex').hide();

}

$(document).bind('keydown', 'j', nextArticle);
$(document).bind('keydown', 'k', previousArticle);
$(document).bind('keydown', 'right', nextArticle);
$(document).bind('keydown', 'left', previousArticle);

$(document).ready(function() {

%for id_, entry in enumerate(c.entries): 
 $("#e${id_}").hide(); 
 $("#e${id_}_sh").click(function() {hideArticle(currentArticle);showArticle(${id_}, false); currentArticle=${id_}});
%endfor

showArticle(currentArticle, true);
 
 });

</script>

<table id="entries">
%for id_, entry in enumerate(c.entries):
<tr class="feedEntry" id="e${id_}_fe"> 
  <td class="feedTitle clickable" id="e${id_}_sh"> 
    ${entry['title']}  
    <span class="extract" id="e${id_}_ex">${entry['extract']}</span> 
 </td>
 <td class="feedDate">
   ${entry['pubDate']}
 </td>
 <td class="feedLink">
    <a target="_blank" class="linker" 
    href="${entry['link']}"><img class="noBorder" src="link.png" 
    alt="link"/>
   </a>
 </td>
</tr>
<tr>
 <td class="feedBodyContainer" colspan="3">
  <div id="e${id_}" class="feedBody">
    ${entry['description']}
  </div>
 </td>
</tr>
%endfor
</table>

