<?php

$previous_year = 2012;
$competition_year = date('Y');
if ($competition_year == $previous_year) $competition_year += 1;
$competition_date = 'Wednesday/Woensdag 17 April';
$entries_closing_date_eng = 'Friday 15 March ';
$entries_closing_date_afr = 'Vrydag 15 Maart';

// Competition: 17/04 Wednesday Woensdag
// Written Sub Dead: 08/03 Friday
// Elec Sub Dead: 15/03 Friday

include("functions.php"); 

#foreach($posted as $posted_key => $posted_val
#$posted = stripslashes($posted);

if(is_numeric(school_submitted($_POST['name_of_school']))) {
$school_submitted = TRUE;
}
else {
$school_submitted = FALSE;
}
$page = '';
?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="en-US"> 
<head> 
	<title><?php echo $competition_year; ?> UCT Maths Competition - <?php
	if ($current_page_number <= $total_pages) { echo "Page " . $current_page_number . " of " . $total_pages;  }
	elseif ($current_page_name == "review.php") { echo "Review form data"; }
	else { echo "Mail sent"; }
	?></title> 
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> 
<link rel="stylesheet" href="style.css" type="text/css" media="all" /> 
<meta name="robots" content="noindex,nofollow" /> 

<script src="jquery-1.3.2.min.js" type="text/javascript"></script> 
<script src="jquery.validate.pack.js" type="text/javascript"></script> 
<script type="text/javascript"> 
$(document).ready(function() {
	$("#umc").validate({
	<?php if ($short_current_page_name == "review") {?>	
	submitHandler: function(form) {
		$("input[type!=submit]").removeAttr("disabled");
		form.submit();
		}
	<?php } ?>
	
	<?php if ($short_current_page_name == 'grade8' || $short_current_page_name == 'grade8' || $short_current_page_name == 'grade10' || $short_current_page_name == 'grade11' || $short_current_page_name == 'grade12') {?>
	rules: {
	<?php for ($i = 1; $i <= 5; $i++) { ?>
"grade<?php echo $grade_number; ?>[<?php echo $i; ?>][firstname]": { "required": "#grade<?php echo $grade_number; ?><?php echo $i; ?>surname:filled"},
		"grade<?php echo $grade_number; ?>[<?php echo $i; ?>][gender]": { "required": "#grade<?php echo $grade_number; ?><?php echo $i; ?>surname:filled"},
		"grade<?php echo $grade_number; ?>[<?php echo $i; ?>][language]": { "required": "#grade<?php echo $grade_number; ?><?php echo $i; ?>surname:filled"},
		
		"grade<?php echo $grade_number; ?>[<?php echo $i; ?>][surname]": { "required": "#grade<?php echo $grade_number; ?><?php echo $i; ?>firstname:filled"}<?php if ($i != 5) { echo ","; } ?>
		<?php } ?>
		
	}
	<?php } ?>
		
		
	});
	
	$("#back").click(function() {
		$("#umc").attr("action","<?php echo $page_list[$current_page_number - 1]; ?>");
	});

	$("#back-to-review").click(function() {
		$("#umc").attr("action","review.php");
	});

	<?php if($short_current_page_name == "review") { ?>
	$('#print_button').click(function() {
		window.print();
		return false;
	});
	
	$("input[type!=submit]").attr({disabled: "disabled"});
	<?php } ?>
	
	<?php if($short_current_page_name == "index") { ?>
jQuery("#name_of_school").change(function(){
	
			var school = $(this).attr("value");
	
			jQuery.ajax({
				type: "POST",
				url: "school-details.php",
				dataType: "html",
				cache: false,
				data: { school: school },
				success: function(html) {
					jQuery("#school_details").replaceWith(html);
				}
			});
	});
	<?php } ?>
	
});
</script> 
</head> 
<body id="<?php echo $short_current_page_name; ?>">
<div id="wrapper">

<div id="header">
<h1><?php echo $competition_year; ?> UCT MATHEMATICS COMPETITION / <?php echo $competition_year; ?> UK WISKUNDEKOMPETISIE <br />
ENTRY FORM / INSKRYWINGSVORM<br />
<?php echo $competition_date . ' ' . $competition_year; ?></h1>
<h2>Closing date for entries: <?php echo $entries_closing_date_eng . ' ' . $competition_year; ?> / <?php echo $entries_closing_date_afr . ' ' . $competition_year; ?></h2>
</div>

<form action="<?php echo $page_list[$current_page_number + 1]; ?>" method="post" id="umc">

<?php if ( $current_page_name != "review.php" && $current_page_name != "sent.php" ) {
carry_through($posted,$short_current_page_name); 
}?>
