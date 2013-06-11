<?php
$page .= '<div id="continue">';

if ($current_page_name != "index.php" && $current_page_name != "sent.php") {
	$page .= '<input type="submit" id="back" value="&laquo; Back to previous page" />';
}
	
if ($current_page_name == "review.php") {
	$page .= '<input type="submit" id="print_button" value="Print this page" />';
}
	
if ($current_page_name != "sent.php") {
		$page .= '<input type="submit" name="next" id="next" value="';
		if ($current_page_name == "teachers.php") {
		$page .= 'Review entered data &raquo;';
		} elseif ($current_page_name == "review.php") {
		$page .= 'Email form data &raquo;';
		} else {
		$page .= 'Continue &raquo;';
		}
		$page .= '" />';
}


if($current_page_name != "sent.php" && $current_page_name != "review.php" && $current_page_name != "teachers.php" && school_reviewed($posted['name_of_school']))
{
	$page .= '<input type="submit" id="back-to-review" value="Review page &rArr;" />';
}

$page .= '</div>';
