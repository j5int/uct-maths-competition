<?

require_once("math_fns.php");
	
session_start();

import_request_variables("p","p_");

require("language/functions.eng");    				//load english

//-------------------------------------------------

require("display_fns.php");

do_html_header(); 

check_valid_user();

//-------------------------------------------------
//Show navigation menu
//-------------------------------------------------

SAMOS_navigation();

//-------------------------------------------------
//Update database
//-------------------------------------------------

	set_solutions($p_publication);

 	do_html_footer();
	
?>
