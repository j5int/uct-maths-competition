// sidbar.js
// used for hiding the sidebar

var hid=false;
$(document).ready(function(){
    $('#hideshow').click(function(event) {    
        $('#sidebar').toggle('show');
        if (hid)	{
        	// alert("showing");
        	$('#hideshow').attr('src','/static/hidebutton.png'); 
        	$('#hideshow').attr('alt','Hide'); 
        	$('#hideshow').attr('title','Hide Sidebar'); 
        	hid=false;
        }
        else {
        	// alert("hiding");
        	$('#hideshow').attr('src','/static/showbutton.png');
        	$('#hideshow').attr('alt','Show'); 
        	$('#hideshow').attr('title','Show Sidebar');
        	hid=true;
        }
    });
});