#!/usr/bin/php
<?php

$input = $argv[1];

for ($i = 0; $i < strlen($input); $i++) {
    $val = $input[$i];
    echo chr(ord($val) - $i);
}

echo "\n";