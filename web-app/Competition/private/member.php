<?

require_once("math_fns.php");						// include function files for this application

session_start();
global $valid_user;
global $valid_user_id;
global $admin_user;
global $school_user;
global $participant_user;
global $challenge_user;
global $mc_user;
global $lang;										//language variable
global $grap;										//graphics quality variable

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

//if ($_SESSION['admin_user'])
//{
echo "progress";
	check_valid_user();

	school_navigation();
//	participant_navigation();

    if ($p_page == "school_home")
    {
		school_home();    
    } else
    if ($p_page == "school_submit")
    {
		school_submit();
    } else
    if ($p_page == "school_view")
    {
		school_view();
    } else
    if ($p_page == "school_edit")
    {
		school_edit();
    } else
    {
		school_home();    
    }
//} else
//{
//	mc_invalid();
//}
	
do_html_footer();

?>
