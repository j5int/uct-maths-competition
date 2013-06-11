<?php

include("schools-array.php");

$formschool = $_POST["school"];
// change up apostrophes
$formschool = stripslashes(str_replace("'","&#039",$formschool));

$formschooladdress = $schools["$formschool"]["Address"];
$formschoolphone = $schools["$formschool"]["Phone"];
$formschoolfaxs = $schools["$formschool"]["Fax"];
$formschoolemail = $schools["$formschool"]["Email"];
?>
<div id="school_details">
<table>
	<tr valign="top">
		<td class="english"><label for="address">ADDRESS</label></td>
		<td><input size="50" name="address" id="address" value="<?php echo $formschooladdress; ?>" /></td>
		<td class="afrikaans"><label>ADRES</label></td>
	</tr>
</table>
<table>	
	<tr valign="top">
		<td class="english"><label for="tel">TEL</label></td>
		<td><input size="20" name="tel" id="tel" value="<?php echo $formschoolphone; ?>" class="required" /></td>
		<td class="afrikaans"></td>

		<td class="english"><label for="fax">FAX</label></td>
		<td><input size="20" name="fax" id="fax" value="<?php echo $formschoolfaxs; ?>" /></td>
		<td class="afrikaans"></td>

		<td class="english"><label for="email">EMAIL</label></td>
		<td><input size="50" name="email" id="email" value="<?php echo $formschoolemail; ?>" class="required" /></td>
		<td class="afrikaans"></td>
	</tr>
</table>