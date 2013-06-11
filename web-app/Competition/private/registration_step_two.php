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

if ($p_step_one == 'complete')										//They have not been logged in yet
{

?>

<h2 align="center"> Registration - Step 2 </h2>

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

}

do_html_footer();

?>
