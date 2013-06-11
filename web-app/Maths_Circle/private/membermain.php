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

if ($_SESSION['admin_user'] || $_SESSION['mc_user'])
{

	check_valid_user();

    if ($p_page == "news")
    {
		news();    
    } else
    if ($p_page == "questionnaire")
    {
		questionnaire();    
    } else
    if ($p_page == "schedule")
    {
		schedule();
    } else
    if ($p_page == "weekly")
    {
		weekly();
    } else
    if ($p_page == "ipmo_selection")
    {
		ipmo_selection();
    } else
    if ($p_page == "homework")
    {
		homework();
    } else
    if ($p_page == "ipmo_rankings")
    {
		ipmo_rankings();
    } else
    if ($p_page == "notes_start")
    {
		notes_start();
    } else
    if ($p_page == "notes_tier_1")
    {
		notes_tier_1();
    } else
    if ($p_page == "notes_tier_2")
    {
		notes_tier_2();
    } else
    if ($p_page == "notes_tutor")
    {
		notes_tutor();
    } else
    if ($p_page == "notes_proofs")
    {
		notes_proofs();
    } else
    if ($p_page == "notes_tilings_01")
    {
		notes_tilings_01();
    } else
    if ($p_page == "notes_tilings_02")
    {
		notes_tilings_02();
    } else
    if ($p_page == "notes_numbertheory_01")
    {
		notes_numbertheory_01();
    } else
    if ($p_page == "notes")
    {
		notes();
    } else
    if ($p_page == "series")
    {
		series();
    } else
    if ($p_page == "rules")
    {
		mcq_rules();
    } else
    if ($p_page == "j_1996")
    {
		mcq_junior_1996();
    } else
    if ($p_page == "j_1997")
    {
		mcq_junior_1997();
    } else
    if ($p_page == "j_1998")
    {
		mcq_junior_1998();
    } else
    if ($p_page == "j_1999")
    {
		mcq_junior_1999();
    } else
    if ($p_page == "j_2002")
    {
		mcq_junior_2002();
    } else
    if ($p_page == "j_2003")
    {
		mcq_junior_2003();
    } else
    if ($p_page == "j_2004")
    {
		mcq_junior_2004();
    } else
    if ($p_page == "j_2005")
    {
		mcq_junior_2005();
    } else
    if ($p_page == "j_2006")
    {
		mcq_junior_2006();
    } else
    if ($p_page == "s_1996")
    {
		mcq_senior_1996();
    } else
    if ($p_page == "s_1997")
    {
		mcq_senior_1997();
    } else
    if ($p_page == "s_1998")
    {
		mcq_senior_1998();
    } else
    if ($p_page == "s_1999")
    {
		mcq_senior_1999();
    } else
    if ($p_page == "s_2003")
    {
		mcq_senior_2003();
    } else
    if ($p_page == "s_2004")
    {
		mcq_senior_2004();
    } else
    if ($p_page == "s_2005")
    {
		mcq_senior_2005();
    } else
    if ($p_page == "s_2006")
    {
		mcq_senior_2006();
    } else
    if ($p_page == "ipmo_results")
    {
		ipmo_results();
    } else
    if ($p_page == "teams")
    {
		teams();
    } else
    if ($p_page == "selection")
    {
		selection();
    } else
    if ($p_page == "test_1")
    {
		selection_test_1();
    } else
    if ($p_page == "test_2")
    {
		selection_test_2();
    } else
    if ($p_page == "marks")
    {
		marks();
    } else
    if ($p_page == "junior")
    {
		junior();
    } else
    if ($p_page == "senior")
    {
		senior();
    } else
    if ($p_page == "bs")
    {
		bs();
    } else
    if ($p_page == "is")
    {
		is();
    } else
    if ($p_page == "cs")
    {
		cs();
    } else
    if ($p_page == "notes_a")
    {
		notes_a();
    } else
    if ($p_page == "notes_b")
    {
		notes_b();
    } else
    if ($p_page == "notes_d")
    {
		notes_d();
    } else
    if ($p_page == "notes_f")
    {
		notes_f();
    } else
    if ($p_page == "notes_i")
    {
		notes_i();
    } else
    if ($p_page == "notes_k")
    {
		notes_k();
    } else
    if ($p_page == "notes_l")
    {
		notes_l();
    } else
    if ($p_page == "notes_p")
    {
		notes_p();
    } else
    if ($p_page == "notes_q")
    {
		notes_q();
    } else
    if ($p_page == "notes_r")
    {
		notes_r();
    } else
    if ($p_page == "notes_s")
    {
		notes_s();
    } else
    if ($p_page == "notes_t")
    {
		notes_t();
    } else
    if ($p_page == "stellenbosch")
    {
		stellenbosch();
    } else
    if ($p_page == "stc_rankings")
    {
		stc_rankings();
    } else
    if ($p_page == "resources")
    {
		resources();
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
