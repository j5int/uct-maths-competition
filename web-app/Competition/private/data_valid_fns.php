<?

function filled_out($form_vars)
{
  // test that each variable has a value
  foreach ($form_vars as $key => $value)
  {
     if (!isset($key) || ($value == "")) 
        return false;
  } 
  return true;
}

function filled_out2($form_vars)
{
   // test that each variable has a value
  foreach ($form_vars as $key => $value)
  {
     if (!isset($key) || ($value == ""))
     {
	if (strcmp($key,"new_passwd")!=0 && strcmp($key,"new_passwd2")!=0 && strcmp($key,"old_passwd")!=0)
        return false;
     }
  }
  return true;

}
function valid_email($form_vars)
{
  // check an email address is possibly valid
  foreach ($form_vars as $key => $value)
  {
	if (strcmp($key,"email")==0)
	{
		if (ereg("^[a-zA-Z0-9_]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$", $value))
		{
			return true;
		} else
		{
			return false;
		}
		
	}
  }
}

?>
