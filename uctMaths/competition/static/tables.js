// tables.js
// used in view and registration pages.
// does the edit button and delete confirmation.

//edit button: switch to input mode
function show_input(id)
{
	$('#input'+id).show()	
	$('#show'+id).hide()
}

//confirmation dialogue for when you click 'Delete All' in views
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

//used in newstudents
//enables the submit button for the form
function disableElement(checkBox)
{
  var sbmt = document.getElementById("complete");
  
  if (checkBox.checked)
	{sbmt.disabled = false;}
  else
	{sbmt.disabled = true;}
}

/*
//to be extended to double check empty fields
function validateForm()
{
var f=document.forms["registration"]["inv_firstname"][0].value;
if (f==null || f=="")
  {
  alert("Please fill out the required fields for an invigilator");
  return false;
  }
 else
 {return true;}
}
*/

function validateForm(doc)
{
  var mail = document.getElementsByClassName('mail');   // array of email fields
  
  // for each email field
  for (var i=0; i < mail.length; i++)
  {	var x=mail[i].value;
  
    if (x == '')
    {  break;  }
    else
    {
		var atpos=x.indexOf('@');
		var dotpos=x.lastIndexOf('.');
      if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length)
      {  alert("The following email address is not valid: '"+x+"'");
          return false;
      }
    }
  }
  
   return true;
}