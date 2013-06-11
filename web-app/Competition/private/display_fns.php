<?

function competition_header()

{

?>

    <body bgcolor="turquoise">

    <table align="center" border="0" cellpadding="0" >
 	<tr valign="center">
	    <td width="91">
			<a href="http://www.uct.ac.za"><img src="../graphics/uct.gif" height="96" border="0"></a>
	    </td>
	    <td width="800">
		<font color="0000CC">
			<h1 align="center"> University of Cape Town Mathematics Competition </h1>
		</font>			
	    </td>
	    <td width="100">
		<img height="120" src="../graphics/logo140.gif" border="0">
	    </td>
	</tr>
    </table>

    <hr align="center">

<?

}

function school_navigation()
{

?>

    <table align="center" border="1" cellpadding="1" width="750">
		<tr valign="center" bgcolor="gray">
	    	<td width="140" valign="center" align="center">
				<p>
					<form action="member.php" method="post"> 
				    	<input type="hidden" name="page" value="school_home">
				    	<input type="hidden" name="logged_in" value="true">
			    		<input type="submit" value="Home">
					</form>
				</p>
			</td> 
	    	<td width="140" align="center">
				<p>
					<form action="member.php" method="post"> 
				    	<input type="hidden" name="page" value="school_submit">
				    	<input type="hidden" name="logged_in" value="true">
			    		<input type="submit" value="Submit Entry">
					</form>
				</p>
			</td> 
	    	<td width="140" align="center">
				<p>
					<form action="member.php" method="post"> 
				    	<input type="hidden" name="page" value="school_view">
				    	<input type="hidden" name="logged_in" value="true">
			    		<input type="submit" value="View Entry">
					</form>
				</p>
			</td> 
	    	<td width="140" align="center">
				<p>
					<form action="member.php" method="post"> 
				    	<input type="hidden" name="page" value="school_edit">
				    	<input type="hidden" name="logged_in" value="true">
			    		<input type="submit" value="Edit Entry">
					</form>
				</p>
			</td> 
	    	<td width="140" valign="center" align="center">
				<p>
					<form action="../logout.php" method="post"> 
				    	<input type="hidden" name="page" value="login">
					    <input type="hidden" name="logged_in" value="false">
		    			<input type="submit" value="Logout">
					</form>
				</p>
			</td> 
  		</tr>

    </table>

<?

}

function participant_navigation()
{

?>

    <table align="center" border="1" cellpadding="1" width="700">
		<tr valign="center" bgcolor="gray">
	    	<td width="140" valign="center" align="center">
				<p>
					<form action="member.php" method="post"> 
				    	<input type="hidden" name="page" value="participant_home">
				    	<input type="hidden" name="logged_in" value="true">
			    		<input type="submit" value="Home">
					</form>
				</p>
			</td> 
	    	<td width="140" align="center">
				<p>
					<form action="member.php" method="post"> 
				    	<input type="hidden" name="page" value="participant_submit">
				    	<input type="hidden" name="logged_in" value="true">
			    		<input type="submit" value="Submit Entry">
					</form>
				</p>
			</td> 
	    	<td width="140" align="center">
				<p>
					<form action="member.php" method="post"> 
				    	<input type="hidden" name="page" value="participant_view">
				    	<input type="hidden" name="logged_in" value="true">
			    		<input type="submit" value="View Entry">
					</form>
				</p>
			</td> 
	    	<td width="140" align="center">
				<p>
					<form action="member.php" method="post"> 
				    	<input type="hidden" name="page" value="participant_edit">
				    	<input type="hidden" name="logged_in" value="true">
			    		<input type="submit" value="Edit Entry">
					</form>
				</p>
			</td> 
	    	<td width="140" valign="center" align="center">
				<p>
					<form action="../logout.php" method="post"> 
				    	<input type="hidden" name="page" value="login">
					    <input type="hidden" name="logged_in" value="false">
		    			<input type="submit" value="Logout">
					</form>
				</p>
			</td> 
  		</tr>

    </table>

<?

}

