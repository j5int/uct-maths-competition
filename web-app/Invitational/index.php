<html>



<?	

    import_request_variables("p","p_");

    require("general_disp.fns");

    cheader();

?>
    
    <table align="center" border="1" cellpadding="1" width="960">
	<tr valign="top" bgcolor="gray">
	    <td width="160" align="center"><br>
		<form action="index.php" method="post"> 
		    <input type="hidden" name="page" value="news">
		    <input type="submit" value="News">
		</form>
	    </td> 
	    <td width="160" align="center"><br>
		<form action="index.php" method="post"> 
		    <input type="hidden" name="page" value="description">
		    <input type="submit" value="Description">
		</form>
	    </td>
	    <td width="160" align="center"><br>
		<form action="index.php" method="post"> 
		    <input type="hidden" name="page" value="papers">
		    <input type="submit" value="Papers">
		</form>
	    </td>
	    <td width="160" align="center"><br>
		<form action="index.php" method="post"> 
		    <input type="hidden" name="page" value="juniors">
		    <input type="submit" value="Junior Results">
		</form>
	    </td>
	    <td width="160" align="center"><br>
		<form action="index.php" method="post"> 
		    <input type="hidden" name="page" value="seniors">
		    <input type="submit" value="Senior Results">
		</form>
	    </td>
	    <td width="160" align="center"><br>
		<form action="index.php" method="post"> 
		    <input type="hidden" name="page" value="links">
		    <input type="submit" value="Links">
		</form>
	    </td>
  	</tr>
    </table>

    <hr align="center">

<?
    
    if ($p_page == "news") 
    {
	news();
    } else
    if ($p_page == "description") 
    {
	description();
    } else
    if ($p_page == "papers") 
    {
    papers();
    } else
    if ($p_page == "juniors") 
    {
	juniors();
    } else
    if ($p_page == "seniors") 
    {
    seniors();
    } else
    if ($p_page == "links") 
    {
	links();
    } else
    {
	news();
    }
		
?>

</body>

</html>
