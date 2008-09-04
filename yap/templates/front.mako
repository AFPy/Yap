<%inherit file="/base.mako" />

<script type="text/javascript">

currentArticle = 0;
size = 50;

function nextArticle() {
  if (currentArticle<size) { 
    currentArticle+=1;
  }
  showCurrent(); 
}

function previousArticle() {
  if (currentArticle>0) {
    currentArticle-=1; 
  }
  showCurrent();
}

function showCurrent() {
  showArticle(currentArticle);
}

function showArticle(id) {
  var current = $('#e'+id);
  if (!current.is(':visible')) {
        $("div.feedBody").hide('slow');
  }
  current.slideToggle('slow');
  /*$(document).scrollTo('#e'+id+'_sh', {duration: 1000, margin:true});*/
  currentArticle = id;
}

$(document).bind('keydown', 'j', nextArticle);
$(document).bind('keydown', 'k', previousArticle);
$(document).bind('keydown', 'right', nextArticle);
$(document).bind('keydown', 'left', previousArticle);

$(document).ready(function() {

%for id_, entry in enumerate(c.entries): 
 $("#e${id_}").hide(); 
 $("#e${id_}_sh").click(function() {showArticle(${id_})});
%endfor

showCurrent();
 
 });

</script>

<table id="entries">
%for id_, entry in enumerate(c.entries):
<tr class="feedEntry"> 
  <td class="feedTitle clickable" id="e${id_}_sh"> 
    ${entry['title']}  
    <span class="extract">${entry['extract']}</span> 
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

