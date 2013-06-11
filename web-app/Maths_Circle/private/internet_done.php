<?

require_once("math_fns.php");
	
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

	if ($p_paper == 101)
	{

	$query = "INSERT INTO mc_questionnaire(mc_uid, FirstName, Surname, Grade, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		} else
		{
			echo "<p align=center>Not successfully submitted</p>";
		}

	} else
	

	if ($p_paper == 199609)
	{

	$query = "INSERT INTO mc_mcq_junior_1996(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17', '$p_Q18', '$p_Q19', '$p_Q20')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else

	if ($p_paper == 199709)
	{

	$query = "INSERT INTO mc_mcq_junior_1997(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17', '$p_Q18', '$p_Q19', '$p_Q20', '$p_Q21', '$p_Q22', '$p_Q23', '$p_Q24', '$p_Q25')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else
	if ($p_paper == 199809)
	{

	$query = "INSERT INTO mc_mcq_junior_1998(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17', '$p_Q18', '$p_Q19', '$p_Q20', '$p_Q21', '$p_Q22', '$p_Q23', '$p_Q24', '$p_Q25')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else
	if ($p_paper == 199909)
	{

	$query = "INSERT INTO mc_mcq_junior_1999(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17', '$p_Q18', '$p_Q19', '$p_Q20', '$p_Q21', '$p_Q22', '$p_Q23', '$p_Q24', '$p_Q25')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else
	if ($p_paper == 200209)
	{

	$query = "INSERT INTO mc_mcq_junior_2002(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17', '$p_Q18', '$p_Q19', '$p_Q20', '$p_Q21', '$p_Q22', '$p_Q23', '$p_Q24', '$p_Q25')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else
	if ($p_paper == 200309)
	{

	$query = "INSERT INTO mc_mcq_junior_2003(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17', '$p_Q18', '$p_Q19', '$p_Q20')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else
	if ($p_paper == 200409)
	{

	$query = "INSERT INTO mc_mcq_junior_2004(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17', '$p_Q18', '$p_Q19', '$p_Q20', '$p_Q21', '$p_Q22', '$p_Q23', '$p_Q24', '$p_Q25')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else
	if ($p_paper == 200509)
	{

	$query = "INSERT INTO mc_mcq_junior_2005(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17', '$p_Q18', '$p_Q19', '$p_Q20')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else
	if ($p_paper == 200609)
	{

	$query = "INSERT INTO mc_mcq_junior_2006(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else


	if ($p_paper == 199612)
	{

	$query = "INSERT INTO mc_mcq_senior_1996(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17', '$p_Q18', '$p_Q19', '$p_Q20')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else

	if ($p_paper == 199712)
	{

	$query = "INSERT INTO mc_mcq_senior_1997(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17', '$p_Q18', '$p_Q19', '$p_Q20', '$p_Q21', '$p_Q22', '$p_Q23', '$p_Q24', '$p_Q25')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else
	if ($p_paper == 199812)
	{

	$query = "INSERT INTO mc_mcq_senior_1998(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17', '$p_Q18', '$p_Q19', '$p_Q20', '$p_Q21', '$p_Q22', '$p_Q23', '$p_Q24', '$p_Q25')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else
	if ($p_paper == 199912)
	{

	$query = "INSERT INTO mc_mcq_senior_1999(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17', '$p_Q18', '$p_Q19', '$p_Q20', '$p_Q21', '$p_Q22', '$p_Q23', '$p_Q24', '$p_Q25')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else
	if ($p_paper == 200312)
	{

	$query = "INSERT INTO mc_mcq_senior_2003(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17', '$p_Q18', '$p_Q19', '$p_Q20')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else

	if ($p_paper == 200412)
	{

	$query = "INSERT INTO mc_mcq_senior_2004(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17', '$p_Q18', '$p_Q19', '$p_Q20', '$p_Q21', '$p_Q22', '$p_Q23', '$p_Q24', '$p_Q25')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else
	if ($p_paper == 200512)
	{

	$query = "INSERT INTO mc_mcq_senior_2005(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15', '$p_Q16', '$p_Q17', '$p_Q18', '$p_Q19', '$p_Q20')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	} else
	if ($p_paper == 200612)
	{

	$query = "INSERT INTO mc_mcq_senior_2006(mc_uid, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15) VALUES('$uid', '$p_Q1', '$p_Q2', '$p_Q3', '$p_Q4', '$p_Q5', '$p_Q6', '$p_Q7', '$p_Q8', '$p_Q9', '$p_Q10', '$p_Q11', '$p_Q12', '$p_Q13', '$p_Q14', '$p_Q15')";

		if (mysql_query($query))
		{
			echo "<p align=center>Successfully submitted</p>";
		}

	}
	
 	do_html_footer();
	
?>
