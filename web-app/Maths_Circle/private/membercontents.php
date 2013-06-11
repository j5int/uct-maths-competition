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

?>

<html>
	
	<title>UCT Maths Circle</title>
	
	<base target=main>

	<style type="text/css">
		<!-- td { align=center font-family: Arial, Helvetica, sans-serif; font-size: 11pt} -->
	</style>

	<body bgcolor="#330077" text=#ffffff link=#ccccff alink=#ffffff vlink=#cccccc>
	
		<br>

		<p align="center">
			<img src=../graphics/logo70b.gif width=70 height=70 border=0>
		</p>

		
		<table align="center" border="0" cellpadding="0" width="170">
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<font color=white>
						General<br>
						</font>
					</p>
				</td> 
			</tr>
			<tr>
	    		<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="news">
		    				<input type="hidden" name="logged_in" value="true">
				    		<input type="submit" value="             News              ">
						</form>
					</p>
				</td> 
			</tr>
<?
/*
			<tr>
	    		<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="schedule">
		    				<input type="hidden" name="logged_in" value="true">
				    		<input type="submit" value="          Schedule          ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
	    		<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="questionnaire">
		    				<input type="hidden" name="logged_in" value="true">
				    		<input type="submit" value="     Questionnaire      ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="weekly">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="Weekly Performers">
						</form>
					</p>
				</td> 
			</tr>
*/
?>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="marks">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="             Marks             ">
						</form>
					</p>
				</td> 
			</tr>
<?
/*
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<font color=white>
						<br>
						IPMO 2009<br>
						</font>
					</p>
				</td> 
			</tr>
			<tr>
	    		<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
				    		<input type="hidden" name="page" value="ipmo_selection">
				    		<input type="hidden" name="logged_in" value="true">
				    		<input type="submit" value="          Selection          ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
	    		<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
				    		<input type="hidden" name="page" value="homework">
				    		<input type="hidden" name="logged_in" value="true">
				    		<input type="submit" value="         Homework        ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="bs">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="   Beginner Series    ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="is">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="Intermediate Series">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
	    		<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
				    		<input type="hidden" name="page" value="junior">
				    		<input type="hidden" name="logged_in" value="true">
				    		<input type="submit" value="   Junior Rankings    ">
						</form>
					</p>
				</td> 
			</tr>

			<tr>
	    		<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
				    		<input type="hidden" name="page" value="senior">
				    		<input type="hidden" name="logged_in" value="true">
				    		<input type="submit" value="   Senior Rankings   ">
						</form>
					</p>
				</td> 
			</tr>
 */
?>

			
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<font color=white>
						<br>
						IPMO 2010 Online Homework<br>
						</font>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="rules">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="       Rules      ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="j_1996">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Junior MCQ 1996 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="j_1997">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Junior MCQ 1997 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="j_1998">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Junior MCQ 1998 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="j_1999">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Junior MCQ 1999 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="j_2002">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Junior MCQ 2002 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="j_2003">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Junior MCQ 2003 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="j_2004">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Junior MCQ 2004 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="j_2005">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Junior MCQ 2005 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="j_2006">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Junior MCQ 2006 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="s_1996">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Senior MCQ 1996 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="s_1997">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Senior MCQ 1997 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="s_1998">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Senior MCQ 1998 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="s_1999">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Senior MCQ 1999 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="s_2003">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Senior MCQ 2003 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="s_2004">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Senior MCQ 2004 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="s_2005">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Senior MCQ 2005 ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="s_2006">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Senior MCQ 2006 ">
						</form>
					</p>
				</td> 
			</tr>

<?			
/*
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="teams">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="        Teams        ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="test_1">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Selection Test 1  ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="test_2">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Selection Test 2  ">
						</form>
					</p>
				</td> 
			</tr>
			
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<font color=white>
						<br>
						International Maths Olympiad - Preparation<br>
						</font>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="stellenbosch">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Camps and IMO  ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_start">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="   Getting Started    ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_tier_1">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="            Tier 1             ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_tier_2">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="            Tier 2             ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_tutor">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="            Tutor              ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="resources">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="       Resources       ">
						</form>
					</p>
				</td> 
			</tr>

			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<font color=white>
						IMO Preparation Rankings
						</font>
					</p>
				</td> 
			</tr>

			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_proofs">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="           Proofs           ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_tilings_01">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="        Tilings 01        ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_tilings_02">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="        Tilings 02        ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_numbertheory_01">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="Number Theory 01">
						</form>
					</p>
				</td> 
			</tr>

			
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="stc_rankings">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="        Rankings        ">
						</form>
					</p>
				</td> 
			</tr>


			<tr>
	    		<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
				    		<input type="hidden" name="page" value="series">
				    		<input type="hidden" name="logged_in" value="true">
				    		<input type="submit" value="            Series            ">
						</form>
					</p>
				</td> 
			</tr>



			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="junior">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="   Junior Rankings  ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="senior">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Senior Rankings  ">
						</form>
					</p>
				</td> 
			</tr>

			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="cs">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="  Challenge Series ">
						</form>
					</p>
				</td> 
			</tr>

			
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<font color=white>
						<br>
						2007 Rankings<br>
						</font>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
		    				<input type="hidden" name="page" value="notes">
				    		<input type="hidden" name="logged_in" value="true">
	    					<input type="submit" value="       2007 Notes        ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_a">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="           Notes A          ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_b">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="           Notes B          ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_d">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="           Notes D          ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_f">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="            Notes F          ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_i">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="             Notes I          ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_k">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="            Notes K          ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_l">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="            Notes L          ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_p">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="            Notes P          ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_q">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="            Notes Q          ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_r">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="            Notes R          ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_s">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="            Notes S          ">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="notes_t">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="            Notes T          ">
						</form>
					</p>
				</td> 
			</tr>
*/
?>


			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<font color=white>
						<br>
						Admin<br>
						</font>
					</p>
				</td> 
			</tr>



			<tr>
		    	<td width="170" align="center">
						<p align="center">
						<form action="membermain.php" method="post"> 
					    	<input type="hidden" name="page" value="password">
				    		<input type="hidden" name="logged_in" value="true">
			    			<input type="submit" value="Change Password">
						</form>
					</p>
				</td> 
			</tr>
			<tr>
	    		<td width="170" align="center">
					<p align="center">
						<form action="../login.html" method="post"> 
				    		<input type="hidden" name="page" value="login">
					    	<input type="hidden" name="logged_in" value="false">
			    			<input type="submit" value="            Logout           ">
						</form>
					</p>
				</td> 
	  		</tr>
	    </table>

	</body>
	
</html>
