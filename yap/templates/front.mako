<%inherit file="/base.mako" />

<script type="text/javascript">
$(document).ready(function(){

%for id_, entry in enumerate(c.entries):  

 div_${id_} = "#${id_}";
 $(div_${id_}).hide();
 button_${id_} = "#${id_}_sh";
 
 $(button_${id_}).click(
    function() {
      $(div_${id_}).slideToggle('slow');
    }
  );

%endfor
 
 });

</script>

%for id_, entry in enumerate(c.entries): 
<div class="feedEntry">
 <div class="feedTitle clickable" id="${id_}_sh">
   ${entry['title']}  
   <a target="_blank" class="linker" href="${entry['link']}"><img class="noBorder" src="link.png"/></a>
 </div>
 
 <div class="feedBody" id="${id_}">
  <strong>Date: ${entry['pubDate']}</strong>
  ${entry['description']}
 </div>
</div>
%endfor


