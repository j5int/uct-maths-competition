<?

require_once('db_fns.php');

/*function get_round()
{
	$uid = $_SESSION['valid_user_id'];
	
	if (!($conn = db_connect()))
		return false;

	$query = "select uround from imarks where uid='$uid'";

	$result = mysql_fetch_row(mysql_query($query));
	
	if ($result)
	{
		return $result[0];
	} else
	{
		return 0;
	}
	

}*/

function set_solutions($publication)
{
	$uid = $_SESSION['valid_user_id'];
	
	if (!($conn = db_connect()))
		return false;


//	if ($round == 1)
//	{
//		$query = "INSERT INTO exploration(uid, uround, Q1_1, Q1_2, Q1_3, Q1_4, Q1_5) 
//							VALUES('$uid', '$round', '$Q1', '$Q2', '$Q3', '$Q4', '$Q5')";
	
//		if (mysql_query($query))
//		{
//			echo "Successfully entered publication<br/>";
//		}

//	}
	

	if ($publication == '05expsollgt6y83f1')
	{
		$mark = 5;
		$query = "UPDATE exploration SET exp1='$mark' where uid = '$uid'";
	
		if (mysql_query($query))
		{
			echo "Successfully entered publication<br/>";
		}
	}

	if ($publication == '10expsollgt5re421')
	{
		$mark = 10;
		$query = "UPDATE exploration SET exp2='$mark' where uid = '$uid'";
	
		if (mysql_query($query))
		{
			echo "Successfully entered publication<br/>";
		}
	}

	if ($publication == '15expsollgtu863fe')
	{
		$mark = 15;
		$query = "UPDATE exploration SET exp3='$mark' where uid = '$uid'";
	
		if (mysql_query($query))
		{
			echo "Successfully entered publication<br/>";
		}
	}

	if ($publication == '20expsollgthh52se')
	{
		$mark = 20;
		$query = "UPDATE exploration SET exp4='$mark' where uid = '$uid'";
	
		if (mysql_query($query))
		{
			echo "Successfully entered publication<br/>";
		}
	}

	if ($publication == '25expsollgtkl75df')
	{
		$mark = 25;
		$query = "UPDATE exploration SET exp5='$mark' where uid = '$uid'";
	
		if (mysql_query($query))
		{
			echo "Successfully entered publication<br/>";
		}
	}

	if ($publication == '30expsollgtcvrt43')
	{
		$mark = 30;
		$query = "UPDATE exploration SET exp6='$mark' where uid = '$uid'";
	
		if (mysql_query($query))
		{
			echo "Successfully entered publication<br/>";
		}
	}

	if ($publication == '35expsollgtftg567')
	{
		$mark = 35;
		$query = "UPDATE exploration SET exp7='$mark' where uid = '$uid'";
	
		if (mysql_query($query))
		{
			echo "Successfully entered publication<br/>";
		}
	}

	if ($publication == '40expsollgtlpk96v')
	{
		$mark = 40;
		$query = "UPDATE exploration SET exp8='$mark' where uid = '$uid'";
	
		if (mysql_query($query))
		{
			echo "Successfully entered publication<br/>";
		}
	}
	
}

?>
