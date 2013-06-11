<?

function competition_header()

{

?>

    <body bgcolor="#FFCCAA">

    <table align="center" border="0" cellpadding="0" >
 	<tr valign="center">
	    <td>
		<font color="red">
		    <h1 align="center">UCT Mathematics Competition - Training</h1>
		</font>			
	    </td>
	</tr>
    </table>

    <hr align="center">

<?

}

// -------------------------------------------------------------------
//                         Page information
// -------------------------------------------------------------------

function news()
{

?>

	<h2 align="center"> News </h2>

<p><b>
<a href=documents/MCQ_Reading.pdf>Necessary Theory</a>: This contains some important concepts. I will add an update containing some more theory later today (Monday 28 April). Please make sure that you understand it completely. And don't be lazy calculating the primes below 100 and check why the others aren't prime.</b>
</p>
	
<p><b>
Make sure that you know how to correct the mistakes you made. If you can't figure out why you made a mistake or the solution to a question which you got wrong, you can ask help on the tutor page.
</p></b>
	
<p>
Juniors are allowed to compete in the Senior section, but not vice versa. Grade 8's and 9's are classified as Juniors.
</p>
	
<p>
Please try to complete all the questions. If you are stuck and just cannot figure out some questions, you can go to the tutor page and try to get some help on there. This site is for training purposes and thus it is fine to get some help, as long as in the end you understand the solution. The whole purpose is to make sure that you understand the solutions.
</p>
	
<p>
New Problem Sets will become available from time to time. We will also add more if we see that someone has completed them all.
</p>

<?

}

function policies()
{

?>

	<h2 align="center"> Policies </h2>

<p>
Juniors are allowed to compete in the Senior section, but not vice versa.
</p>

<p>
Since this site is for training only and not for any selection purpose, getting help and hints from each other or from the tutor is completely acceptable. The only request is that, if you get some help please make sure that you indeed do understand the solution to the question or otherwise it will be of no benefit to you. We suggest that you ask the tutor if possible.
</p>
	
<?

}

function tutor()
{

?>

	<h2 align="center"> Tutor </h2>

If you need some help you can contact the tutor by clicking underneath if the talk bubble is green. The tutor will be online frequently so if not availble immediately you can try again a bit later. The conversation will start as "guest" and therefore you can choose to remain anonymous (of course you can identify yourself if you want). 

<iframe src="http://www.google.com/talk/service/badge/Show?tk=z01q6amlqbe3k2nu89a46b8e2tv6ef5c8heefv55cm93o3hq9c45anoasmpbp403kocbu8a8g8uldf1nina14j8v9997cd55ceicu9v948nmtva67i9vhf7q4b6d43anha7dabbeusvuf1bvunltmc2eikrjuidlagq6vpln63i351eo1hdmb7cujb5d07l5qk0&amp;w=200&amp;h=60" frameborder="0" allowtransparency="true" width="200" height="60"></iframe>

<p><b>
The tutor function wasn't working this morning since I couldn't access the account. It seems to be working now again. But please be aware that there might be some connection problems from my end.
</b>
</p>

<p>
When you click on the link another window should open. However, if nothing happens after a while in it your internet connection can probably not handle it.
</p>

<?

}

