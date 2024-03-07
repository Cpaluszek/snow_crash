# level09

## Initial Clue
once logged into level06 we find 2 files:
- `level09`
if `file level09` we find out that it's an executable: 
```
level09: setuid setgid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0x0e1c5a0dfb537112250e1c78d5afec3104abb143, not stripped
```
- `token`
if we `file token` we find out that it contains data:
```
token: data
```

## Trying to execute ./level09
- Running ./level09 results in the message: You need to provide only one arg. This implies that an argument is required, but what should it be?
- Trying token as an argument yields: tpmhr.
- The output shares the same length as the filename passed as an argument, with the same initial letter and subsequent letters following a pattern.
- It becomes clear that there is a rule governing the script's transformation of the filename: a shift for each character corresponding to its index. For instance, t remains t, o becomes o + 1 = p, k becomes k + 2 = m, and so on.
- However, the token file contains data, as observed earlier. If we cat token, the output is: f4kmm6p|=�p�n��DB�Du{��.
- Attempting to pass the content of token as an argument to the script doesn't seem to be the correct approach, as it produces the following output:
```
$ ./level09 "$(cat token)"
f5mpq;v�E��{�{��TS�W�����
```

## What if token Contains the Output of the Script with the Shifting Done?
- This suggests that to revert the token value to its original state, we need to perform the opposite of what the script does.
- We create a PHP script this time (in /tmp, the only place where we have permission to create things), granting execution permission:
```
#!/usr/bin/php
<?php

$input = $argv[1];

for ($i = 0; $i < strlen($input); $i++) {
    $val = $input[$i];
    echo chr(ord($val) - $i);
}

echo "\n";
```
- than we launch the script with the content of `token`as argument and we have a plausible token for the flag09 => "/tmp/reverse.php \`cat token\`"
- this way we get the token: `f3iji1ju5yuevaus41q1afiuq`

## getting the flag
- using the token as password for `su flag09` allows us to access flag09 and launching `getflag` we get the flag
