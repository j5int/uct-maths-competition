 <?php include("header.php"); ?>

 <h3 id="review_header">Please review the data you entered</h3>

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

$page .= '<tr><td colspan="6"><hr /></td></tr>';

for ($k = 8; $k <=12; $k++) {
$grade_number = $k;

	if(count($posted["grade" . $k]) > 0) {
		$page .= '<tr>
		<td>Grade ' . $k . '<br />Graad ' . $k . '</td>
		<td colspan="5">';
		include("grade.inc.php");
		$page .= '</td>
		</tr>';

	$page .= '<tr><td colspan="6"><hr /></td></tr>';

	}


}

$page .= '</table>';

include("pairs.inc.php");
include("teachers.inc.php");

include("buttons.php"); 

// update reviewed list

$filename = 'reviewed' . date('Y') . '.txt';
$content = str_replace('&#039',"'",$posted['name_of_school']) . "\n";

$handle = fopen($filename,'a');
fwrite($handle, $content);
fclose($handle);

// end update reviewed list


echo $page;
 
include("footer.php"); 

?>