function marks()
{

?>

	<h2 align="center"> Marks </h2>

<?

//--------------------------------------------------------------------------------------------------------------------------------------------------------
//Junior Problem Set 01
//--------------------------------------------------------------------------------------------------------------------------------------------------------
require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
		return false;

	$query = "select * from junior_problem_set_01 where mc_uid = '$uid'";

	$result = mysql_query($query);
	if (!$result)
		return false;
	$marks = mysql_fetch_row($result);

	$query2 = "select * from junior_problem_set_01 where mc_uid = '0'";

	$result2 = mysql_query($query2);
	if (!$result2)
		return false;
	$solution = mysql_fetch_row($result2);
	
	if ($marks != false)
		{
			echo "<h3> Junior Problem Set 1 </h3>";
			
			echo "<table border=1 width=600>";

			echo "<tr>";
			echo "<td><b> Question </b></td>";

			for ($i=1; $i <= 10 ; $i++)
			{
				echo "<td align=center> $i  </td>";
			}
			echo "<td align=center><b> Total </b></td>";
			echo "</tr>";

			echo "<tr>";
			$Total = 0;
			echo "<td><b> Mark </b></td>";
			
			for ($i=1; $i <= 10 ; $i++)
			{
				if ($marks[$i]==$solution[$i])
				{
					echo "<td align=center>5</td>";
					$Total = $Total+5;
				} else
				if ($marks[$i]==NULL)
				{
					echo "<td align=center>0</td>";
					$Total = $Total+0;
				} else
				{
					echo "<td align=center> 1 </td>";
					$Total--;
				}
			}
			echo "<td align=center>$Total</td>";
			echo "</tr>";
			echo "</table>";
			echo "<br>";
			
		}

//--------------------------------------------------------------------------------------------------------------------------------------------------------
//Junior Problem Set 02
//--------------------------------------------------------------------------------------------------------------------------------------------------------
require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
		return false;

	$query = "select * from junior_problem_set_02 where mc_uid = '$uid'";

	$result = mysql_query($query);
	if (!$result)
		return false;
	$marks = mysql_fetch_row($result);

	$query2 = "select * from junior_problem_set_02 where mc_uid = '0'";

	$result2 = mysql_query($query2);
	if (!$result2)
		return false;
	$solution = mysql_fetch_row($result2);
	
	if ($marks != false)
		{
			echo "<h3> Junior Problem Set 2 </h3>";
			
			echo "<table border=1 width=600>";

			echo "<tr>";
			echo "<td><b> Question </b></td>";

			for ($i=1; $i <= 10 ; $i++)
			{
				echo "<td align=center> $i  </td>";
			}
			echo "<td align=center><b> Total </b></td>";
			echo "</tr>";

			echo "<tr>";
			$Total = 0;
			echo "<td><b> Mark </b></td>";
			
			for ($i=1; $i <= 10 ; $i++)
			{
				if ($marks[$i]==$solution[$i])
				{
					echo "<td align=center>5</td>";
					$Total = $Total+5;
				} else
				if ($marks[$i]==NULL)
				{
					echo "<td align=center>0</td>";
					$Total = $Total+0;
				} else
				{
					echo "<td align=center> 1 </td>";
					$Total--;
				}
			}
			echo "<td align=center>$Total</td>";
			echo "</tr>";
			echo "</table>";
			echo "<br>";
			
		}

//--------------------------------------------------------------------------------------------------------------------------------------------------------
//Junior Problem Set 03
//--------------------------------------------------------------------------------------------------------------------------------------------------------
require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
		return false;

	$query = "select * from junior_problem_set_03 where mc_uid = '$uid'";

	$result = mysql_query($query);
	if (!$result)
		return false;
	$marks = mysql_fetch_row($result);

	$query2 = "select * from junior_problem_set_03 where mc_uid = '0'";

	$result2 = mysql_query($query2);
	if (!$result2)
		return false;
	$solution = mysql_fetch_row($result2);
	
	if ($marks != false)
		{
			echo "<h3> Junior Problem Set 3 </h3>";
			
			echo "<table border=1 width=600>";

			echo "<tr>";
			echo "<td><b> Question </b></td>";

			for ($i=1; $i <= 10 ; $i++)
			{
				echo "<td align=center> $i  </td>";
			}
			echo "<td align=center><b> Total </b></td>";
			echo "</tr>";

			echo "<tr>";
			$Total = 0;
			echo "<td><b> Mark </b></td>";
			
			for ($i=1; $i <= 10 ; $i++)
			{
				if ($marks[$i]==$solution[$i])
				{
					echo "<td align=center>5</td>";
					$Total = $Total+5;
				} else
				if ($marks[$i]==NULL)
				{
					echo "<td align=center>0</td>";
					$Total = $Total+0;
				} else
				{
					echo "<td align=center> 1 </td>";
					$Total--;
				}
			}
			echo "<td align=center>$Total</td>";
			echo "</tr>";
			echo "</table>";
			echo "<br>";
			
		}

//--------------------------------------------------------------------------------------------------------------------------------------------------------
//Junior Problem Set 04
//--------------------------------------------------------------------------------------------------------------------------------------------------------
require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
		return false;

	$query = "select * from junior_problem_set_04 where mc_uid = '$uid'";

	$result = mysql_query($query);
	if (!$result)
		return false;
	$marks = mysql_fetch_row($result);

	$query2 = "select * from junior_problem_set_04 where mc_uid = '0'";

	$result2 = mysql_query($query2);
	if (!$result2)
		return false;
	$solution = mysql_fetch_row($result2);
	
	if ($marks != false)
		{
			echo "<h3> Junior Problem Set 4 </h3>";
			
			echo "<table border=1 width=600>";

			echo "<tr>";
			echo "<td><b> Question </b></td>";

			for ($i=1; $i <= 10 ; $i++)
			{
				echo "<td align=center> $i  </td>";
			}
			echo "<td align=center><b> Total </b></td>";
			echo "</tr>";

			echo "<tr>";
			$Total = 0;
			echo "<td><b> Mark </b></td>";
			
			for ($i=1; $i <= 10 ; $i++)
			{
				if ($marks[$i]==$solution[$i])
				{
					echo "<td align=center>5</td>";
					$Total = $Total+5;
				} else
				if ($marks[$i]==NULL)
				{
					echo "<td align=center>0</td>";
					$Total = $Total+0;
				} else
				{
					echo "<td align=center> 1 </td>";
					$Total--;
				}
			}
			echo "<td align=center>$Total</td>";
			echo "</tr>";
			echo "</table>";
			echo "<br>";
			
		}

//--------------------------------------------------------------------------------------------------------------------------------------------------------
//Junior Problem Set 05
//--------------------------------------------------------------------------------------------------------------------------------------------------------
require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
		return false;

	$query = "select * from junior_problem_set_05 where mc_uid = '$uid'";

	$result = mysql_query($query);
	if (!$result)
		return false;
	$marks = mysql_fetch_row($result);

	$query2 = "select * from junior_problem_set_05 where mc_uid = '0'";

	$result2 = mysql_query($query2);
	if (!$result2)
		return false;
	$solution = mysql_fetch_row($result2);
	
	if ($marks != false)
		{
			echo "<h3> Junior Problem Set 5 </h3>";
			
			echo "<table border=1 width=600>";

			echo "<tr>";
			echo "<td><b> Question </b></td>";

			for ($i=1; $i <= 10 ; $i++)
			{
				echo "<td align=center> $i  </td>";
			}
			echo "<td align=center><b> Total </b></td>";
			echo "</tr>";

			echo "<tr>";
			$Total = 0;
			echo "<td><b> Mark </b></td>";
			
			for ($i=1; $i <= 10 ; $i++)
			{
				if ($marks[$i]==$solution[$i])
				{
					echo "<td align=center>5</td>";
					$Total = $Total+5;
				} else
				if ($marks[$i]==NULL)
				{
					echo "<td align=center>0</td>";
					$Total = $Total+0;
				} else
				{
					echo "<td align=center> 1 </td>";
					$Total--;
				}
			}
			echo "<td align=center>$Total</td>";
			echo "</tr>";
			echo "</table>";
			echo "<br>";
			
		}
		
//--------------------------------------------------------------------------------------------------------------------------------------------------------
//Senior Problem Set 01
//--------------------------------------------------------------------------------------------------------------------------------------------------------
require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
		return false;

	$query = "select * from senior_problem_set_01 where mc_uid = '$uid'";

	$result = mysql_query($query);
	if (!$result)
		return false;
	$marks = mysql_fetch_row($result);

	$query2 = "select * from senior_problem_set_01 where mc_uid = '0'";

	$result2 = mysql_query($query2);
	if (!$result2)
		return false;
	$solution = mysql_fetch_row($result2);
	
	if ($marks != false)
		{
			echo "<h3> Senior Problem Set 1 </h3>";
			
			echo "<table border=1 width=600>";

			echo "<tr>";
			echo "<td><b> Question </b></td>";

			for ($i=1; $i <= 10 ; $i++)
			{
				echo "<td align=center> $i  </td>";
			}
			echo "<td align=center><b> Total </b></td>";
			echo "</tr>";

			echo "<tr>";
			$Total = 0;
			echo "<td><b> Mark </b></td>";
			
			for ($i=1; $i <= 10 ; $i++)
			{
				if ($marks[$i]==$solution[$i])
				{
					echo "<td align=center>5</td>";
					$Total = $Total+5;
				} else
				if ($marks[$i]==NULL)
				{
					echo "<td align=center>0</td>";
					$Total = $Total+0;
				} else
				{
					echo "<td align=center> 1 </td>";
					$Total--;
				}
			}
			echo "<td align=center>$Total</td>";
			echo "</tr>";
			echo "</table>";
			echo "<br>";
			
		}

//--------------------------------------------------------------------------------------------------------------------------------------------------------
//Senior Problem Set 02
//--------------------------------------------------------------------------------------------------------------------------------------------------------
require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
		return false;

	$query = "select * from senior_problem_set_02 where mc_uid = '$uid'";

	$result = mysql_query($query);
	if (!$result)
		return false;
	$marks = mysql_fetch_row($result);

	$query2 = "select * from senior_problem_set_02 where mc_uid = '0'";

	$result2 = mysql_query($query2);
	if (!$result2)
		return false;
	$solution = mysql_fetch_row($result2);
	
	if ($marks != false)
		{
			echo "<h3> Senior Problem Set 2 </h3>";
			
			echo "<table border=1 width=600>";

			echo "<tr>";
			echo "<td><b> Question </b></td>";

			for ($i=1; $i <= 10 ; $i++)
			{
				echo "<td align=center> $i  </td>";
			}
			echo "<td align=center><b> Total </b></td>";
			echo "</tr>";

			echo "<tr>";
			$Total = 0;
			echo "<td><b> Mark </b></td>";
			
			for ($i=1; $i <= 10 ; $i++)
			{
				if ($marks[$i]==$solution[$i])
				{
					echo "<td align=center>5</td>";
					$Total = $Total+5;
				} else
				if ($marks[$i]==NULL)
				{
					echo "<td align=center>0</td>";
					$Total = $Total+0;
				} else
				{
					echo "<td align=center> 1 </td>";
					$Total--;
				}
			}
			echo "<td align=center>$Total</td>";
			echo "</tr>";
			echo "</table>";
			echo "<br>";
			
		}

//--------------------------------------------------------------------------------------------------------------------------------------------------------
//Senior Problem Set 03
//--------------------------------------------------------------------------------------------------------------------------------------------------------
require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
		return false;

	$query = "select * from senior_problem_set_03 where mc_uid = '$uid'";

	$result = mysql_query($query);
	if (!$result)
		return false;
	$marks = mysql_fetch_row($result);

	$query2 = "select * from senior_problem_set_03 where mc_uid = '0'";

	$result2 = mysql_query($query2);
	if (!$result2)
		return false;
	$solution = mysql_fetch_row($result2);
	
	if ($marks != false)
		{
			echo "<h3> Senior Problem Set 3 </h3>";
			
			echo "<table border=1 width=600>";

			echo "<tr>";
			echo "<td><b> Question </b></td>";

			for ($i=1; $i <= 10 ; $i++)
			{
				echo "<td align=center> $i  </td>";
			}
			echo "<td align=center><b> Total </b></td>";
			echo "</tr>";

			echo "<tr>";
			$Total = 0;
			echo "<td><b> Mark </b></td>";
			
			for ($i=1; $i <= 10 ; $i++)
			{
				if ($marks[$i]==$solution[$i])
				{
					echo "<td align=center>5</td>";
					$Total = $Total+5;
				} else
				if ($marks[$i]==NULL)
				{
					echo "<td align=center>0</td>";
					$Total = $Total+0;
				} else
				{
					echo "<td align=center> 1 </td>";
					$Total--;
				}
			}
			echo "<td align=center>$Total</td>";
			echo "</tr>";
			echo "</table>";
			echo "<br>";
			
		}

//--------------------------------------------------------------------------------------------------------------------------------------------------------
//Senior Problem Set 04
//--------------------------------------------------------------------------------------------------------------------------------------------------------
require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
		return false;

	$query = "select * from senior_problem_set_04 where mc_uid = '$uid'";

	$result = mysql_query($query);
	if (!$result)
		return false;
	$marks = mysql_fetch_row($result);

	$query2 = "select * from senior_problem_set_04 where mc_uid = '0'";

	$result2 = mysql_query($query2);
	if (!$result2)
		return false;
	$solution = mysql_fetch_row($result2);
	
	if ($marks != false)
		{
			echo "<h3> Senior Problem Set 4 </h3>";
			
			echo "<table border=1 width=600>";

			echo "<tr>";
			echo "<td><b> Question </b></td>";

			for ($i=1; $i <= 10 ; $i++)
			{
				echo "<td align=center> $i  </td>";
			}
			echo "<td align=center><b> Total </b></td>";
			echo "</tr>";

			echo "<tr>";
			$Total = 0;
			echo "<td><b> Mark </b></td>";
			
			for ($i=1; $i <= 10 ; $i++)
			{
				if ($marks[$i]==$solution[$i])
				{
					echo "<td align=center>5</td>";
					$Total = $Total+5;
				} else
				if ($marks[$i]==NULL)
				{
					echo "<td align=center>0</td>";
					$Total = $Total+0;
				} else
				{
					echo "<td align=center> 1 </td>";
					$Total--;
				}
			}
			echo "<td align=center>$Total</td>";
			echo "</tr>";
			echo "</table>";
			echo "<br>";
			
		}
		
//--------------------------------------------------------------------------------------------------------------------------------------------------------

		
}

