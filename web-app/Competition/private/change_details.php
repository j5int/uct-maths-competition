<?

require_once("math_fns.php");
	
session_start();

import_request_variables("p","p_");

//-------------------------------------------------
//Languages
//-------------------------------------------------

	if ($p_web_language == "eng")							//check language
	{
		require("language/functions.eng");    				//load english
	}

	if ($p_web_language == "afr")							//check language
	{
		require("language/functions.afr");    				//load afrikaans
	}

//-------------------------------------------------

require("display_fns.php");

do_html_header(); 

check_valid_user();

//-------------------------------------------------
//Update database
//-------------------------------------------------

	$user = $_SESSION['valid_user'];

	if (!($conn = db_connect()))
	{
		return false;
	}

	$language = str_replace("/", "", $p_langselect);
	$uid = $_SESSION['valid_user_id'];

	if (!mysql_query("update uctmathcomp_school_users set Email='$p_email', Fax='$p_cellphone', Telephone='$p_homenr', Address='$p_postadd', Town='$p_town', Postal_Code='$p_postcode', Name='$p_fname', Language='$language', Correction=1 where comp_uid='$uid'"))
	{
		echo "Could not change details";
		?>
			<form action="registration_step_one.php" name="first_step" method=post>

			<table align=center>
				<tr>
					<td colspan=2 align=center>
						<input type=submit value="Retry">
					</td>
				</tr>
			</table>
	
			</form>
		<?
	} else
	{
		ts_successful_update();

	?>	
		<form action="registration_step_two.php" name="second_step" method=post>

		<input type="hidden" name="step_one" value=complete>

		<table align=center>
			<tr>
				<td colspan=2 align=center>
					<input type=submit value="Proceed to Step 2">
				</td>
			</tr>
		</table>
	
		</form>

	<?
	}

//-------------------------------------------------
//Show navigation menu
//-------------------------------------------------

    
	
	do_html_footer();

?>
