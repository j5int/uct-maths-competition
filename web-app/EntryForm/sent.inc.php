<?php if (isset($_POST['next'])) { ?>

<?php  

include("index.inc.php");



// wrapper table
$page .= '<table>
	<tr>
		<td>INDIVIDUALS<br />INDIVIDUE</td>
		<td></td>
		<td>SURNAME<br />VAN</td>
		<td>FIRST NAME<br />VOORNAAM</td>
		<td>M/F<br />M/V</td>
		<td>E/A</td>
	</tr>';

for ($k = 8; $k <=12; $k++) {
$grade_number = $k;

	if(count($posted["grade" . $k]) > 0) {
		$page .= '<tr class="grade">
		<td>Grade ' . $k . '<br />Graad ' . $k . '</td>
		<td colspan="5">';
		include("grade.inc.php");
		$page .= '</td>
		</tr>';
	}

}

$page .= '</table>';

include("pairs.inc.php");
include("teachers.inc.php");

#print_r($posted);

$csv_header = 'SCHOOL:,NAME,GRADE,VENUE,Inv/Reg,Phone(h),PHONE(W),FAX,FAX(W),E-MAIL ADDRESS,Responsible
';

$csv_content = '';

$csv_content .= $posted['name_of_school'] . "," . $posted['invigilator1firstname'] . " " . $posted['invigilator1surname'] . ",,,," . $posted['invigilator1number'] .",,,," . $posted['invigilator1email'] . "," . $posted['responsible_teacher_name'] . $posted['responsible_teacher_tel'] . "
";

for ($invigilator = 2; $invigilator <= 7; $invigilator++)
{
	if (isset($posted['invigilator' . $invigilator . 'firstname']))
	{
		$csv_content .= $posted['name_of_school'] . "," . $posted['invigilator' . $invigilator . 'firstname'] . " " . $posted['invigilator' . $invigilator . 'surname'] . ",,,," . $posted['invigilator' . $invigilator . 'number'] .",,,," . $posted['invigilator' . $invigilator . 'email'] . "," . $posted['responsible_teacher_name'] . " " . $posted['responsible_teacher_tel'] . "
";
	}
}

#print_r($csv_content);

$msg = str_replace('&#039',"'",$page); 

//$msg = str_replace('<table>','<table width="100%">',$msg); 

$jsforimporting = '';

#$posted['name_of_school'] = str_replace("'","&#039",stripslashes($posted['name_of_school']));
#$jsforimporting .= print_r($schools,true);


$jsforimporting .= "
var db_location = new String(window.location);
db_location = db_location.replace('file:///', '');
db_location = db_location.replace(/%20/g, ' ');
db_location = db_location.replace(/\//g, '\\\');
db_location = db_location.replace('import.html', 'db1.mdb');

var myDB = new ACCESSdb(db_location, {showErrors:true});
";

// $jsforimporting .= '
// var SQLdc = "SELECT Schools WHERE Entered = -1 AND Key = \'' . $schools[str_replace("'","&#039",stripslashes($posted['name_of_school']))]["Key"] . '\'";
// var rsdc = myDB.query(SQLdc);

// if (rsdc == false) {
// ';

$jsforimporting .= '
var SQL = "UPDATE Schools SET Entered = -1 WHERE Key = \'' . $schools[str_replace("'","&#039",stripslashes($posted['name_of_school']))]["Key"] . '\'";
var rs = myDB.query(SQL);
';

for ($grade=8;$grade<=12;$grade++) 
{
	if (count($posted['grade' . $grade])>0) 
	{
			foreach ($posted['grade' . $grade] as $slot => $student) 
			{
				if (trim($student['firstname']) != '')
				{
				$Key= $schools[str_replace("'","&#039",stripslashes($posted['name_of_school']))]["Key"] . str_pad($grade, 2, "0", STR_PAD_LEFT) . str_pad($slot, 2, "0", STR_PAD_LEFT);

				$quotes = '"';
			/*
				$jsforimporting .= "
				var SQL" . $Key . " = " . $quotes .  "INSERT INTO Students VALUES ('" . $student['firstname']  . "', '" . $student['surname'] . "', '" . $Key . "', '" . str_replace("'","&#039",stripslashes($posted['name_of_school'])) . "', '0', '0', '" . $grade . "', '" . strtolower(substr($student['gender'], 0, 1)) . "', '" . strtolower(substr($student['language'], 0, 1)) . "', '')" . $quotes .  ";
				";
			*/

// added 2012-01-23

$gender = substr(strtolower($student['gender']),0,1);

if ($gender != 'v' && $gender != 'f' &&  $gender != 'm') {
	$gender = 'm';
}

$language = substr(strtolower($student['language']),0,1);

if ($language != 'a' && $language != 'e') {
	$language = 'e';
}


					$jsforimporting .= "
					var SQL" . $Key . " = " . $quotes .  "INSERT INTO Students VALUES ('" . str_replace("'","&#039",stripslashes($student['firstname']))  . "', '" . str_replace("'","&#039",stripslashes($student['surname'])) . "', '" . $Key . "', '" . str_replace("'","&#039",stripslashes($posted['name_of_school'])) . "', '0', '0', '" . $grade . "', '" . $gender . "', '" . $language . "', '')" . $quotes .  ";
					";

							$jsforimporting .= "var rs" . $Key . " = myDB.query(SQL" . $Key . ");
						";

				}


			}
	}

	if ($posted['pairs']['grade' . $grade]['number'] > 0)
	{
		$pair_ref = 6;
		// $StartOfPairKey= $schools[$posted['name_of_school']]["Key"] . str_pad($grade, 2, "0", STR_PAD_LEFT);
		$StartOfPairKey= $schools[str_replace("'","&#039",stripslashes($posted['name_of_school']))]["Key"] . str_pad($grade, 2, "0", STR_PAD_LEFT);

		for ($pairs_to_add = 1; $pairs_to_add <= $posted['pairs']['grade' . $grade]['number']; $pairs_to_add++)
//		for ($pairs_to_add = 1; $pairs_to_add <= 2 * $posted['pairs']['grade' . $grade]['number']; $pairs_to_add++)
		{
			$jsforimporting .= "
	var SQL" . $StartOfPairKey . str_pad($pair_ref, 2, "0", STR_PAD_LEFT) . " = " . $quotes .  "INSERT INTO Students VALUES ('', '', '" . $StartOfPairKey . str_pad($pair_ref, 2, "0", STR_PAD_LEFT) . "', '" . str_replace("'","&#039",stripslashes($posted['name_of_school'])) . "', '0', '0', '" . $grade . "', 'u', 'e', '')" . $quotes .  ";";

			$jsforimporting .= "
	var rs" . $StartOfPairKey . str_pad($pair_ref, 2, "0", STR_PAD_LEFT) . " = myDB.query(SQL" . $StartOfPairKey . str_pad($pair_ref, 2, "0", STR_PAD_LEFT) . ");
			";
			
//			double up for pairs

			$jsforimporting .= "
	var SQL" . $StartOfPairKey . str_pad($pair_ref, 2, "0", STR_PAD_LEFT) . " = " . $quotes .  "INSERT INTO Students VALUES ('', '', '" . $StartOfPairKey . str_pad($pair_ref, 2, "0", STR_PAD_LEFT) . "', '" . str_replace("'","&#039",stripslashes($posted['name_of_school'])) . "', '0', '0', '" . $grade . "', 'u', 'e', '')" . $quotes .  ";";

			$jsforimporting .= "
	var rs" . $StartOfPairKey . str_pad($pair_ref, 2, "0", STR_PAD_LEFT) . " = myDB.query(SQL" . $StartOfPairKey . str_pad($pair_ref, 2, "0", STR_PAD_LEFT) . ");
			";

			$pair_ref++;
		}
	}

}

// // if (rsdc) {
// $jsforimporting .= '
// }
// ';

// add js for school

$school_nice_name = $posted['name_of_school'];
#print_r($posted);
$remove = array ('\'' => '', '/' => '', ' ' => '-', '&#039' => "'", '.' => '', "'" => '');
foreach ($remove as $find => $replace) {
	$school_nice_name = str_replace($find, $replace, $school_nice_name);
}

$school_nice_name = stripslashes($school_nice_name);

$school_nice_name = $school_nice_name . date('Y') . '.txt';

$sqlhandle = fopen($school_nice_name,'w');
#$sqlhandle = fopen($school_nice_name,'a');
fwrite($sqlhandle, $jsforimporting);
fclose($sqlhandle);

$jsforimporting_url = 'http://' . str_replace('sent.php', '', $_SERVER["HTTP_HOST"] . $_SERVER["REQUEST_URI"]) . $school_nice_name;



if (!file_exists('invigilator_list' . date('Y') . '.csv'))
{
	$csv_content = $csv_header . $csv_content;
}

$csvhandle = fopen('invigilator_list' . date('Y') . '.csv','a');
fwrite($csvhandle, $csv_content);
fclose($csvhandle);

$csv_url = 'http://' . str_replace('sent.php', '', $_SERVER["HTTP_HOST"] . $_SERVER["REQUEST_URI"]) . 'invigilator_list' . date('Y') . '.csv';



$msg .= '<br /><br /><br />File for importing: <a href="' . $jsforimporting_url . '">' .$jsforimporting_url . '</a>';

$msg .= '<br /><br /><br />CSV file of Invigilators: <a href="' . $csv_url . '">' .$csv_url . '</a>';

if ($_SERVER["HTTP_HOST"] == "localhost") {
#if (true) {

echo $msg;

} // end if lolcat host 

else {
#$to ='Cynthia.Sher@uct.ac.za';
#$to ='Cynthia.Sher@uctmathcomp.co.za';
$to ='uctmathscomp@gmail.com';
// $to ='steve@naga.co.za';
// $to ='steve.at.naga@gmail.com';
$subject = date('Y') . ' UCT Mathematics Competition Form data - ' .  str_replace('&#039',"'",$posted['name_of_school']);
$message = $msg;

$headers = 
'MIME-Version: 1.0' . "\r\n" .
'Content-type: text/html; charset=iso-8859-1' . "\r\n" .
'From: UCT Mathematics Competition Form <uctmathcomp@naga.co.za>' . "\r\n" .
	'Reply-To: uctmathcomp@naga.co.za' . "\r\n" .

	'Cc: Cynthia.Sher@uct.ac.za' . "\r\n";
	// 'Cc: ' . $posted["email"] .  "\r\n";
	'Bcc: Cynthia.Sher@naga.co.za,steve@naga.co.za,bezi@mypostbox.co.za' . "\r\n";
	'X-Mailer: PHP/' . phpversion();

if(mail($to, $subject, $message, $headers)) { 
echo '
<h2>Your email was sent.</h2>
<br /><br />
<a href="javascript: history.go(-1)" id="back">&laquo; Return to Review page</a>.';

// echo $message;
// echo $jsforimporting;
}
else { echo "<h2>Error sending email. Please reload the page to try again.</h2>"; }


} // end else not lolcat host

// updated submitted list

$filename = 'submitted' . date('Y') . '.txt';
$content = str_replace('&#039',"'",$posted['name_of_school']) . "\n";
// $content = str_replace('&#039;',"'",$posted['name_of_school']) . "\n";
// $content = str_replace('&#039',"\'",$posted['name_of_school']) . "\n";
// $content = str_replace('&#039',"' + \"'\" + '",$posted['name_of_school']) . "\n";

$handle = fopen($filename,'a');
fwrite($handle, $content);
fclose($handle);

} // end if $_POST['next'] isset
?>
