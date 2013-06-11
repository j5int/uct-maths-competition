<?

require_once("db_fns.php");

function get_member_details($type)
{
	$uid = $_SESSION['valid_user_id'];
	
	if (!($conn = db_connect()))
		return false;
	
	if ($type == 1)
	{
		$query = "select * from user where uid = '$uid'";
	}

	if ($type == 2)
	{
		$query = "select * from upinfo where uid = '$uid'";
	}

	if ($type == 3)
	{
		$query = "select * from ucinfo where uid = '$uid'";
	}

	$result = mysql_query($query);
	
	if (!$result)
		return false;
	
	$row = mysql_fetch_row($result);
	
	return $row;

};

function get_members_list()
{
  if (!($conn = db_connect()))
    return false;
  $result = mysql_query("select surname, firstname, grade from user");
  if (!$result)
    return false;

  //create an array of the URLs
  $member_array = array();

  for ($count = 1; $row = mysql_fetch_row ($result); ++$count)
  {
    $member_array[$count][0] = $row[0];
    $member_array[$count][1] = $row[1];
    $member_array[$count][2] = $row[2];
  }

  return $member_array;

};

function get_marks($type)
{
	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
		return false;

	if ($type == 1)
	{
		$query = "select * from jmarks where uid = '$uid'";
		$result = mysql_query($query);
		if (!$result)
			return false;
		$row = mysql_fetch_row($result);
		$query2 = "select * from juniorsols";
		$result2 = mysql_query($query2);
		if (!$result2)
			return false;
		$row2 = mysql_fetch_row($result2);
		$marks = 0;
		for ($i = 0; $i < $row[1] * 5; $i++)
		{
			if ($row[$i+2] == "")
			{
				$marks++;
			} else
			if ($row[$i+2] == $row2[$i])
			{
				$marks = $marks + 4;
			}
		}
		return $marks;
	}

	if ($type == 2)
	{
		$query = "select * from smarks where uid = '$uid'";
	}

	if ($type == 3)
	{
		$query = "select * from imarks where uid = '$uid'";
	}

	$result = mysql_query($query);
	if (!$result)
		return false;
	$row = mysql_fetch_row($result);
	return $row;	
}
?>
