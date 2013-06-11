<html>

<?	

require_once("private/math_fns.php"); 						// include function files for this application

unset($_SESSION['valid_user']);
unset($_SESSION['valid_user_id']);
unset($_SESSION['admin_user']);
unset($_SESSION['school_user']);
unset($_SESSION['participant_user']);
unset($_SESSION['challenge_user']);
unset($_SESSION['mc_user']);

import_request_variables("p","p_");

?>

<body bgcolor="#ffffff">

	<table align="center" border="0" cellpadding="0">
		<tr valign="center" height="100">
			<td width="90" bgcolor="ffffff" align="center" valign="center">
				<a href="http://www.uct.ac.za"><img src="graphics/uct.gif" height="96" border="0"></a>
		    </td>
			<td>
				<font color="0000CC">
					<h1 align="center"> University of Cape Town Mathematics Competition </h1>
				</font>			
			</td>
		</tr>
	</table>

<h2 align="center">Logged out</h2>

</body>

</html>




<?
