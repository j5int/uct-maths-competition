<?

require_once("math_fns.php");
	
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

		require("language/functions.eng");    				//load english

//-------------------------------------------------

require("display_fns.php");

do_html_header(); 

check_valid_user();

//-------------------------------------------------
//Show navigation menu
//-------------------------------------------------

//-------------------------------------------------
//Update database
//-------------------------------------------------

	$uid = $_SESSION['valid_user_id'];

	if (!($conn = db_connect()))
	{
		echo "cannot connect";
		return false;
	}


	if ($p_paper == 1 && $p_level == 9)
	{

	$query = "INSERT INTO junior_problem_set_01(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else

	if ($p_paper == 2 && $p_level == 9)
	{

	$query = "INSERT INTO junior_problem_set_02(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else
	
	if ($p_paper == 3 && $p_level == 9)
	{

	$query = "INSERT INTO junior_problem_set_03(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else

	if ($p_paper == 4 && $p_level == 9)
	{

	$query = "INSERT INTO junior_problem_set_04(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else

	if ($p_paper == 5 && $p_level == 9)
	{

	$query = "INSERT INTO junior_problem_set_05(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else

	if ($p_paper == 1 && $p_level == 12)
	{

	$query = "INSERT INTO senior_problem_set_01(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else

	if ($p_paper == 2 && $p_level == 12)
	{

	$query = "INSERT INTO senior_problem_set_02(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else
	
	if ($p_paper == 3 && $p_level == 12)
	{

	$query = "INSERT INTO senior_problem_set_03(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else

	if ($p_paper == 4 && $p_level == 12)
	{

	$query = "INSERT INTO senior_problem_set_04(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	}

	do_html_footer();
	
?>
