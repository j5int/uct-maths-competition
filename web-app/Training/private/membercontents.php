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

?>

<html>
	
<title>UCT Mathematics Competition - Training</title>
	
	<base target=main>

	<style type="text/css">
		<!-- td { align=center font-family: Arial, Helvetica, sans-serif; font-size: 11pt} -->
	</style>

	<body bgcolor="#330077" text=#ffffff link=#ccccff alink=#ffffff vlink=#cccccc>
	
		<br>
			<p align="center"><img src=../uct.gif width=70 height=120 border=0> </p>
		<br>
		
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
				<td width=170 align=center>
					<p align=center>
						<form action=membermain.php method=post>
			 			   	<input type=hidden name=page value=news>
			     			<input type=hidden name=logged_in value=true>
			 		    	<input type=submit value= '            News            ' >
			 			</form>
			 		</p>
			 	</td>
			 </tr>

			<tr>
				<td width=170 align=center>
					<p align=center>
						<form action=membermain.php method=post>
			 			   	<input type=hidden name=page value=policies>
			     			<input type=hidden name=logged_in value=true>
			 		    	<input type=submit value= '         Policies          ' >
			 			</form>
			 		</p>
			 	</td>
			 </tr>
		 	 
<?

			if ($user_type_B || $user_type_C)
			{
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=tutor>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '            Tutor             ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=marks>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '           Marks            ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
			}


			if ($user_type_B)
			{
				echo "	<tr>";
		    	echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<font color=white>";
				echo "					<br>Juniors<br>";
				echo "				</font>";
				echo "			</p>";
				echo "		</td>";
				echo "	</tr>";
			}

			if ($user_type_B)
			{
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=junior_questions>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '    Problem Sets    ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=junior_submit>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '          Submit           ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=junior_problem_set_01>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '   Problem Set 1    ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=junior_problem_set_02>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '   Problem Set 2    ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=junior_problem_set_03>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '   Problem Set 3    ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=junior_problem_set_04>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '   Problem Set 4    ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=junior_problem_set_05>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '   Problem Set 5    ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=junior_rankings>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '         Ranking         ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
			}

			if ($user_type_B || $user_type_C)
			{
				echo "	<tr>";
		    	echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<font color=white>";
				echo "					<br>Seniors<br>";
				echo "				</font>";
				echo "			</p>";
				echo "		</td>";
				echo "	</tr>";
			}

			if ($user_type_B || $user_type_C)
			{
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=senior_questions>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '    Problem Sets    ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=senior_submit>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '          Submit           ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=senior_problem_set_01>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '   Problem Set 1    ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=senior_problem_set_02>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '   Problem Set 2    ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=senior_problem_set_03>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '   Problem Set 3    ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
				echo "	<tr>";
				echo "		<td width=170 align=center>";
				echo "			<p align=center>";
				echo "				<form action=membermain.php method=post>";
				echo "			    	<input type=hidden name=page value=senior_problem_set_04>";
				echo "    				<input type=hidden name=logged_in value=true>";
				echo "		    		<input type=submit value= '   Problem Set 4    ' >";
				echo "				</form>";
				echo "			</p>";
				echo "		</td>"; 
				echo "	</tr>";
//				echo "	<tr>";
//				echo "		<td width=170 align=center>";
//				echo "			<p align=center>";
//				echo "				<form action=membermain.php method=post>";
//				echo "			    	<input type=hidden name=page value=senior_rankings>";
//				echo "    				<input type=hidden name=logged_in value=true>";
//				echo "		    		<input type=submit value= '         Ranking         ' >";
//				echo "				</form>";
//				echo "			</p>";
//				echo "		</td>"; 
//				echo "	</tr>";
			}
			
?>	

			<tr>
		    	<td width="170" align="center">
					<p align="center">
						<font color=white>
						<br>
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
						<form action="../login.html"> 
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
