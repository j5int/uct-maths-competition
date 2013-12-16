// tables.js
// used in view and registration pages.
// does the edit button and delete confirmation.

//edit button: switch to iput mode
function show_input(id)
{
	$('#input'+id).show()	
	$('#show'+id).hide()
}

//confirmation dialog for when you click 'Delete All' in views
function drop(type)
{
	if (del){
		return confirm('Are you sure you want to permanently delete all of your registered '+type+'s?')
	}
	else {return true}
}

/*
//checks for empty responsible teacher form
function validate(){ 
//var mail = document.getElementById('rt_email'); 
//var sub = document.getElementById('submit');
//var m = document.getElementById('rmail');
//return false;
//var box = document.getElementById('confirm');

if(mail.value.length == 0){ 
//sub.disabled = true;
//sub.setAttribute("disabled", "disabled");
//m.setattribute("re")
return true; 
} 
else{ 
return true; 
} 
//document.getElementById("submits").disabled = true;
//$('#submits').prop('disabled', true);
}
*/
// todo: check first row of invigilator for empty forms
function disableElement(checkBox)
{
  var sbmt = document.getElementById("complete");
  
  if (checkBox.checked)
	{sbmt.disabled = false;}
  else
	{sbmt.disabled = true;}
}
