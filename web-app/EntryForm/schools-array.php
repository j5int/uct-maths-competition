<?php
// generate $schools array

$schoolsxml = @simplexml_load_file("Schools.xml");
$numschools = count($schoolsxml);

for ($i = 0; $i<$numschools; $i++) {
	$schoolname = $schoolsxml->Schools[$i]->Name;
	$schooladdress = $schoolsxml->Schools[$i]->Address;
	$schoolphone = $schoolsxml->Schools[$i]->Phone;
	$schoolfax = $schoolsxml->Schools[$i]->Fax;
	$schoolemail = $schoolsxml->Schools[$i]->Email;
	$schoolkey = $schoolsxml->Schools[$i]->Key;
	
	$schooladdress = strtr($schooladdress, array("\r\n" => ' ', "\r" => ' ', "\n" => ' '));
	
	$schools["$schoolname"]["Address"] = "$schooladdress";
	$schools["$schoolname"]["Phone"] = "$schoolphone";
	$schools["$schoolname"]["Fax"] = "$schoolfax";
	$schools["$schoolname"]["Email"] = "$schoolemail";
	$schools["$schoolname"]["Key"] = "$schoolkey";
}
ksort($schools);
?>