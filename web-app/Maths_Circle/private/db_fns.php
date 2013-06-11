<?

function db_connect()
{
	$result = mysql_connect('localhost', 'uctmathc_1_1', 'Ghoe1ImK');
	if (!$result)
	{
		echo "Cannot connect";
   		return false;
	}

	$result = mysql_select_db("uctmathc_1");
	if (!$result)
	{
		echo "No database";
		return false;
	}

	return $result;
}

?>
