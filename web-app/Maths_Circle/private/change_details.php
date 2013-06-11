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

	if ($p_bdMonth < 10) 
	{
		$bmonth = "0$p_bdMonth";
	} else 
	{
		$bmonth = $p_bdMonth;
	}
	if ($p_bdDay < 10) 
	{
		$bdday = "0$p_bdDay";
	} else 
	{
		$bdday = $p_bdDay;
	}

	$bday = "$p_bdYear-$bmonth-$bdday";
	$bday = str_replace("/", "", $bday);
	$grade = str_replace("/", "", $p_grade);
	$gender = str_replace("/", "", $p_gender);
	$anonymous = str_replace("/", "", $p_anonymous);
	$language = str_replace("/", "", $p_langselect);
	$uid = $_SESSION['valid_user_id'];
	
	if (!mysql_query("update user set anonymous='$anonymous' where uid='$uid'"))
	{
		echo mysql_error();
	}
	if (!mysql_query("update ucinfo set uemail='$p_email', ucellphone='$p_cellphone', uphone='$p_homenr',
upostal='$p_postadd', utown='$p_town', upcode='$p_postcode', uschool='$p_school', ugrade='$grade' where uid='$uid'"))
	{
		echo mysql_error();
	}
	if (!mysql_query("update upinfo set ufname='$p_fname', uinitials='$p_initials', ulname='$p_lname', ubdate=DATE('$bday'), gender='$gender', language='$language' where uid='$uid'"))
	{
		echo mysql_error();
	}

//-------------------------------------------------
//Show navigation menu
//-------------------------------------------------

	ts_navigation();
    
	ts_successful_update();
	
	do_html_footer();

?>
