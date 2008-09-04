<%inherit file="/base.mako" />

<script type="text/javascript">
$(document).ready(function(){

%for id_, entry in enumerate(c.entries):  

 div_${id_} = "#e${id_}";
 $(div_${id_}).hide();
 button_${id_} = "#e${id_}_sh";
 
 $(button_${id_}).click(
    function() {
      var current = $(div_${id_});
      if (!current.is(':visible')) {
        $("div.feedBody").hide('slow');
      }
      current.slideToggle('slow');
    }
  );

%endfor
 
 });

</script>

%for id_, entry in enumerate(c.entries): 
<div class="feedEntry">
 <div class="feedDate">${entry['pubDate']}</div>
 <div class="feedTitle clickable" id="e${id_}_sh">
   ${entry['title']}  
   <a target="_blank" class="linker" href="${entry['link']}"><img class="noBorder" src="link.png" alt="link"/></a>
   <span class="extract">${entry['extract']}</span> </div>
 <div style="clear: top"/> 
 <div class="feedBody" id="e${id_}">
    ${entry['description']}
 </div>
</div>
%endfor


