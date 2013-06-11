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

	set_solutions($p_round, $p_Q1, $p_Q2, $p_Q3, $p_Q4, $p_Q5);

 	do_html_footer();
	
?>
