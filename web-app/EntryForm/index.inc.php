<?php
include("schools-array.php");

$page .= '
<table>
	<tr valign="top">
		<td class="english"><label for="name_of_school">NAME OF SCHOOL</label></td>
		<td>';
			if ($current_page_name == "index.php") {			
			$page .= '<select name="name_of_school" id="name_of_school" class="required" >
			<option></option>';
				foreach ($schools as $school => $school_details) {
					$page .= '<option value="' . $school . '"';
					if ($school == $posted["name_of_school"]) { $page .= ' selected="selected"';}
					$page .= '>' . $school . '</option>';
				} //end foreach
			$page .= '</select>';
			} // end if
			elseif ($current_page_name == "review.php" || $current_page_name == "sent.php") {
			$page .= '<input name="name_of_school" id="name_of_school" size="50" value="' . stripslashes($posted["name_of_school"]) . '" />';
			}
			$page .= '
			</td>
		<td class="afrikaans"><label>NAAM VAN SKOOL</label></td>
	</tr>
</table>
<div id="school_details">
<table>
	<tr valign="top">
		<td class="english"><label for="address">ADDRESS</label></td>
		<td><input size="50" name="address" id="address" value="' . $posted["address"] . '" /></td>
		<td class="afrikaans"><label>ADRES</label></td>
	</tr>
</table>
<table>	
	<tr valign="top">
		<td class="english"><label for="tel">TEL</label></td>
		<td><input size="' . (strlen($posted["tel"]) * 1.1) . '" name="tel" id="tel" value="' . $posted["tel"]. '" class="required" /></td>

		<td class="english"><label for="fax">FAX</label></td>
		<td><input size="' . (strlen($posted["fax"]) * 1.1) . '" name="fax" id="fax" value="' . $posted["fax"] . '" /></td>

		<td class="english"><label for="email">EMAIL</label></td>
		<td><input size="' . (strlen($posted["email"]) * 1.1 ). '" name="email" id="email" value="' . $posted["email"] . '" class="email required" /></td>
	</tr>
 </table>
 </div>';