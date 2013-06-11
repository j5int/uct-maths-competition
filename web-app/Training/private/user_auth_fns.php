<?

require_once("db_fns.php");

function register($username, $email, $password)
// register new person with db
// return true or error message
{
 // connect to db
  $conn = db_connect();
  if (!$conn)
    return "Could not connect to database server - please try later.";

  // check if username is unique 
  $result = mysql_query("select * from user where username='$username'"); 
  if (!$result)
     return "Could not execute query";
  if (mysql_num_rows($result)>0) 
     return "That username is taken - go back and choose another one.";

  // if ok, put in db
  $result = mysql_query("insert into user values ('$username', password('$password'), '$email')");
  if (!$result)
    return "Could not register you  in database - please try again later.";

  return true;
}
 
function login($username, $password)
// check username and password with db
// if yes, return true
// else return false
{
  // connect to db
  $conn = db_connect();
  if (!$conn)
    return 0;

  // check if username is unique
  $result = mysql_query("select * from user where username='$username' and password = password('$password')");
  if (!$result)
     return 0;

  $today = date('Y-m-d');
  if (mysql_num_rows($result)>0)
  {
	$result2 = mysql_query("update user set counter = counter+1, last='$today' where username='$username' and password = password('$password')");
	$result3 = mysql_query("select uid from user where username='$username' and password = password('$password')");
	$result4 = mysql_result($result3, 0);
     return $result4;
  }
  else 
     return 0;
}

function set_user_types()
{
	 // connect to db
	global $valid_user_id;
	global $user_type_A;
	global $user_type_B;
	global $user_type_C;
	global $user_type_teacher;
	global $user_type_admin;
	
	$conn = db_connect();
	if (!$conn)
    return 0;

	$query = $_SESSION['valid_user_id'];
	$result = mysql_query("select utype from user where uid='$query'");
	$result = mysql_result($result, 0);
	
	if ($result >= 16)
	{
		$_SESSION['user_type_admin'] = 1;
		$result = $result - 16;
	} else
	{
		$_SESSION['user_type_admin'] = 0;
	}
	if ($result >= 8)
	{
		$_SESSION['user_type_teacher'] = 1;
		$result = $result - 8;
	} else
	{
		$_SESSION['user_type_teacher'] = 0;
	}

	if ($result >= 4)
	{
		$_SESSION['user_type_C'] = 1;
		$result = $result - 4;
	} else
	{
		$_SESSION['user_type_C'] = 0;
	}

	if ($result >= 2)
	{
		$_SESSION['user_type_B'] = 1;
		$result = $result - 2;
	} else
	{
		$_SESSION['user_type_B'] = 0;
	}

	if ($result >= 1)
	{
		$_SESSION['user_type_A'] = 1;
		$result = $result - 1;
	} else
	{
		$_SESSION['user_type_A'] = 0;
	}
}

function check_valid_user()									// see if somebody is logged in and notify them if not
{
	global $valid_user;
	if (isset($_SESSION['valid_user']))						//check if logged in
	{
		do_login_message();									//if logged in show logged in details
	} else
	{
		do_wrong_login_information();						//if not display that they are not logged in 
		do_html_footer();
		exit;
	}  
}

function change_password($username, $old_password, $new_password)
// change password for username/old_password to new_password
// return true or false
{
  // if the old password is right 
  // change their password to new_password and return true
  // else return false
  if (login($username, $old_password))
  {
    if (!($conn = db_connect()))
      return false;
    $result = mysql_query("update user
                            set password = password('$new_password')
                            where username = '$username'");
    if (!$result)
      return false;  // not changed
    else
      return true;  // changed successfully
  }
  else
    return false; // old password was wrong
}

function reset_password($username)
// set password for username to a random value
// return the new password or false on failure
{ 
  // get a random dictionary word b/w 6 and 13 chars in length
    // add a number  between 0 and 999 to it
  // to make it a slightly better password

  $i = 0;
  srand ((double) microtime() * 1000000);
  $new_password = "";
  while ($i < 7)
  {
     $rand_number = rand(0, 35);
     if ($rand_number < 10)
     {  
     $new_password .= $rand_number;
     } else
     {
	$new_password .= chr($rand_number-10+65);
     }
  }
  // set user's password to this in database or return false
  if (!($conn = db_connect()))
      return false;
  $result = mysql_query("update user
                          set password = password('$new_password')
                          where username = '$username'");
  if (!$result)
    return false;  // not changed
  else
    return $new_password;  // changed successfully  
}

function notify_password($username, $password)
// notify the user that their password has been changed
{
    if (!($conn = db_connect()))
      return false;
    $result = mysql_query("select email from user
                            where username='$username'");
    if (!$result)
      return false;  // not changed
    else if (mysql_num_rows($result)==0)
      return false; // username not in db
    else
    {
      $email = mysql_result($result, 0, "email");
      $from = "From: support@phpmathscircle \r\n";
      $mesg = "Your MathsCircle password has been changed to $password \r\n"
              ."Please change it next time you log in. \r\n";
      if (mail($email, "MathsCircle login information", $mesg, $from))
        return true;      
      else
        return false;     
    }
} 

?>
