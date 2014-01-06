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
/**********************
*** EMAIL VALIDATION***
***********************/
  var mail = document.getElementsByClassName('mail');   // array of email fields
  var error= false;
  
  // highlight invalid email fields
  for (var i=0; i < mail.length; i++)
  {	var x=mail[i].value;	//email value
	
	//skip empty fields and validate others
    if (x == '')
    {  break;  }
    else
    {
		var atpos=x.indexOf('@');	// position of '@' symbol
		var dotpos=x.lastIndexOf('.');	//position of last period('.')
      if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length)
      {//  alert("The following email address is not valid: '"+x+"'");	// notify user of invalid 
		mail[i].style.background ='Yellow';	error =true;
      //    return false;
      }
	  else
	  {
		mail[i].style.background = 'White';
	  }
    }
  }
  
  if (error)
  {
	alert("One or more email addresses seem to be invalid. Please verify your input.");
	return false;
  }
 /************************************
 *** NO# of INVIGILATORS VALIDATION **
 *************************************/ 
//	var students = document.getElementByClassName('pupil');
	var individuals = document.getElementsByClassName('single');	//# of individuals
	var pairs = document.getElementsByClassName('double');			//# of paired students
	var count =0;													// number of students
	var invig = document.getElementsByClassName('invig');			// 10 invigilator fields
	var numOfInvig =0;
	
//  count the number of students	
	for (var j=0; j<individuals.length; j++)
	{
		if (individuals[j].value != '')
		{ count++;}
	}
	
	for (var k=0; k<pairs.length; k++)
	{ count += pairs[k].options[pairs[k].selectedIndex].value*2; }
	
	// prompt user to add invigilator
	if (count ==75)
	{
		//check for 2nd invigilator
		if(invig[1].value =='')
		{
			invig[1].style.background = 'Yellow';
			alert("Reminder: to enter 75 students for this competition, 2 or more invigilators are required!");
			return false;
		}
		invig[1].style.background = 'White';
	}
//	alert(numOfInvig);
	
 
 //	else if()
   return true;
}