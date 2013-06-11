<?

require_once("math_fns.php");						// include function files for this application

session_start();
global $valid_user;
global $valid_user_id;
global $user_type_A;
global $user_type_B;
global $user_type_C;
global $user_type_teacher;
global $user_type_admin;
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
			set_user_types();							//set the types of user they are
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

if ($_SESSION['user_type_A'] || $_SESSION['user_type_B'] || $_SESSION['user_type_C'] || $_SESSION['user_type_teacher'] || $_SESSION['user_type_admin'])
{

	check_valid_user();

    if ($p_page == "news")
    {
		news();    
    } else
    if ($p_page == "policies")
    {
		policies();
    } else
    if ($p_page == "tutor")
    {
		tutor();
    } else
    if ($p_page == "marks")
    {
		marks();
    } else
    if ($p_page == "junior_questions")
    {
		junior_questions();
    } else
    if ($p_page == "junior_submit")
    {
		junior_submit();
    } else
    if ($p_page == "junior_problem_set_01")
    {
		junior_problem_set_01();
    } else
    if ($p_page == "junior_problem_set_02")
    {
		junior_problem_set_02();
    } else
    if ($p_page == "junior_problem_set_03")
    {
		junior_problem_set_03();
    } else
    if ($p_page == "junior_problem_set_04")
    {
		junior_problem_set_04();
    } else
    if ($p_page == "junior_problem_set_05")
    {
		junior_problem_set_05();
    } else
    if ($p_page == "junior_rankings")
    {
		junior_rankings();
    } else
    if ($p_page == "senior_questions")
    {
		senior_questions();
    } else
    if ($p_page == "senior_submit")
    {
		senior_submit();
    } else
    if ($p_page == "senior_problem_set_01")
    {
		senior_problem_set_01();
    } else
    if ($p_page == "senior_problem_set_02")
    {
		senior_problem_set_02();
    } else
    if ($p_page == "senior_problem_set_03")
    {
		senior_problem_set_03();
    } else
    if ($p_page == "senior_problem_set_04")
    {
		senior_problem_set_04();
    } else
    if ($p_page == "senior_rankings")
    {
		senior_rankings();
    } else
    if ($p_page == "password")
    {
		password();
    } else
    {
		news();    
    }
} else
{
	mc_invalid();
}
	
do_html_footer();

?>
