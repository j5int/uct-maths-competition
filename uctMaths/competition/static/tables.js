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

//function checked()
//{
//	if ()
//	{
		//button = enabled
//	}
//	else
//	{
		//button = disabled
//	}
//}


//checks for empty responsible teacher form
function validate(){ 
//var mail = document.getElementById('rt_email'); 
//var sub = document.getElementById('submit');
//var m = document.getElementById('rmail');
return false;
/*
if(mail.value.length == 0){ 
//sub.disabled = true;
//sub.setAttribute("disabled", "disabled");
//m.setattribute("re")
return false; 
} 
else{ 
return true; 
} */
//document.getElementById("submits").disabled = true;
//$('#submits').prop('disabled', true);
}