function junior_questions()
{

?>

	<h2 align="center"> Junior Problem Sets </h2>

	<p>
		<a href=documents/Junior_Problem_Set_01.pdf>Problem Set 1</a><br>	
		<a href=documents/Junior_Problem_Set_02.pdf>Problem Set 2</a><br>	
		<a href=documents/Junior_Problem_Set_03.pdf>Problem Set 3</a><br>	
		<a href=documents/Junior_Problem_Set_04.pdf>Problem Set 4</a><br>	
		<a href=documents/Junior_Problem_Set_05.pdf>Problem Set 5</a><br>	
	</p>
	
<?

}

function junior_submit()
{

?>

	<h2 align="center"> Junior Submit Solutions </h2>

<p>
Please enter the problem set number into the indicated box or otherwise it will not submit correctly. After you submit there should be a message "Successfully Submitted". If you do not get this message you will have to retry.
</p>

<form action=internet_done.php method=post>
	<table align="center" width="300">
		<tr>
		    <td align="center" colspan=5>
	    	    Problem Set: <input type="text" name="paper" size="2" maxlength="2"><br>
		    </td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 1</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q1" value="a"></input></td>
			<td> B <input type="radio" name="Q1" value="b"></input></td>
			<td> C <input type="radio" name="Q1" value="c"></input></td>
			<td> D <input type="radio" name="Q1" value="d"></input></td>
			<td> E <input type="radio" name="Q1" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 2</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q2" value="a"></input></td>
			<td> B <input type="radio" name="Q2" value="b"></input></td>
			<td> C <input type="radio" name="Q2" value="c"></input></td>
			<td> D <input type="radio" name="Q2" value="d"></input></td>
			<td> E <input type="radio" name="Q2" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 3</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q3" value="a"></input></td>
			<td> B <input type="radio" name="Q3" value="b"></input></td>
			<td> C <input type="radio" name="Q3" value="c"></input></td>
			<td> D <input type="radio" name="Q3" value="d"></input></td>
			<td> E <input type="radio" name="Q3" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 4</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q4" value="a"></input></td>
			<td> B <input type="radio" name="Q4" value="b"></input></td>
			<td> C <input type="radio" name="Q4" value="c"></input></td>
			<td> D <input type="radio" name="Q4" value="d"></input></td>
			<td> E <input type="radio" name="Q4" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 5</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q5" value="a"></input></td>
			<td> B <input type="radio" name="Q5" value="b"></input></td>
			<td> C <input type="radio" name="Q5" value="c"></input></td>
			<td> D <input type="radio" name="Q5" value="d"></input></td>
			<td> E <input type="radio" name="Q5" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 6</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q6" value="a"></input></td>
			<td> B <input type="radio" name="Q6" value="b"></input></td>
			<td> C <input type="radio" name="Q6" value="c"></input></td>
			<td> D <input type="radio" name="Q6" value="d"></input></td>
			<td> E <input type="radio" name="Q6" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 7</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q7" value="a"></input></td>
			<td> B <input type="radio" name="Q7" value="b"></input></td>
			<td> C <input type="radio" name="Q7" value="c"></input></td>
			<td> D <input type="radio" name="Q7" value="d"></input></td>
			<td> E <input type="radio" name="Q7" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 8</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q8" value="a"></input></td>
			<td> B <input type="radio" name="Q8" value="b"></input></td>
			<td> C <input type="radio" name="Q8" value="c"></input></td>
			<td> D <input type="radio" name="Q8" value="d"></input></td>
			<td> E <input type="radio" name="Q8" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 9</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q9" value="a"></input></td>
			<td> B <input type="radio" name="Q9" value="b"></input></td>
			<td> C <input type="radio" name="Q9" value="c"></input></td>
			<td> D <input type="radio" name="Q9" value="d"></input></td>
			<td> E <input type="radio" name="Q9" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 10</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q10" value="a"></input></td>
			<td> B <input type="radio" name="Q10" value="b"></input></td>
			<td> C <input type="radio" name="Q10" value="c"></input></td>
			<td> D <input type="radio" name="Q10" value="d"></input></td>
			<td> E <input type="radio" name="Q10" value="e"></input></td>
		</tr>

	</table>
	<table align=center><tr><td>
	<input type=hidden name=level value= 9>
	<input type=submit value= Submit>
	</td></tr></table>
	</form>
	
<?

}

