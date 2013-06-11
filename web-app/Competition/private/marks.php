<?
	require_once("math_fns.php");
	session_start();

	do_html_header("Marks");
	check_valid_user();
	display_user_menu();

	display_marks();
	//display_under_construction();

	do_html_footer();

?>
