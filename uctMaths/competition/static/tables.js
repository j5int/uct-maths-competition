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

  //prevent submission of empty forms
  if (blankForm())
	{return false;}
/**********************
*** EMAIL VALIDATION***
***********************/

   /*---------------------------------------------
    Validate responsible teacher
    ----------------------------------------------*/
	var resp_firstname = document.getElementsByClassName('resp_firstname');			// 10 invigilator fields
	var resp_surname = document.getElementsByClassName('resp_surname');
	var resp_phone_primary = document.getElementsByClassName('resp_phone_primary');
	var resp_mail = document.getElementsByClassName('resp_mail');
	var resp_phone_alt = document.getElementsByClassName('resp_phone_alt');
	
	validity = validate_invigilator(resp_firstname[0].value, resp_surname[0].value, resp_phone_primary[0].value, resp_phone_alt[0].value, resp_mail[0].value);

    resp_firstname[0].style.background = 'White'; 
    resp_surname[0].style.background = 'White'; 
    resp_phone_primary[0].style.background = 'White'; 
    resp_phone_alt[0].style.background = 'White'; 
    resp_email[0].style.background = 'White'; 


	if (validity!=0) {
	    window.scrollTo(100,500);
	    switch(validity){
        case -1: alert("Responsible teacher field must be completed"); break;
        case 1:resp_firstname[0].style.background = 'Yellow'; break;
        case 2:resp_surname[0].style.background = 'Yellow'; break;
        case 3:resp_phone_primary[0].style.background = 'Yellow'; break;
        case 4:resp_phone_alt[0].style.background = 'Yellow'; break;
        case 5:resp_email[0].style.background = 'Yellow'; break;
	    }
	    return false; //Error
	}
  
    /*---------------------------------------------
    Validate invigilators
    ----------------------------------------------*/
	var invig_firstname = document.getElementsByClassName('invig_firstname');			// 10 invigilator fields
	var invig_surname = document.getElementsByClassName('invig_surname');
	var invig_phone_primary = document.getElementsByClassName('invig_phone_primary');
	var invig_mail = document.getElementsByClassName('invig_mail');
	var invig_phone_alt = document.getElementsByClassName('invig_phone_alt');
	
	var num_invigilators =0;
	
	for(var i = 0; i < 10; ++i)
	{
	validity = validate_invigilator(invig_firstname[i].value, invig_surname[i].value, invig_phone_primary[i].value, invig_phone_alt[i].value, invig_mail[i].value);
	
		invig_firstname[i].style.background = 'White'; 
		invig_surname[i].style.background = 'White'; 
		invig_phone_primary[i].style.background = 'White'; 
		invig_phone_alt[i].style.background = 'White';
		invig_mail[i].style.background = 'White'; 
	
	    if (validity > 0) //Any error condition
	    {
	    	window.scrollTo(100,500);
		    switch(validity){
		        case 1:invig_firstname[i].style.background = 'Yellow'; break;
		        case 2:invig_surname[i].style.background = 'Yellow'; break;
		        case 3:invig_phone_primary[i].style.background = 'Yellow'; break;
		        case 4:invig_phone_alt[i].style.background = 'Yellow'; break;
		        case 5:invig_mail[i].style.background = 'Yellow'; break;
		    }
			return false;
	    }
	    else if (validity==0) num_invigilators+=1; //else full and valid field
	}
	
    /*---------------------------------------------
    Validate students
    ----------------------------------------------*/
	var st_firstname = document.getElementsByClassName('st_firstname');
	var st_surname = document.getElementsByClassName('st_surname');
	var pairs = document.getElementsByClassName('pairs');

	var count = 0; 
	
	// count the number of students	
	for (var j=0; j<st_firstname.length; j++)
	{
	    student_valid = validate_student(st_firstname[j].value, st_surname[j].value);
        st_firstname[j].style.background = 'White';
	    st_surname[j].style.background = 'White';
	    
	    if (student_valid>0){ //error
	     switch(student_valid){
	        case 1: st_firstname[j].style.background = 'Yellow'; break;
	        case 2: st_surname[j].style.background = 'Yellow'; break;
	        }
	    return false;
	    }
	    if (student_valid == 0) {
	    st_firstname[j].style.background = 'White';
	    st_surname[j].style.background = 'White';
	    count += 1;
	    }
	}
	
	for (var k=0; k<pairs.length; k++)
	{ count += pairs[k].options[pairs[k].selectedIndex].value*2; }
	
	// prompt user to add invigilator
	if (count == 75 && num_invigilators < 2)
	{
	invig_firstname[1].style.background = 'Yellow';
    invig_surname[1].style.background = 'Yellow';
    invig_phone_primary[1].style.background = 'Yellow';
    invig_mail[1].style.background = 'Yellow'; 

	window.scrollTo(100,500);
    alert("Reminder: A minimum of two invigilators are required for 75 students.");
    return false;
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

function validate_student(firstname, surname){
	//alert("Validate student!");

    if (firstname.length > 254){
            alert("Firstname is too long");
            return 1;
        }
        if (surname.length > 254){
            alert("Surname is too long");
            return 2;
        }

    if(firstname=="" && surname==""){
        return -1; //Empty field
        }
    else if(firstname=="" && surname!=""){
        alert("A student requires a firstname");
        window.scrollTo(200,700);
        return 1; //error in firstname
        }
    else if(firstname!="" && surname==""){
        alert("A student requires a surname");
        window.scrollTo(200,700);
        return 2; //error in surname
        }
    else {
        return 0;//Valid entry
        }
}

function validate_invigilator(firstname, surname, phone_primary, phone_alt, email){
    //alert("Invigilator:"+firstname+", "+surname+"; "+phone_primary+"; " + email);
    
    if (firstname.length > 254)
        {
            alert("Firstname is too long");
            return 1;
        }
        if (surname.length > 254)
        {
            alert("Surname is too long");
            return 2;
        }

    //Validate that all comopulsory fields have been set out
    if(firstname=="" && surname == "" && email == "" && phone_primary == ""){
        //alert("Valid empty line");
        return -1; //Valid
    }
    else if(firstname!="" && surname != "" && email != "" && phone_primary != ""){
        
        //alert("Valid full line");
        //return 1; //Valid - continue to other criteria
        }
    else {
        alert("Invalid entry. Field missing");
        if (firstname=="") return 1;
        else if (surname=="") return 2;
        else if (phone_primary=="") return 3;
        //else if (phone_alt=="") return 4;
        else if (email=="") return 5;
        }
        
    //Validate telephone number
    //Firstly, check length; Secondly check only numerical characters;

    
        if (validate_phonenumber(phone_primary)!=0)
            return 3;

        //If the user has attempted to input alternative phone number
        if (phone_alt!="" && validate_phonenumber(phone_alt)!=0)
            return 4;

        if (email.length > 49)
        {
            alert("Invalid email address. Address too long");
            return 5;
        }

//        //Check validity of email
		var atpos=email.indexOf('@');		// position of '@' symbol
		var dotpos=email.lastIndexOf('.');	//position of last period('.')

      if (atpos<1 || dotpos<atpos+2 || dotpos+2>=email.length)
          {
            alert("Invalid mail input");
            return 5;
          }

        //alert("Done here");
        return 0;
}

function validate_phonenumber(phone_number){

        if (phone_number.length!=10){
            alert("Invalid phone number length.");
            return 3; //invalid -- incorrect length for phone number
        }
       // else alert("Valid phone number length " + phone_number);
        
        //Check for invalid characters in primary phone number
        for (c=0; c < 10; ++c)
        {
         if (isNaN(parseInt(phone_number.substr(c,1)), 10))
         { 
            alert("Invalid character in phone number");
            return 3;//Invalid
          }
        }
      //  alert("Valid phone number");
        return 0; //Valid
}


