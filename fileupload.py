<?php
$myfile = fopen("testtesttest.txt", "w+") or die("Unable to open file!");
fwrite($myfile, 'test\ntest\ntest\ntest\n');
fclose($myfile);
?>
