<?php
$file = '/usr/home/uctmathcomp/public_html/uctmathcomp.co.za/EntryForm/submitted.txt';
echo 'permissions on ' . $file . ' : ' . substr(sprintf('%o', fileperms($file)), -4);
?>
