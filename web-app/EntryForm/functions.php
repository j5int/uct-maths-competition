<?php

$page_list = array (
	1 => "index.php",
	2 => "grade8.php",
	3 => "grade9.php",
	4 => "grade10.php",
	5 => "grade11.php",
	6 => "grade12.php",
	7 => "pairs.php",
	8 => "teachers.php"
);

$total_pages = count($page_list);
$page_list[9] = "review.php";
$page_list[10] = "sent.php";

$page_numbers = array_flip($page_list);
$current_page_name = basename($_SERVER[PHP_SELF]);
$current_page_number = $page_numbers[$current_page_name];
$short_current_page_name = str_replace(".php", "", $current_page_name);

$grade_number = str_replace(".php","",str_replace("grade","",$current_page_name));
 
// for any POSTed values, put into array
foreach ($_POST as $post => $post_val) {
	$posted[$post] = $post_val;
}

#print_r($posted);

function carry_through($array,$short_current_page_name) {

	if (isset($array)) {

	switch($short_current_page_name) {
		
		case "index":
		$ditch = array("name_of_school" => "", "address1" => "", "address2" => "", "tel" => "", "fax" => "", "postal_code" => "", "email" => "");
		break;	
		
		case "grade8":
		$ditch = array("grade8" => "", "next" => "");
		break;
		
		case "grade9":
		$ditch = array("grade9" => "");
		break;
		
		case "grade10":
		$ditch = array("grade10" => "");
		break;
		
		case "grade11":
		$ditch = array("grade11" => "");
		break;
		
		case "grade12":
		$ditch = array("grade12" => "");
		break;
		
		case "pairs":
		$ditch = array("pairs" => "");
		break;
		
		case "teachers":
		$ditch = array ("invigilator1" => "", "invigilator1number" => "", "invigilator1email" => "",
						"invigilator2" => "", "invigilator2number" => "", "invigilator2email" => "", 
						"invigilator3" => "", "invigilator3number" => "", "invigilator3email" => "", 
						"invigilator4" => "", "invigilator4number" => "", "invigilator4email" => "", 
						"invigilator5" => "", "invigilator5number" => "", "invigilator5email" => "", 
						"responsible_teacher_name" => "", "responsible_teacher_tel" => "", "responsible_teacher_fax" => "");
		break;
	
		
	}
	
	$whatsleft = array_diff_key($array, $ditch);
	
		foreach ($whatsleft as $id => $value) {
			if(is_array($value)) {
				foreach ($value as $slot => $fields) {
					foreach ($fields as $fieldname => $fieldvalue) {
						if ( $fieldvalue != "") {
							echo '<input type="hidden" name="' . $id . '[' . $slot . '][' . $fieldname . ']" id="' . $id . $slot . $fieldname . '" value = "' . stripslashes($fieldvalue) .'" />
';
						}
					}
				}
			} 
			else {
				if ($value != "") { ?>
<input type="hidden" name="<?php echo $id; ?>" id="<?php echo $id; ?>" value="<?php echo stripslashes($value); ?>" />
<?php
				}
			}
		}
	
	}
	
}

function school_submitted($name_of_school) {
	$all_submitted = file_get_contents('submitted' . date('Y') . '.txt');
	$school_pos = strpos($all_submitted, $name_of_school);
return $school_pos;
}

function school_reviewed($name_of_school) {
	$all_submitted = file_get_contents('reviewed' . date('Y') . '.txt');
	$school_pos = strpos($all_submitted, $name_of_school);

	if(is_numeric($school_pos))
	{
		return true;
	}
	else
	{
		return false;
	}
}

?>