function junior_problem_set_01()
{

?>

	<h2 align="center"> Junior Problem Set 1 - Ranking </h2>

<?

require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
	return false;

	$query = "select * from junior_problem_set_01";
	$result = mysql_query($query);
	$num_results = mysql_num_rows($result);

	$user[$num_results];
	$mark[$num_results];
	$name[$num_results];
	$surname[$num_results];
	$school[$num_results];
	$grade[$num_results];
	$number = 0;

	$solutions = mysql_fetch_row($result);
	if ($solutions[0] == 0)
	{
	
	//read everything out
	for ($i = 1; $i < $num_results; $i++)
	{
		$row = mysql_fetch_row($result);
		$user[$i] = $row[0];
		$total = 0;
		for ($j=1; $j<=10; $j++)
		{
			if ($row[$j] == $solutions[$j])
			{
				$total=$total+5;
			} else
			if ($row[$j] == NULL)
			{
				$total=$total+0;
			} else
			{
				$total--;
			}
			
		}
		$mark[$i] = $total;
		$number++;
	} 
	}

	//sort
	for ($x = 1; $x < $num_results; $x++)
	{
		for ($count = 1; $count < $num_results; $count++)
		{
			if ($mark[$count] < $mark[$count+1])
			{
				$temp_user = $user[$count];
				$temp_mark = $mark[$count];

				$user[$count] = $user[$count+1];
				$mark[$count] = $mark[$count+1];

				$user[$count+1] = $temp_user;
				$mark[$count+1] = $temp_mark;
			}
		}
	}

	//find top 20 details
	for ($count = 1; $count < $num_results; $count++)
	{

		if (!($conn = db_connect()))
		return false;

		$query = "select * from user where uid = '$user[$count]'";
		$result = mysql_query($query);
		if (!$result)
		return false;
		$pinfo = mysql_fetch_row($result);

		$name[$count] = $pinfo[6];
		$surname[$count] = $pinfo[7];
		$school[$count] = $pinfo[8];
		$grade[$count] = $pinfo[9];

	}

	//display top  20
	echo "<table align=center border=1 width=700>";
	echo "<tr>";
	echo "<td align=center><b> Rank </b></td>";
	echo "<td><b> Name </b></td><td><b> Surname </b></td>";
	echo "<td align=center><b> School </b></td><td align=center><b> Grade </b></td>";
	echo "<td align=center><b> Mark </b></td>";
	echo "</tr>";
	echo "<tr>";
	echo "<td align=center><b> Max </b></td>";
	echo "<td><b> Possible </b></td><td><b> Mark </b></td><td align=center><b> - </b></td><td align=center><b> - </b></td>";
	echo "<td align=center><b> 50 </b></td>";
	echo "</tr>";
	
	$rank = 0;
	
	for ($out = 1; $out < $num_results; $out++)
	{
			echo "<tr>";
			$rank++;
			echo "<td align=center> $rank </td>";
			echo "<td>$name[$out]</td><td>$surname[$out]</td><td>$school[$out]</td>";
			echo "<td align=center> $grade[$out] </td>";
			echo "<td align=center>$mark[$out]</td>";
			echo "</tr>";
	}

	echo "</table>";

}

function junior_problem_set_02()
{

?>

	<h2 align="center"> Junior Problem Set 2 - Ranking </h2>

<?

require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
	return false;

	$query = "select * from junior_problem_set_02";
	$result = mysql_query($query);
	$num_results = mysql_num_rows($result);

	$user[$num_results];
	$mark[$num_results];
	$name[$num_results];
	$surname[$num_results];
	$school[$num_results];
	$grade[$num_results];
	$number = 0;

	$solutions = mysql_fetch_row($result);
	if ($solutions[0] == 0)
	{
	
	//read everything out
	for ($i = 1; $i < $num_results; $i++)
	{
		$row = mysql_fetch_row($result);
		$user[$i] = $row[0];
		$total = 0;
		for ($j=1; $j<=10; $j++)
		{
			if ($row[$j] == $solutions[$j])
			{
				$total=$total+5;
			} else
			if ($row[$j] == NULL)
			{
				$total=$total+0;
			} else
			{
				$total--;
			}
			
		}
		$mark[$i] = $total;
		$number++;
	} 
	}

	//sort
	for ($x = 1; $x < $num_results; $x++)
	{
		for ($count = 1; $count < $num_results; $count++)
		{
			if ($mark[$count] < $mark[$count+1])
			{
				$temp_user = $user[$count];
				$temp_mark = $mark[$count];

				$user[$count] = $user[$count+1];
				$mark[$count] = $mark[$count+1];

				$user[$count+1] = $temp_user;
				$mark[$count+1] = $temp_mark;
			}
		}
	}

	//find top 20 details
	for ($count = 1; $count < $num_results; $count++)
	{

		if (!($conn = db_connect()))
		return false;

		$query = "select * from user where uid = '$user[$count]'";
		$result = mysql_query($query);
		if (!$result)
		return false;
		$pinfo = mysql_fetch_row($result);

		$name[$count] = $pinfo[6];
		$surname[$count] = $pinfo[7];
		$school[$count] = $pinfo[8];
		$grade[$count] = $pinfo[9];

	}

	//display top  20
	echo "<table align=center border=1 width=700>";
	echo "<tr>";
	echo "<td align=center><b> Rank </b></td>";
	echo "<td><b> Name </b></td><td><b> Surname </b></td>";
	echo "<td align=center><b> School </b></td><td align=center><b> Grade </b></td>";
	echo "<td align=center><b> Mark </b></td>";
	echo "</tr>";
	echo "<tr>";
	echo "<td align=center><b> Max </b></td>";
	echo "<td><b> Possible </b></td><td><b> Mark </b></td><td align=center><b> - </b></td><td align=center><b> - </b></td>";
	echo "<td align=center><b> 50 </b></td>";
	echo "</tr>";
	
	$rank = 0;
	
	for ($out = 1; $out < $num_results; $out++)
	{
			echo "<tr>";
			$rank++;
			echo "<td align=center> $rank </td>";
			echo "<td>$name[$out]</td><td>$surname[$out]</td><td>$school[$out]</td>";
			echo "<td align=center> $grade[$out] </td>";
			echo "<td align=center>$mark[$out]</td>";
			echo "</tr>";
	}

	echo "</table>";

}

