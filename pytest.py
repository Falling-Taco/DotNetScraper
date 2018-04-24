<?php
$data = $_POST['issue_date'];
$myfile = fopen("testtest.txt", "w+") or die("Unable to open file!");
fwrite($myfile, $data)
fclose($myfile);
?>
