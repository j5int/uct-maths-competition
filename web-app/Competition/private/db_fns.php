<?

function db_connect()
{
	$result = mysql_connect('localhost', 'uctmaoft_1', 'Ghoe1ImK');
	if (!$result)
	{
		echo "Cannot connect";
   		return false;
	}

	$result = mysql_select_db("uctmaoft_1");
	if (!$result)
	{
		echo "No database";
		return false;
	}

	return $result;
}

?>
