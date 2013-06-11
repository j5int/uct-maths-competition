<?php
$page .='<h5>NB Please note that every school must send at least 1 Invigilator and that if the 
responsible teacher is going to invigilate kindly add your name to the Invigilators list. </h5>
 
 <table>
 
 <tr valign="top">
	<td></td>
	<td>INVIGILATORS SURNAME /<br/>OPSIGTERS VAN</td>
	<td>INVIGILATORS FIRST NAME /<br/>OPSIGTERS VOORNAAM</td>
	<td>CELL / FAX:</td>
	<td>EMAIL:</td>
 </tr>';
for ($i=1; $i<=7; $i++) {
if ($short_current_page_name == "review" && $posted["invigilator" . $i . "surname"] == "") {
	continue;
}
if ($short_current_page_name == "sent" && $posted["invigilator" . $i . "surname"] == "") {
	continue;
}
 
$page .= '<tr valign="top">

	<td>' . $i . '</td>
	<td><input size="' . max(strlen(stripslashes($posted["invigilator" . $i . "surname"])),30) . '" name="invigilator' . $i . 'surname" id="invigilator' . $i . 'surname" value="' . stripslashes($posted["invigilator" . $i . "surname"]) .'"';
	if ($i == 1) { $page .= ' class="required" ';}
	$page .='/></td>

	<td><input size="' . max(strlen(stripslashes($posted["invigilator" . $i . "firstname"])),30) . '" name="invigilator' . $i . 'firstname" id="invigilator' . $i . 'firstname" value="' . stripslashes($posted["invigilator" . $i . "firstname"]) . '"';
	if ($i == 1) { $page .= ' class="required" ';}
	$page .= '/></td>

	<td><input size="' . (strlen($posted["invigilator" . $i . "number"])*1.1) . '" name="invigilator' . $i . 'number" id="invigilator' . $i . 'number" value="' . $posted["invigilator" . $i . "number"] . '"';
	if ($i == 1) { $page .= ' class="required" ';}
	$page .= '/></td>

	<td><input size="' . (strlen($posted["invigilator" . $i . "email"])*1.1) . '" name="invigilator' . $i . 'email" id="invigilator' . $i . 'email" value="' . $posted["invigilator" . $i . "email"] . '"';
	if ($i == 1) { $page .= ' class="required email" ';}
	$page .= '/></td>

</tr>';
 }
 
 $page .='</table>
<br />

<table>
	<tr>
		<td>
	
<table id="responsible_teacher_name_table">

	<tr>
		<td colspan="2">
		
	<label for="responsible_teacher_name">RESPONSIBLE TEACHER NAME / VERANTWOORDELIKE ONDERWYSER NAAM</label><br />
	 <input size="' . max(strlen(stripslashes($posted["responsible_teacher_name"])),30) . '" name="responsible_teacher_name" id="responsible_teacher_name" value ="' . stripslashes($posted["responsible_teacher_name"]) . '" class="required" /><br /><br />	
		
		</td>		
	</tr>
</table>

		</td>
		<td>

<table id="responsible_teacher_details">
	<tr>
		<td>
		<label class="rtl" for="responsible_teacher_tel">TEL (CELL):</label>
		</td>
		
		<td>
		<label class="rtl" for="responsible_teacher_fax">FAX</label>
		</td>
	</tr>
	
	<tr>
		<td>
		<input size="' . (strlen($posted["responsible_teacher_tel"])*1.2) . '" name="responsible_teacher_tel" id="responsible_teacher_tel" value ="' . $posted["responsible_teacher_tel"] . '" class="required" />
		</td>
		
		<td>
		<input size="' . (strlen($posted["responsible_teacher_fax"])*1.2) . '" name="responsible_teacher_fax" id="responsible_teacher_fax" value ="' . $posted["responsible_teacher_fax"] . '" class="required" />
		</td>
	</tr>

</table>

		</td>
	</tr>
</table>

';
