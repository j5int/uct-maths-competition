<?

require_once("math_fns.php");						// include function files for this application

session_start();
global $valid_user;
global $valid_user_id;
global $lang;										//language variable

import_request_variables("p","p_");

//-------------------------------------------------
//Languages
//-------------------------------------------------

	require("language/functions.eng");    			//load english

//-------------------------------------------------
//Logging in procedures
//-------------------------------------------------

require("display_fns.php");

{ 	
	if ($p_username && $p_password)						// they have entered a username and password
	{
		$result = login($p_username, $p_password);		//check whether valid user
	    if ($result) 									// if they are in the database register the user id
    	{
			$_SESSION['valid_user'] = $p_username;		//variable for username set
			$_SESSION['valid_user_id'] = $result;		//variable for user id set
//			set_user_types();							//set the types of user they are
	    } else
    	{ 												//wrong username or password
			competition_header();
			do_wrong_login_information();
			exit;
		}      
	}
}

//-------------------------------------------------

do_html_header(); 

check_valid_user();

if ($p_step_two == "complete")
{
if (($p_invigilator_1_name == 'Change Me') || ($p_rteacher_name == 'Change Me') || ($p_invigilator_1_name == ''))	
{

?>

<p align=center><b> Please note that you have not specified a responsible teacher or Invigilator 1. Please try again! </b></p>

<p>
Please note that filling in the details for the responsible teacher is compulsory. Furthermore, each school must send at least one invigilator. Therefore you need to at least fill in the details for Invigilator 1. 
</p>

	<form action="registration_step_three.php" name="formify" method=post>

	<h3 align="center"> Responsible Teacher - Compulsory</h3>

	<table align=center>   
		<tr>
			<td width="150">
				Name:
			</td>
			<td width="300">
				<input type="text" name="rteacher_name" size=40 maxlength=20 value="Change Me"/>
			</td>
		</tr>
		<tr>
			<td width="150">
				Telephone Number:
			</td>
			<td width="300">
				<input type="text" name="rteacher_telephone" size=10 maxlength=10 value="Change Me"/>
			</td>
		</tr>
		<tr>
			<td width="150">
				Fax Number:
			</td>
			<td width="300">
				<input type="text" name="rteacher_fax" size=10 maxlength=10 value=""/>
			</td>
		</tr>
		<tr>
			<td width="150">
				Email Address:
			</td>
			<td width="300">
				<input type="text" name="rteacher_email" size=40 maxlength=20 value=""/>
			</td>
		</tr>
	</table>

	<h3 align="center"> Invigilator 1 - Compulsory</h3>

	<table align=center>   
		<tr>
			<td width="150">
				Name:
			</td>
			<td width="150">
				<input type="text" name="invigilator_1_name" size=40 maxlength=20 value="Change Me"/>
			</td>
		</tr>
		<tr>
			<td width="150">
				Telephone Number:
			</td>
			<td width="300">
				<input type="text" name="invigilator_1_telephone" size=10 maxlength=10 value=""/>
			</td>
		</tr>
		<tr>
			<td width="150">
				Email Address:
			</td>
			<td width="300">
				<input type="text" name="invigilator_1_email" size=40 maxlength=20 value=""/>
			</td>
		</tr>
	</table>

	<h3 align="center"> Invigilator 2 - Optional</h3>

	<table align=center>   
		<tr>
			<td width="150">
				Name:
			</td>
			<td width="150">
				<input type="text" name="invigilator_2_name" size=40 maxlength=20 value=""/>
			</td>
		</tr>
		<tr>
			<td width="150">
				Telephone Number:
			</td>
			<td width="300">
				<input type="text" name="invigilator_2_telephone" size=10 maxlength=10 value=""/>
			</td>
		</tr>
		<tr>
			<td width="150">
				Email Address:
			</td>
			<td width="300">
				<input type="text" name="invigilator_2_email" size=40 maxlength=20 value=""/>
			</td>
		</tr>
	</table>

	<h3 align="center"> Invigilator 3 - Optional</h3>

	<table align=center>   
		<tr>
			<td width="150">
				Name:
			</td>
			<td width="150">
				<input type="text" name="invigilator_3_name" size=40 maxlength=20 value=""/>
			</td>
		</tr>
		<tr>
			<td width="150">
				Telephone Number:
			</td>
			<td width="300">
				<input type="text" name="invigilator_3_telephone" size=10 maxlength=10 value=""/>
			</td>
		</tr>
		<tr>
			<td width="150">
				Email Address:
			</td>
			<td width="300">
				<input type="text" name="invigilator_3_email" size=40 maxlength=20 value=""/>
			</td>
		</tr>
	</table>

	<h3 align="center"> Invigilator 4 - Optional</h3>

	<table align=center>   
		<tr>
			<td width="150">
				Name:
			</td>
			<td width="150">
				<input type="text" name="invigilator_4_name" size=40 maxlength=20 value=""/>
			</td>
		</tr>
		<tr>
			<td width="150">
				Telephone Number:
			</td>
			<td width="300">
				<input type="text" name="invigilator_4_telephone" size=10 maxlength=10 value=""/>
			</td>
		</tr>
		<tr>
			<td width="150">
				Email Address:
			</td>
			<td width="300">
				<input type="text" name="invigilator_4_email" size=40 maxlength=20 value=""/>
			</td>
		</tr>
	</table>

	<h3 align="center"> Invigilator 5 - Optional</h3>

	<table align=center>   
		<tr>
			<td width="150">
				Name:
			</td>
			<td width="150">
				<input type="text" name="invigilator_5_name" size=40 maxlength=20 value=""/>
			</td>
		</tr>
		<tr>
			<td width="150">
				Telephone Number:
			</td>
			<td width="300">
				<input type="text" name="invigilator_5_telephone" size=10 maxlength=10 value=""/>
			</td>
		</tr>
		<tr>
			<td width="150">
				Email Address:
			</td>
			<td width="300">
				<input type="text" name="invigilator_5_email" size=40 maxlength=20 value=""/>
			</td>
		</tr>
	</table>

	<input type="hidden" name="web_language" value=<? ts_language(); ?>>
	<input type="hidden" name="step_two" value="complete">

	<br>
	
	<table align=center>
		<tr>
			<td colspan=2 align=center>
				<input type=submit value=Submit>
			</td>
		</tr>
	</table>
	
	</form>

<?

} else

{

?>

<h2 align="center"> Registration - Step 3 </h2>

	<form action="registration_step_four.php" name="formify" method=post>

	<h3 align="center"> Individuals </h3>

	<table border=1 align=center>   
		<tr>
			<td width="60" align=center>
				Grade
			</td>
			<td width="60" align=center>
				Number
			</td>
			<td width="250">
				Surname
			</td>
			<td width="250">
				First Name
			</td>
			<td width="150" align = center>
				Gender
			</td>
			<td width="150" align = center>
				Language
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 8 </td>
			<td width="60" align=center> 1 </td>
			<td width="250"> <input type="text" name="ind_8_1_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_8_1_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_8_1_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_8_1_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 8 </td>
			<td width="60" align=center> 2 </td>
			<td width="250"> <input type="text" name="ind_8_2_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_8_2_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_8_2_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_8_2_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 8 </td>
			<td width="60" align=center> 3 </td>
			<td width="250"> <input type="text" name="ind_8_3_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_8_3_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_8_3_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_8_3_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 8 </td>
			<td width="60" align=center> 4 </td>
			<td width="250"> <input type="text" name="ind_8_4_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_8_4_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_8_4_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_8_4_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 8 </td>
			<td width="60" align=center> 5 </td>
			<td width="250"> <input type="text" name="ind_8_5_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_8_5_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_8_5_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_8_5_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 9 </td>
			<td width="60" align=center> 1 </td>
			<td width="250"> <input type="text" name="ind_9_1_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_9_1_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_9_1_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_9_1_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 9 </td>
			<td width="60" align=center> 2 </td>
			<td width="250"> <input type="text" name="ind_9_2_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_9_2_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_9_2_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_9_2_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 9 </td>
			<td width="60" align=center> 3 </td>
			<td width="250"> <input type="text" name="ind_9_3_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_9_3_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_9_3_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_9_3_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 9 </td>
			<td width="60" align=center> 4 </td>
			<td width="250"> <input type="text" name="ind_9_4_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_9_4_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_9_4_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_9_4_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 9 </td>
			<td width="60" align=center> 5 </td>
			<td width="250"> <input type="text" name="ind_9_5_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_9_5_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_9_5_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_9_5_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 10 </td>
			<td width="60" align=center> 1 </td>
			<td width="250"> <input type="text" name="ind_10_1_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_10_1_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_10_1_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_10_1_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 10 </td>
			<td width="60" align=center> 2 </td>
			<td width="250"> <input type="text" name="ind_10_2_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_10_2_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_10_2_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_10_2_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 10 </td>
			<td width="60" align=center> 3 </td>
			<td width="250"> <input type="text" name="ind_10_3_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_10_3_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_10_3_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_10_3_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 10 </td>
			<td width="60" align=center> 4 </td>
			<td width="250"> <input type="text" name="ind_10_4_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_10_4_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_10_4_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_10_4_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 10 </td>
			<td width="60" align=center> 5 </td>
			<td width="250"> <input type="text" name="ind_10_5_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_10_5_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_10_5_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_10_5_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 11 </td>
			<td width="60" align=center> 1 </td>
			<td width="250"> <input type="text" name="ind_11_1_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_11_1_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_11_1_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_11_1_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 11 </td>
			<td width="60" align=center> 2 </td>
			<td width="250"> <input type="text" name="ind_11_2_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_11_2_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_11_2_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_11_2_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 11 </td>
			<td width="60" align=center> 3 </td>
			<td width="250"> <input type="text" name="ind_11_3_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_11_3_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_11_3_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_11_3_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 11 </td>
			<td width="60" align=center> 4 </td>
			<td width="250"> <input type="text" name="ind_11_4_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_11_4_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_11_4_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_11_4_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 11 </td>
			<td width="60" align=center> 5 </td>
			<td width="250"> <input type="text" name="ind_11_5_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_11_5_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_11_5_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_11_5_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 12 </td>
			<td width="60" align=center> 1 </td>
			<td width="250"> <input type="text" name="ind_12_1_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_12_1_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_12_1_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_12_1_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 12 </td>
			<td width="60" align=center> 2 </td>
			<td width="250"> <input type="text" name="ind_12_2_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_12_2_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_12_2_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_12_2_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 12 </td>
			<td width="60" align=center> 3 </td>
			<td width="250"> <input type="text" name="ind_12_3_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_12_3_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_12_3_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_12_3_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 12 </td>
			<td width="60" align=center> 4 </td>
			<td width="250"> <input type="text" name="ind_12_4_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_12_4_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_12_4_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_12_4_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="60" align=center> 12 </td>
			<td width="60" align=center> 5 </td>
			<td width="250"> <input type="text" name="ind_12_5_surname" size=30 maxlength=30 value=""/> </td>
			<td width="250"> <input type="text" name="ind_12_5_firstname" size=30 maxlength=30 value=""/> </td>
			<td width="150" align=center>
				<select name="ind_12_5_gender" size=2>
					<option value="m"> Male </option>
					<option value="f"> Female </option>
				<select/>
			</td>
			<td width="150" align=center>
				<select name="ind_12_5_language" size=2>
					<option value="e"> English </option>
					<option value="a"> Afrikaans </option>
				<select/>
			</td>
		</tr>
	</table>

	<h3 align="center"> Pairs </h3>

	<table border=1 align=center>   
		<tr>
			<td width="150" align=center>
				Grade
			</td>
			<td width="60" align=center>
				8
			</td>
			<td width="60" align=center>
				9
			</td>
			<td width="60" align=center>
				10
			</td>
			<td width="60" align=center>
				11
			</td>
			<td width="60" align=center>
				12
			</td>
		</tr>
		<tr>
			<td width="150" align=center>
				Number of Pairs
			</td>
			<td width="60" align=center>
				<select name="pair_grade_8" size=6>
					<option value="0"> 0 </option>
					<option value="1"> 1 </option>
					<option value="2"> 2 </option>
					<option value="3"> 3 </option>
					<option value="4"> 4 </option>
					<option value="5"> 5 </option>
				<select/>
			</td>
			<td width="60" align=center>
				<select name="pair_grade_9" size=6>
					<option value="0"> 0 </option>
					<option value="1"> 1 </option>
					<option value="2"> 2 </option>
					<option value="3"> 3 </option>
					<option value="4"> 4 </option>
					<option value="5"> 5 </option>
				<select/>
			</td>
			<td width="60" align=center>
				<select name="pair_grade_10" size=6>
					<option value="0"> 0 </option>
					<option value="1"> 1 </option>
					<option value="2"> 2 </option>
					<option value="3"> 3 </option>
					<option value="4"> 4 </option>
					<option value="5"> 5 </option>
				<select/>
			</td>
			<td width="60" align=center>
				<select name="pair_grade_11" size=6>
					<option value="0"> 0 </option>
					<option value="1"> 1 </option>
					<option value="2"> 2 </option>
					<option value="3"> 3 </option>
					<option value="4"> 4 </option>
					<option value="5"> 5 </option>
				<select/>
			</td>
			<td width="60" align=center>
				<select name="pair_grade_12" size=6>
					<option value="0"> 0 </option>
					<option value="1"> 1 </option>
					<option value="2"> 2 </option>
					<option value="3"> 3 </option>
					<option value="4"> 4 </option>
					<option value="5"> 5 </option>
				<select/>
			</td>
		</tr>
	</table>

	<input type="hidden" name="web_language" value=<? ts_language(); ?>>

	<br>
	
	<table align=center>
		<tr>
			<td colspan=2 align=center>
				<input type=submit value=Submit>
			</td>
		</tr>
	</table>
	
	</form>
	
<?

}
}

do_html_footer();

?>
