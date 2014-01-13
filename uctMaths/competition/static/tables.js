/**********************************************
***				 table.js					***
*** 	  used in newstudents.html		    ***
*** does client-side validation of the form ***
**********************************************/
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

/****************************************
*** ENABLE/DISABLE FORM SUBMIT BUTTON ***
*****************************************/
function disableElement(checkBox)
{
  var sbmt = document.getElementById("complete");				//submit button iD
  
  if (checkBox.checked)
	{sbmt.disabled = false;}		//enable
  else
	{sbmt.disabled = true;}			//disable
}

// [FIX NEEDED] allows second invigilator to not have an email address
function validateForm(doc)
{
  var individuals = document.getElementsByClassName('single');	//# of individual student first names
  var pairs = document.getElementsByClassName('double');		//# of paired students

  //prevent submission of empty forms
  if (blankForm())
	{return false;}
/**********************
*** EMAIL VALIDATION***
***********************/
  var mail = document.getElementsByClassName('mail');   // array of email fields
  var error= false;
  
  // highlight invalid email fields
  for (var i=0; i < mail.length; i++)
  {	var x=mail[i].value;				//email value
	
	//skip empty fields and validate others
    if (x == '')
    {  break;  }
    else
    {
		var atpos=x.indexOf('@');		// position of '@' symbol
		var dotpos=x.lastIndexOf('.');	//position of last period('.')
      if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length)
      {
		mail[i].style.background ='Yellow';	error =true;
      }
	  else
	  {
		mail[i].style.background = 'White';
	  }
    }
  }
  
  if (error)
  {
	window.scrollTo(100,400);
	alert("One or more email addresses seem to be invalid. Please verify your input.");
	return false;
  }
  
 /************************************
 *** NO# of INVIGILATORS VALIDATION **
 *************************************/ 
	var count =0;													// number of students
	var invig_firstname = document.getElementsByClassName('invig_firstname');			// 10 invigilator fields
	var invig_surname = document.getElementsByClassName('invig_surname');
	var invig_phone_primary = document.getElementsByClassName('invig_phone_primary');
	var invig_mail = document.getElementsByClassName('mail');
	
	var numOfInvig =0;
	
	for(var i = 0; i < 10; ++i)
	{
	    validity = validate_invigilator(invig_firstname[i].value, invig_surname[i].value, invig_phone_primary[i].value, invig_mail[i+1].value);
	    if (validity == 0)
	    {
	        invig_firstname[i].style.background = 'Yellow';
	    	window.scrollTo(100,500);
			alert("Invalid entry");
			return false;
	    }
	}
	// count the number of students	
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
			window.scrollTo(100,500);
			alert("Reminder: A minimum of two invigilators are required for 75 students!");
			return false;
		}
		invig[1].style.background = 'White';
	}
/*********************
*** ALL TESTS PAST ***
*********************/	
   return true;
}

function blankForm()
{
/********************************************************
*** 1. SAFARI BROWSER FIX: PREVENTS EMPTY SUBMISSIONS ***
*** 2. WARN USER WHEN NO STUDENTS ARE REGISTERED      ***
*********************************************************/
	// all the inputs within form
    var inputs = document.getElementsByTagName('input');
	var blank = false;
    for (var i = 0; i < inputs.length; i++) {
        // only validate the inputs that have the required attribute
        if(inputs[i].hasAttribute("required")){
            if(inputs[i].value == ""){
                // found an empty field that is required
				inputs[i].style.background = 'Yellow';
				window.scrollTo(100,400);
				blank = true;
            }
			else {
			//found a highlighted field that is no longer empty
			inputs[i].style.background = 'White';
			}
        }
    }
	if (blank){
		alert("Please fill all required fields");
		return true;			// empty required fields found
	}
	else if(!blank)				// all required fields filled
		return false;
}

function validate_invigilator(firstname, surname, phone_primary, email){
    //alert("Invigilator:"+firstname+", "+surname+"; "+phone_primary+"; " + email);
    
    //Validate that all comopulsory fields have been set out
    if(firstname=="" && surname == "" && email == "" && phone_primary == ""){
        //alert("Valid empty line");
        return 1; //Valid
    }
    else if(firstname!="" && surname != "" && email != "" && phone_primary != ""){
        //alert("Valid full line");
        return 1; //Valid
        }
    else {
        //alert("Invalid line");
        return 0; //Invalid
        }
}


