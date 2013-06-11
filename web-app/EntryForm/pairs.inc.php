<?php
if ($short_current_page_name == "review" || $short_current_page_name == "sent") {
$page .= '
<table>
	<tr>
		<td>';
}

$page .='<h3 id="pairs_header">NUMBER OF PAIRS  (MAXIMUM FIVE PER GRADE):<br />
 AANTAL PARE  (MAKSIMUM VYF PER GRAAD):</h3>';

if ($short_current_page_name == "review" || $short_current_page_name == "sent") {
$page .= '
		</td>
		<td>';
}
 
$page .='
<table>

<tr>
	<td>8</td>
	<td>9</td>
	<td>10</td>
	<td>11</td>
	<td>12</td>
</tr>
<tr valign="top">';

for ($i = 8; $i <= 12; $i++) {
	if ($short_current_page_name == "review" || $short_current_page_name == "sent") {
	$page .= '<td>
	<input size="1" name="pairs[grade' . $i . '][number]" id="pairsgrade' . $i . 'number" value="' . $posted[pairs]["grade" . $i][number] . '" />
	</td>';
	} else { 
	$page .= '<td>
	<select name="pairs[grade' . $i . '][number]" id="pairsgrade' . $i . 'number" class="required">
	<option></option>';
		for ($j = 0; $j <= 5; $j++) {
			if ($posted[pairs]["grade" . $i][number] == $j && $posted[pairs]["grade" . $i][number]  != "") {
			$page .= '<option value="' . $j . '" selected="selected">' . $j . '</option>';
			}
			else {
			$page .= '<option value="' . $j . '">' . $j . '</option>';
			}
		}
	$page .='</select>
	</td>';
	}
} 
$page .='</tr>

</table>';

if ($short_current_page_name == "review" || $short_current_page_name == "sent") {
$page .= '
		</td>
	</tr>
</table>';
}