function junior_problem_set_03()
{

?>

	<h2 align="center"> Junior Problem Set 3 - Ranking </h2>

<?

require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
	return false;

	$query = "select * from junior_problem_set_03";
	$result = mysql_query($query);
	$num_results = mysql_num_rows($result);

	$user[$num_results];
	$mark[$num_results];
	$name[$num_results];
	$surname[$num_results];
	$school[$num_results];
	$grade[$num_results];
	$number = 0;

	$solutions = mysql_fetch_row($result);
	if ($solutions[0] == 0)
	{
	
	//read everything out
	for ($i = 1; $i < $num_results; $i++)
	{
		$row = mysql_fetch_row($result);
		$user[$i] = $row[0];
		$total = 0;
		for ($j=1; $j<=10; $j++)
		{
			if ($row[$j] == $solutions[$j])
			{
				$total=$total+5;
			} else
			if ($row[$j] == NULL)
			{
				$total=$total+0;
			} else
			{
				$total--;
			}
			
		}
		$mark[$i] = $total;
		$number++;
	} 
	}

	//sort
	for ($x = 1; $x < $num_results; $x++)
	{
		for ($count = 1; $count < $num_results; $count++)
		{
			if ($mark[$count] < $mark[$count+1])
			{
				$temp_user = $user[$count];
				$temp_mark = $mark[$count];

				$user[$count] = $user[$count+1];
				$mark[$count] = $mark[$count+1];

				$user[$count+1] = $temp_user;
				$mark[$count+1] = $temp_mark;
			}
		}
	}

	//find top 20 details
	for ($count = 1; $count < $num_results; $count++)
	{

		if (!($conn = db_connect()))
		return false;

		$query = "select * from user where uid = '$user[$count]'";
		$result = mysql_query($query);
		if (!$result)
		return false;
		$pinfo = mysql_fetch_row($result);

		$name[$count] = $pinfo[6];
		$surname[$count] = $pinfo[7];
		$school[$count] = $pinfo[8];
		$grade[$count] = $pinfo[9];

	}

	//display top  20
	echo "<table align=center border=1 width=700>";
	echo "<tr>";
	echo "<td align=center><b> Rank </b></td>";
	echo "<td><b> Name </b></td><td><b> Surname </b></td>";
	echo "<td align=center><b> School </b></td><td align=center><b> Grade </b></td>";
	echo "<td align=center><b> Mark </b></td>";
	echo "</tr>";
	echo "<tr>";
	echo "<td align=center><b> Max </b></td>";
	echo "<td><b> Possible </b></td><td><b> Mark </b></td><td align=center><b> - </b></td><td align=center><b> - </b></td>";
	echo "<td align=center><b> 50 </b></td>";
	echo "</tr>";
	
	$rank = 0;
	
	for ($out = 1; $out < $num_results; $out++)
	{
			echo "<tr>";
			$rank++;
			echo "<td align=center> $rank </td>";
			echo "<td>$name[$out]</td><td>$surname[$out]</td><td>$school[$out]</td>";
			echo "<td align=center> $grade[$out] </td>";
			echo "<td align=center>$mark[$out]</td>";
			echo "</tr>";
	}

	echo "</table>";

}

function junior_problem_set_04()
{

?>

	<h2 align="center"> Junior Problem Set 4 - Ranking </h2>

<?

require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
	return false;

	$query = "select * from junior_problem_set_04";
	$result = mysql_query($query);
	$num_results = mysql_num_rows($result);

	$user[$num_results];
	$mark[$num_results];
	$name[$num_results];
	$surname[$num_results];
	$school[$num_results];
	$grade[$num_results];
	$number = 0;

	$solutions = mysql_fetch_row($result);
	if ($solutions[0] == 0)
	{
	
	//read everything out
	for ($i = 1; $i < $num_results; $i++)
	{
		$row = mysql_fetch_row($result);
		$user[$i] = $row[0];
		$total = 0;
		for ($j=1; $j<=10; $j++)
		{
			if ($row[$j] == $solutions[$j])
			{
				$total=$total+5;
			} else
			if ($row[$j] == NULL)
			{
				$total=$total+0;
			} else
			{
				$total--;
			}
			
		}
		$mark[$i] = $total;
		$number++;
	} 
	}

	//sort
	for ($x = 1; $x < $num_results; $x++)
	{
		for ($count = 1; $count < $num_results; $count++)
		{
			if ($mark[$count] < $mark[$count+1])
			{
				$temp_user = $user[$count];
				$temp_mark = $mark[$count];

				$user[$count] = $user[$count+1];
				$mark[$count] = $mark[$count+1];

				$user[$count+1] = $temp_user;
				$mark[$count+1] = $temp_mark;
			}
		}
	}

	//find top 20 details
	for ($count = 1; $count < $num_results; $count++)
	{

		if (!($conn = db_connect()))
		return false;

		$query = "select * from user where uid = '$user[$count]'";
		$result = mysql_query($query);
		if (!$result)
		return false;
		$pinfo = mysql_fetch_row($result);

		$name[$count] = $pinfo[6];
		$surname[$count] = $pinfo[7];
		$school[$count] = $pinfo[8];
		$grade[$count] = $pinfo[9];

	}

	//display top  20
	echo "<table align=center border=1 width=700>";
	echo "<tr>";
	echo "<td align=center><b> Rank </b></td>";
	echo "<td><b> Name </b></td><td><b> Surname </b></td>";
	echo "<td align=center><b> School </b></td><td align=center><b> Grade </b></td>";
	echo "<td align=center><b> Mark </b></td>";
	echo "</tr>";
	echo "<tr>";
	echo "<td align=center><b> Max </b></td>";
	echo "<td><b> Possible </b></td><td><b> Mark </b></td><td align=center><b> - </b></td><td align=center><b> - </b></td>";
	echo "<td align=center><b> 50 </b></td>";
	echo "</tr>";
	
	$rank = 0;
	
	for ($out = 1; $out < $num_results; $out++)
	{
			echo "<tr>";
			$rank++;
			echo "<td align=center> $rank </td>";
			echo "<td>$name[$out]</td><td>$surname[$out]</td><td>$school[$out]</td>";
			echo "<td align=center> $grade[$out] </td>";
			echo "<td align=center>$mark[$out]</td>";
			echo "</tr>";
	}

	echo "</table>";

}

