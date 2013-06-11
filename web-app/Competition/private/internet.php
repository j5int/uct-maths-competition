<?
 require_once("math_fns.php");
 session_start();
 do_html_header("Internet Talent Search");
 check_valid_user();
 display_user_menu();
 
	display_internet_round();
 do_html_footer();
?>