function school_home()
{

?>

<hr align="center">

<h2 align="center"> Home </h2>

<?

	display_school_details_form();

?>

	<form action="step_two.php" name="second_step" method=post>

	<table>
		<tr>
			<td colspan=2 align=center>
				<input type=submit value="Proceed Directly to Step 2">
			</td>
		</tr>
	</table>
	
	</form>


<p align="center">
Remember the final date for submitting your school's entry is Friday 23 March 2007.</p>
<p align="center">
The moment you have submitted your learners will have access to the practice site.
</p>

<?

}

function school_submit()
{

?>

    <hr align="center">

	<h2 align="center"> Submit Entry </h2>

<p align="center">
Remember every school needs to send at least one invigilator.<br>
You will only be able to submit your entry if you also submit the details of at least one invigilator.
</p>
	
<form action="private/member.php" method="post"> 

	<h3 align="center"> Responsible Teacher </h3>

    <table align="center" border="0" cellpadding="0">
	<tr>
		<td align="center">
			Name
		</td>
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	</tr>
	<tr valign="center">
		<td align="center">
			Telephone (H)
		</td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	</tr>
	<tr valign="center">
		<td align="center">
			Fax
		</td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	</tr>
    </table><br>	

	<h3 align="center"> Invigilators </h3>

    <table align="center" border="0" cellpadding="0">
	<tr>
		<td align="center">
			Name
		</td>
		<td align="center">
			Tel / Fax
		</td>
		<td align="center">
			Cell
		</td>
	</tr>
	<tr valign="center">
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	</tr>
    </table><br>	
	

	<h3 align="center"> Grade 8 Individual </h3>

    <table align="center" border="0" cellpadding="0">
	<tr>
		<td align="center">
			First Name
		</td>
		<td align="center">
			Surname
		</td>
		<td align="center">
			Gender (M/F)
		</td>
		<td align="center">
			Language (E/A)
		</td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
    </table><br>	

	<h3 align="center"> Grade 9 Individual </h3>

    <table align="center" border="0" cellpadding="0">
	<tr>
		<td align="center">
			First Name
		</td>
		<td align="center">
			Surname
		</td>
		<td align="center">
			Gender (M/F)
		</td>
		<td align="center">
			Language (E/A)
		</td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
    </table><br>	

	<h3 align="center"> Grade 10 Individual </h3>

    <table align="center" border="0" cellpadding="0">
	<tr>
		<td align="center">
			First Name
		</td>
		<td align="center">
			Surname
		</td>
		<td align="center">
			Gender (M/F)
		</td>
		<td align="center">
			Language (E/A)
		</td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
    </table><br>	

	<h3 align="center"> Grade 11 Individual </h3>

    <table align="center" border="0" cellpadding="0">
	<tr>
		<td align="center">
			First Name
		</td>
		<td align="center">
			Surname
		</td>
		<td align="center">
			Gender (M/F)
		</td>
		<td align="center">
			Language (E/A)
		</td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
    </table><br>	

	<h3 align="center"> Grade 12 Individual </h3>

    <table align="center" border="0" cellpadding="0">
	<tr>
		<td align="center">
			First Name
		</td>
		<td align="center">
			Surname
		</td>
		<td align="center">
			Gender (M/F)
		</td>
		<td align="center">
			Language (E/A)
		</td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	    <td width="100">
	        <input type="text" name="name" size="3" maxlength="1"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="3" maxlength="11"><br>
	    </td>
	</tr>
    </table><br>	
	
	<h3 align="center"> Pairs </h3>

    <table align="center" border="0" cellpadding="0">
	<tr>
		<td align="center">
			Grade
		</td>
		<td align="center">
			Number
		</td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	</tr>
	<tr valign="center">
	    <td width="100">
	        <input type="text" name="name" size="16" maxlength="16"><br>
	    </td>
	    <td>
	        <input type="text" name="surname" size="16" maxlength="16"><br>
	    </td>
	</tr>
    </table><br>	


	
    <table align="center" border="0" cellpadding="0">
        <tr valign="top">
	    <td>
	        <input type="submit" value="Submit">
	    </td>
        </tr>
    </table>

    <input type="hidden" name="page" value="home">

</form>

<?

}

function school_view()
{

?>
	<h2 align="center"> View </h2> 

	<p>This will only be available after you submitted your entry.</p>
<?

}

function school_edit()
{

?>

	<h2 align="center"> Edit </h2> 

	<p>This will only be available after you submitted your entry.</p>

<?

}

?>
