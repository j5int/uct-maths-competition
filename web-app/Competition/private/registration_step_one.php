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

//if (!$p_logged_in)										//They have not been logged in yet
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

	$uid = $_SESSION['valid_user_id'];
	
	if (!($conn = db_connect()))
		return false;

	$query = "select * from uctmathcomp_school_users where comp_uid = '$uid'";
	$result = mysql_query($query);
	if (!$result)
		return false;
	$row = mysql_fetch_row($result);

?>

<h2 align="center"> Registration - Step 1 </h2>

<p>
Please verify your school's details. If all the details are correct you should click the "Proceed Directly to Step 2" button. If some of the details need to change, please change it and then click "Update Details". Your details will then be updated and you will thereafter be able to proceed to Step 2.
</p>

	<form action="change_details.php" name="formify" method=post>

	<table align=center>   
		<tr>
			<td width="150">
				Name of School:
			</td>
			<td width="300">
				<input type="text" name="fname" size=40 maxlength=20 value="<? echo $row[6]; ?>"/>
			</td>
		</tr>
		<tr>
			<td>
				<? ts_df_language(); ?>
			</td>
			<td>
				<select name="langselect" size=2>
					<option value="e"  <? if ($row[7]=="e") echo "selected=\"selected\"";?> >
						English
					</option>
					<option value="a" <? if ($row[7]=="a") echo "selected=\"selected\"";?> >
						Afrikaans
					</option>
				<select/>
			</td>
		</tr>
		<tr>
			<td width="150">
				<? ts_df_email(); ?>
			</td>
			<td>
				<input type="text" name="email" size=30 maxlength=100 value="<? echo $row[13]; ?>" />
			</td>
		</tr>
		<tr>
			<td>
				Fax Number:
			</td>
			<td>
				<input type="text" name="cellphone" size=10 maxlength=10 value="<? echo $row[12]; ?>" />
			</td>
		</tr>
		<tr>
			<td>
				<? ts_df_telephone(); ?>
			</td>
			<td>
				<input type="text" name="homenr" size=10 maxlength=10 value="<? echo $row[11]; ?>" />
			</td>
		</tr>
		<tr>
			<td>
				<? ts_df_post_address(); ?>
			</td>
			<td>
				<input type="text" name="postadd" size=30 maxlength=30 value="<? echo $row[8]; ?>" />
			</td>
		</tr>				
		<tr>
			<td>
				Suburb/Town:
			</td>
			<td>
				<input type="text" name="town" size=30 maxlength=30 value="<? echo $row[9]; ?>" />
			</td>
		</tr>
		<tr>
			<td>
				<? ts_df_post_code(); ?>
			</td>
			<td>
				<input type="text" name="postcode" size=5 maxlength=7 value="<? echo $row[10]; ?>" />
			</td>
		</tr>				

	</table>

	<input type="hidden" name="web_language" value=<? ts_language(); ?>>

	<br>
	
	<table align=center>
		<tr>
			<td colspan=2 align=center>
				<input type=submit value=<? ts_details_button(); ?>>
			</td>
		</tr>
	</table>
	
	</form>
	
	<form action="registration_step_two.php" name="second_step" method=post>

	<input type="hidden" name="step_one" value="complete">

	<table align=center>
		<tr>
			<td colspan=2 align=center>
				<input type=submit value="Proceed Directly to Step 2">
			</td>
		</tr>
	</table>
	
	</form>

<?
	
do_html_footer();

?>
