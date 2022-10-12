<?php
$output1 = shell_exec('pwd');
$output2 = shell_exec('ls');
$output3 = shell_exec('ls /');
$output4 = shell_exec('ps aux --no-headers | wc -l');

echo "<pre>$output1</pre>";
echo "<pre>$output2</pre>";
echo "<pre>$output3</pre>";
echo "<pre>$output4</pre>";
?>