function junior_problem_set_05()
{

?>

	<h2 align="center"> Junior Problem Set 5 - Ranking </h2>

<?

require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
	return false;

	$query = "select * from junior_problem_set_05";
	$result = mysql_query($query);
	$num_results = mysql_num_rows($result);

	$user[$num_results];
	$mark[$num_results];
	$name[$num_results];
	$surname[$num_results];
	$school[$num_results];
	$grade[$num_results];
	$number = 0;

	$solutions = mysql_fetch_row($result);
	if ($solutions[0] == 0)
	{
	
	//read everything out
	for ($i = 1; $i < $num_results; $i++)
	{
		$row = mysql_fetch_row($result);
		$user[$i] = $row[0];
		$total = 0;
		for ($j=1; $j<=10; $j++)
		{
			if ($row[$j] == $solutions[$j])
			{
				$total=$total+5;
			} else
			if ($row[$j] == NULL)
			{
				$total=$total+0;
			} else
			{
				$total--;
			}
			
		}
		$mark[$i] = $total;
		$number++;
	} 
	}

	//sort
	for ($x = 1; $x < $num_results; $x++)
	{
		for ($count = 1; $count < $num_results; $count++)
		{
			if ($mark[$count] < $mark[$count+1])
			{
				$temp_user = $user[$count];
				$temp_mark = $mark[$count];

				$user[$count] = $user[$count+1];
				$mark[$count] = $mark[$count+1];

				$user[$count+1] = $temp_user;
				$mark[$count+1] = $temp_mark;
			}
		}
	}

	//find top 20 details
	for ($count = 1; $count < $num_results; $count++)
	{

		if (!($conn = db_connect()))
		return false;

		$query = "select * from user where uid = '$user[$count]'";
		$result = mysql_query($query);
		if (!$result)
		return false;
		$pinfo = mysql_fetch_row($result);

		$name[$count] = $pinfo[6];
		$surname[$count] = $pinfo[7];
		$school[$count] = $pinfo[8];
		$grade[$count] = $pinfo[9];

	}

	//display top  20
	echo "<table align=center border=1 width=700>";
	echo "<tr>";
	echo "<td align=center><b> Rank </b></td>";
	echo "<td><b> Name </b></td><td><b> Surname </b></td>";
	echo "<td align=center><b> School </b></td><td align=center><b> Grade </b></td>";
	echo "<td align=center><b> Mark </b></td>";
	echo "</tr>";
	echo "<tr>";
	echo "<td align=center><b> Max </b></td>";
	echo "<td><b> Possible </b></td><td><b> Mark </b></td><td align=center><b> - </b></td><td align=center><b> - </b></td>";
	echo "<td align=center><b> 50 </b></td>";
	echo "</tr>";
	
	$rank = 0;
	
	for ($out = 1; $out < $num_results; $out++)
	{
			echo "<tr>";
			$rank++;
			echo "<td align=center> $rank </td>";
			echo "<td>$name[$out]</td><td>$surname[$out]</td><td>$school[$out]</td>";
			echo "<td align=center> $grade[$out] </td>";
			echo "<td align=center>$mark[$out]</td>";
			echo "</tr>";
	}

	echo "</table>";

}

function junior_rankings()
{

?>

	<h2 align="center"> Junior Rankings </h2>

<p> Under construction</p>

<?
					

}

function senior_questions()
{

?>

	<h2 align="center"> Senior Problem Sets </h2>

	<p>
		<a href=documents/Senior_Problem_Set_01.pdf>Problem Set 1</a><br>	
		<a href=documents/Senior_Problem_Set_02.pdf>Problem Set 2</a><br>	
		<a href=documents/Senior_Problem_Set_03.pdf>Problem Set 3</a><br>	
		<a href=documents/Senior_Problem_Set_04.pdf>Problem Set 4</a><br>	
	</p>
	
<?

}

function senior_submit()
{

?>

	<h2 align="center"> Senior Submit Solutions </h2>

<p>
Please enter the problem set number into the indicated box or otherwise it will not submit correctly. After you submit there should be a message "Successfully Submitted". If you do not get this message you will have to retry.
</p>

<form action=internet_done.php method=post>
	<table align="center" width="300">
		<tr>
		    <td align="center" colspan=5>
	    	    Problem Set: <input type="text" name="paper" size="2" maxlength="2"><br>
		    </td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 1</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q1" value="a"></input></td>
			<td> B <input type="radio" name="Q1" value="b"></input></td>
			<td> C <input type="radio" name="Q1" value="c"></input></td>
			<td> D <input type="radio" name="Q1" value="d"></input></td>
			<td> E <input type="radio" name="Q1" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 2</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q2" value="a"></input></td>
			<td> B <input type="radio" name="Q2" value="b"></input></td>
			<td> C <input type="radio" name="Q2" value="c"></input></td>
			<td> D <input type="radio" name="Q2" value="d"></input></td>
			<td> E <input type="radio" name="Q2" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 3</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q3" value="a"></input></td>
			<td> B <input type="radio" name="Q3" value="b"></input></td>
			<td> C <input type="radio" name="Q3" value="c"></input></td>
			<td> D <input type="radio" name="Q3" value="d"></input></td>
			<td> E <input type="radio" name="Q3" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 4</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q4" value="a"></input></td>
			<td> B <input type="radio" name="Q4" value="b"></input></td>
			<td> C <input type="radio" name="Q4" value="c"></input></td>
			<td> D <input type="radio" name="Q4" value="d"></input></td>
			<td> E <input type="radio" name="Q4" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 5</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q5" value="a"></input></td>
			<td> B <input type="radio" name="Q5" value="b"></input></td>
			<td> C <input type="radio" name="Q5" value="c"></input></td>
			<td> D <input type="radio" name="Q5" value="d"></input></td>
			<td> E <input type="radio" name="Q5" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 6</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q6" value="a"></input></td>
			<td> B <input type="radio" name="Q6" value="b"></input></td>
			<td> C <input type="radio" name="Q6" value="c"></input></td>
			<td> D <input type="radio" name="Q6" value="d"></input></td>
			<td> E <input type="radio" name="Q6" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 7</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q7" value="a"></input></td>
			<td> B <input type="radio" name="Q7" value="b"></input></td>
			<td> C <input type="radio" name="Q7" value="c"></input></td>
			<td> D <input type="radio" name="Q7" value="d"></input></td>
			<td> E <input type="radio" name="Q7" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 8</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q8" value="a"></input></td>
			<td> B <input type="radio" name="Q8" value="b"></input></td>
			<td> C <input type="radio" name="Q8" value="c"></input></td>
			<td> D <input type="radio" name="Q8" value="d"></input></td>
			<td> E <input type="radio" name="Q8" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 9</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q9" value="a"></input></td>
			<td> B <input type="radio" name="Q9" value="b"></input></td>
			<td> C <input type="radio" name="Q9" value="c"></input></td>
			<td> D <input type="radio" name="Q9" value="d"></input></td>
			<td> E <input type="radio" name="Q9" value="e"></input></td>
		</tr>
		<tr>
			<td align="center" colspan=5><b>Question 10</b></td>
		</tr>
		<tr>
			<td> A <input type="radio" name="Q10" value="a"></input></td>
			<td> B <input type="radio" name="Q10" value="b"></input></td>
			<td> C <input type="radio" name="Q10" value="c"></input></td>
			<td> D <input type="radio" name="Q10" value="d"></input></td>
			<td> E <input type="radio" name="Q10" value="e"></input></td>
		</tr>

	</table>
	<table align=center><tr><td>
	<input type=hidden name=level value= 12>
	<input type=submit value= Submit>
	</td></tr></table>
	</form>
	
	
<?

}

