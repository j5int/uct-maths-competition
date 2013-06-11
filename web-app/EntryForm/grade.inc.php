<?php
if ($short_current_page_name == "review" || $short_current_page_name == "sent") {

} else { 
	$page .= '<h3>INDIVIDUALS / INDIVIDUE - Grade ' .  $grade_number . '</h3>';
}

if ($short_current_page_name != "review" && $short_current_page_name != "sent") {
	$page .= '<h4>Please complete all fields for each entrant</h4>';
 }

 $page .= '<table class="grade">';
 
 if ($short_current_page_name != "review" && $short_current_page_name != "sent") {
 $page .= '<thead class="grade' . $grade_number . '"><tr valign="top">
	<td></td>
	<td>SURNAME<br />VAN</td>
	<td>FIRST NAME<br />VOORNAAM</td>
	<td>GENDER (M/F)<br />GESLAG (M/V)</td>
	<td class="language">LANGUAGE PREFERENCE<br />TAALVOORKEUR (E/A)</td>
</tr></thead>';
}

for ($j = 1; $j <= 5; $j++) {
	 if ($short_current_page_name == "review" && $posted["grade" . $grade_number][$j]["surname"] == "") { 
	 continue;
	 }
	 if ($short_current_page_name == "sent" && $posted["grade" . $grade_number][$j]["surname"] == "") { 
	 continue;
	 }
$page .= '
<tr valign="top">
	<td>' . $j . '</td>
	<td><input size="40" name="grade' . $grade_number . '[' . $j . '][surname]" id="grade' . $grade_number . $j . 'surname" value="' . stripslashes($posted["grade" . $grade_number][$j]["surname"]) . '"/></td>
	<td><input size="40" name="grade' . $grade_number . '[' .  $j . '][firstname]" id="grade' . $grade_number . $j. 'firstname" value="' . stripslashes($posted["grade" . $grade_number][$j]["firstname"]) . '" /></td>';
	if ($short_current_page_name == "review" || $short_current_page_name == "sent") {
		$page .=' <td>
		<input size="1" name="grade' . $grade_number . '[' . $j . '][gender]" id="grade' . $grade_number . $j . 'gender" value="' . $posted["grade" . $grade_number][$j]["gender"] . '" />
	</td>
	<td>
		<input size="1" name="grade' . $grade_number . '[' . $j . '][language]" id="grade' . $grade_number . $j . 'language" value="' . $posted["grade" . $grade_number][$j]["language"] . '"/>
	</td>';
	} else {
#	$page .= '<td>
#		<select name="grade' . $grade_number . '[' . $j . '][gender]" id="grade' . $grade_number . $j . 'gender">
#			<option value=""></option>
#			<option value="Male/Manlik"';
#			if ($posted["grade" . $grade_number][$j]["gender"]=="Male/Manlik"){$page .= ' selected="selected"';}
#			$page .= '>Male/Manlik</option>
#			<option value="Female/Vroulik"';
#			if ($posted["grade" . $grade_number][$j]["gender"]=="Female/Vroulik"){$page .= ' selected="selected"';}
#			$page .= '>Female/Vroulik</option>
#		</select>
#	</td>
#	<td>
#		<select name="grade' . $grade_number . '[' . $j . '][language]" id="grade' . $grade_number . $j . 'language">
#			<option value=""></option>
#			<option value="English"';
#			if ($posted["grade" . $grade_number][$j]["language"]=="English"){$page .= ' selected="selected"';}
#			$page .= '>English</option>
#			<option value="Afrikaans"';
#			if ($posted["grade" . $grade_number][$j]["language"]=="Afrikaans"){$page .= ' selected="selected"';}
#			$page .= '>Afrikaans</option>
#		</select>
#	</td>';

	$page .= '<td>
		<input name="grade' . $grade_number . '[' . $j . '][gender]" id="grade' . $grade_number . $j . 'gender" type="text"';
			if ($posted["grade" . $grade_number][$j]["gender"]) {
					$page .= 'value = "' . $posted["grade" . $grade_number][$j]["gender"] . '"';
			}
		$page .= ' />
	</td>
	<td>
		<input name="grade' . $grade_number . '[' . $j . '][language]" id="grade' . $grade_number . $j . 'language" type="text"';
			if ($posted["grade" . $grade_number][$j]["language"]) {
				$page .= 'value = "' . $posted["grade" . $grade_number][$j]["language"] . '"';
			}
		$page .= ' />
	</td>';

	}
$page .= '</tr>';

} // end for

$page .= '</table>';
