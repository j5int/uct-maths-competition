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
//Show navigation menu
//-------------------------------------------------

ts_navigation();

//-------------------------------------------------
//Update database
//-------------------------------------------------

	if (!filled_out2($HTTP_POST_VARS))
	{
		echo "You have not filled out the form completely.
		Please try again.";
		do_html_footer();  
		exit;
	} else 
	{
		if ($p_new_passwd !="" && $p_new_passwd2!="" && $p_old_passwd!="")
		{
			if ($p_new_passwd!=$p_new_passwd2)
			{
				echo "Passwords entered were not the same.  Not changed.<br/>";
			}
			else if (strlen($p_new_passwd)>16 || strlen($p_new_passwd)<6)
			{
				echo "New password must be between 6 and 16 characters.  Try again.<br/>";
			}
			else
			{
			// attempt update
				if (change_password($_SESSION['valid_user'], $p_old_passwd, $p_new_passwd))
				echo "Password changed.<br/>";
				else
				echo "Password could not be changed.<br/>";
			}

		} else
		{
			echo "Password not changed</br>";
		}
	}

do_html_footer();

?>