function senior_problem_set_01()
{

?>

	<h2 align="center"> Senior Problem Set 1 - Ranking </h2>

<?

require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
	return false;

	$query = "select * from senior_problem_set_01";
	$result = mysql_query($query);
	$num_results = mysql_num_rows($result);

	$user[$num_results];
	$mark[$num_results];
	$name[$num_results];
	$surname[$num_results];
	$school[$num_results];
	$grade[$num_results];
	$number = 0;

	$solutions = mysql_fetch_row($result);
	if ($solutions[0] == 0)
	{
	
	//read everything out
	for ($i = 1; $i < $num_results; $i++)
	{
		$row = mysql_fetch_row($result);
		$user[$i] = $row[0];
		$total = 0;
		for ($j=1; $j<=10; $j++)
		{
			if ($row[$j] == $solutions[$j])
			{
				$total=$total+5;
			} else
			if ($row[$j] == NULL)
			{
				$total=$total+0;
			} else
			{
				$total--;
			}
			
		}
		$mark[$i] = $total;
		$number++;
	} 
	}

	//sort
	for ($x = 1; $x < $num_results; $x++)
	{
		for ($count = 1; $count < $num_results; $count++)
		{
			if ($mark[$count] < $mark[$count+1])
			{
				$temp_user = $user[$count];
				$temp_mark = $mark[$count];

				$user[$count] = $user[$count+1];
				$mark[$count] = $mark[$count+1];

				$user[$count+1] = $temp_user;
				$mark[$count+1] = $temp_mark;
			}
		}
	}

	//find top 20 details
	for ($count = 1; $count < $num_results; $count++)
	{

		if (!($conn = db_connect()))
		return false;

		$query = "select * from user where uid = '$user[$count]'";
		$result = mysql_query($query);
		if (!$result)
		return false;
		$pinfo = mysql_fetch_row($result);

		$name[$count] = $pinfo[6];
		$surname[$count] = $pinfo[7];
		$school[$count] = $pinfo[8];
		$grade[$count] = $pinfo[9];

	}

	//display top  20
	echo "<table align=center border=1 width=700>";
	echo "<tr>";
	echo "<td align=center><b> Rank </b></td>";
	echo "<td><b> Name </b></td><td><b> Surname </b></td>";
	echo "<td align=center><b> School </b></td><td align=center><b> Grade </b></td>";
	echo "<td align=center><b> Mark </b></td>";
	echo "</tr>";
	echo "<tr>";
	echo "<td align=center><b> Max </b></td>";
	echo "<td><b> Possible </b></td><td><b> Mark </b></td><td align=center><b> - </b></td><td align=center><b> - </b></td>";
	echo "<td align=center><b> 50 </b></td>";
	echo "</tr>";
	
	$rank = 0;
	
	for ($out = 1; $out < $num_results; $out++)
	{
			echo "<tr>";
			$rank++;
			echo "<td align=center> $rank </td>";
			echo "<td>$name[$out]</td><td>$surname[$out]</td><td>$school[$out]</td>";
			echo "<td align=center> $grade[$out] </td>";
			echo "<td align=center>$mark[$out]</td>";
			echo "</tr>";
	}

	echo "</table>";

}

function senior_problem_set_02()
{

?>

	<h2 align="center"> Senior Problem Set 2 - Ranking </h2>

<?

require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
	return false;

	$query = "select * from senior_problem_set_02";
	$result = mysql_query($query);
	$num_results = mysql_num_rows($result);

	$user[$num_results];
	$mark[$num_results];
	$name[$num_results];
	$surname[$num_results];
	$school[$num_results];
	$grade[$num_results];
	$number = 0;

	$solutions = mysql_fetch_row($result);
	if ($solutions[0] == 0)
	{
	
	//read everything out
	for ($i = 1; $i < $num_results; $i++)
	{
		$row = mysql_fetch_row($result);
		$user[$i] = $row[0];
		$total = 0;
		for ($j=1; $j<=10; $j++)
		{
			if ($row[$j] == $solutions[$j])
			{
				$total=$total+5;
			} else
			if ($row[$j] == NULL)
			{
				$total=$total+0;
			} else
			{
				$total--;
			}
			
		}
		$mark[$i] = $total;
		$number++;
	} 
	}

	//sort
	for ($x = 1; $x < $num_results; $x++)
	{
		for ($count = 1; $count < $num_results; $count++)
		{
			if ($mark[$count] < $mark[$count+1])
			{
				$temp_user = $user[$count];
				$temp_mark = $mark[$count];

				$user[$count] = $user[$count+1];
				$mark[$count] = $mark[$count+1];

				$user[$count+1] = $temp_user;
				$mark[$count+1] = $temp_mark;
			}
		}
	}

	//find top 20 details
	for ($count = 1; $count < $num_results; $count++)
	{

		if (!($conn = db_connect()))
		return false;

		$query = "select * from user where uid = '$user[$count]'";
		$result = mysql_query($query);
		if (!$result)
		return false;
		$pinfo = mysql_fetch_row($result);

		$name[$count] = $pinfo[6];
		$surname[$count] = $pinfo[7];
		$school[$count] = $pinfo[8];
		$grade[$count] = $pinfo[9];

	}

	//display top  20
	echo "<table align=center border=1 width=700>";
	echo "<tr>";
	echo "<td align=center><b> Rank </b></td>";
	echo "<td><b> Name </b></td><td><b> Surname </b></td>";
	echo "<td align=center><b> School </b></td><td align=center><b> Grade </b></td>";
	echo "<td align=center><b> Mark </b></td>";
	echo "</tr>";
	echo "<tr>";
	echo "<td align=center><b> Max </b></td>";
	echo "<td><b> Possible </b></td><td><b> Mark </b></td><td align=center><b> - </b></td><td align=center><b> - </b></td>";
	echo "<td align=center><b> 50 </b></td>";
	echo "</tr>";
	
	$rank = 0;
	
	for ($out = 1; $out < $num_results; $out++)
	{
			echo "<tr>";
			$rank++;
			echo "<td align=center> $rank </td>";
			echo "<td>$name[$out]</td><td>$surname[$out]</td><td>$school[$out]</td>";
			echo "<td align=center> $grade[$out] </td>";
			echo "<td align=center>$mark[$out]</td>";
			echo "</tr>";
	}

	echo "</table>";

}

function senior_problem_set_03()
{

?>

	<h2 align="center"> Senior Problem Set 3 - Ranking </h2>

<?

require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
	return false;

	$query = "select * from senior_problem_set_03";
	$result = mysql_query($query);
	$num_results = mysql_num_rows($result);

	$user[$num_results];
	$mark[$num_results];
	$name[$num_results];
	$surname[$num_results];
	$school[$num_results];
	$grade[$num_results];
	$number = 0;

	$solutions = mysql_fetch_row($result);
	if ($solutions[0] == 0)
	{
	
	//read everything out
	for ($i = 1; $i < $num_results; $i++)
	{
		$row = mysql_fetch_row($result);
		$user[$i] = $row[0];
		$total = 0;
		for ($j=1; $j<=10; $j++)
		{
			if ($row[$j] == $solutions[$j])
			{
				$total=$total+5;
			} else
			if ($row[$j] == NULL)
			{
				$total=$total+0;
			} else
			{
				$total--;
			}
			
		}
		$mark[$i] = $total;
		$number++;
	} 
	}

	//sort
	for ($x = 1; $x < $num_results; $x++)
	{
		for ($count = 1; $count < $num_results; $count++)
		{
			if ($mark[$count] < $mark[$count+1])
			{
				$temp_user = $user[$count];
				$temp_mark = $mark[$count];

				$user[$count] = $user[$count+1];
				$mark[$count] = $mark[$count+1];

				$user[$count+1] = $temp_user;
				$mark[$count+1] = $temp_mark;
			}
		}
	}

	//find top 20 details
	for ($count = 1; $count < $num_results; $count++)
	{

		if (!($conn = db_connect()))
		return false;

		$query = "select * from user where uid = '$user[$count]'";
		$result = mysql_query($query);
		if (!$result)
		return false;
		$pinfo = mysql_fetch_row($result);

		$name[$count] = $pinfo[6];
		$surname[$count] = $pinfo[7];
		$school[$count] = $pinfo[8];
		$grade[$count] = $pinfo[9];

	}

	//display top  20
	echo "<table align=center border=1 width=700>";
	echo "<tr>";
	echo "<td align=center><b> Rank </b></td>";
	echo "<td><b> Name </b></td><td><b> Surname </b></td>";
	echo "<td align=center><b> School </b></td><td align=center><b> Grade </b></td>";
	echo "<td align=center><b> Mark </b></td>";
	echo "</tr>";
	echo "<tr>";
	echo "<td align=center><b> Max </b></td>";
	echo "<td><b> Possible </b></td><td><b> Mark </b></td><td align=center><b> - </b></td><td align=center><b> - </b></td>";
	echo "<td align=center><b> 50 </b></td>";
	echo "</tr>";
	
	$rank = 0;
	
	for ($out = 1; $out < $num_results; $out++)
	{
			echo "<tr>";
			$rank++;
			echo "<td align=center> $rank </td>";
			echo "<td>$name[$out]</td><td>$surname[$out]</td><td>$school[$out]</td>";
			echo "<td align=center> $grade[$out] </td>";
			echo "<td align=center>$mark[$out]</td>";
			echo "</tr>";
	}

	echo "</table>";

}

function senior_problem_set_04()
{

?>

	<h2 align="center"> Senior Problem Set 4 - Ranking </h2>

<?

require_once("db_fns.php");

	$uid = $_SESSION['valid_user_id'];
	if (!($conn = db_connect()))
	return false;

	$query = "select * from senior_problem_set_04";
	$result = mysql_query($query);
	$num_results = mysql_num_rows($result);

	$user[$num_results];
	$mark[$num_results];
	$name[$num_results];
	$surname[$num_results];
	$school[$num_results];
	$grade[$num_results];
	$number = 0;

	$solutions = mysql_fetch_row($result);
	if ($solutions[0] == 0)
	{
	
	//read everything out
	for ($i = 1; $i < $num_results; $i++)
	{
		$row = mysql_fetch_row($result);
		$user[$i] = $row[0];
		$total = 0;
		for ($j=1; $j<=10; $j++)
		{
			if ($row[$j] == $solutions[$j])
			{
				$total=$total+5;
			} else
			if ($row[$j] == NULL)
			{
				$total=$total+0;
			} else
			{
				$total--;
			}
			
		}
		$mark[$i] = $total;
		$number++;
	} 
	}

	//sort
	for ($x = 1; $x < $num_results; $x++)
	{
		for ($count = 1; $count < $num_results; $count++)
		{
			if ($mark[$count] < $mark[$count+1])
			{
				$temp_user = $user[$count];
				$temp_mark = $mark[$count];

				$user[$count] = $user[$count+1];
				$mark[$count] = $mark[$count+1];

				$user[$count+1] = $temp_user;
				$mark[$count+1] = $temp_mark;
			}
		}
	}

	//find top 20 details
	for ($count = 1; $count < $num_results; $count++)
	{

		if (!($conn = db_connect()))
		return false;

		$query = "select * from user where uid = '$user[$count]'";
		$result = mysql_query($query);
		if (!$result)
		return false;
		$pinfo = mysql_fetch_row($result);

		$name[$count] = $pinfo[6];
		$surname[$count] = $pinfo[7];
		$school[$count] = $pinfo[8];
		$grade[$count] = $pinfo[9];

	}

	//display top  20
	echo "<table align=center border=1 width=700>";
	echo "<tr>";
	echo "<td align=center><b> Rank </b></td>";
	echo "<td><b> Name </b></td><td><b> Surname </b></td>";
	echo "<td align=center><b> School </b></td><td align=center><b> Grade </b></td>";
	echo "<td align=center><b> Mark </b></td>";
	echo "</tr>";
	echo "<tr>";
	echo "<td align=center><b> Max </b></td>";
	echo "<td><b> Possible </b></td><td><b> Mark </b></td><td align=center><b> - </b></td><td align=center><b> - </b></td>";
	echo "<td align=center><b> 50 </b></td>";
	echo "</tr>";
	
	$rank = 0;
	
	for ($out = 1; $out < $num_results; $out++)
	{
			echo "<tr>";
			$rank++;
			echo "<td align=center> $rank </td>";
			echo "<td>$name[$out]</td><td>$surname[$out]</td><td>$school[$out]</td>";
			echo "<td align=center> $grade[$out] </td>";
			echo "<td align=center>$mark[$out]</td>";
			echo "</tr>";
	}

	echo "</table>";

}

function senior_rankings()
{

?>

	<h2 align="center"> Senior Rankings </h2>

<p> Under construction</p>

	
<?

}


function password()
{

?>


	<h2 align="center"> Change Password </h2>

<?

 	display_password_form();

}

?>
