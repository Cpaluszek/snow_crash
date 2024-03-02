# level05

## Initial Clue
once logged into level06 we find 2 files:
- `level06.php` => it defines two functions (x and y) and processes the content of a file specified as a command-line argument ($y). The content is manipulated using regular expressions, and the final result is printed.

- `level06` => if we `file level06`we find out that it is an executable: 
```
level06: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0xaabebdcd979e47982e99fa318d1225e5249abea7, not stripped
```

## Relationship between the 2 files
- Attempting to execute level06 results in the following message:
```
PHP Warning:  file_get_contents(): Filename cannot be empty in /home/user/level06/level06.php on line 4
```
- What does this mean? It indicates that the PHP script level06.php is attempting to use file_get_contents() on an empty filename. But why is level06.php involved when we try to execute `./level06`? While we can't access the source code of the binary executable (we attempted to disassemble it with `objdump -d level06 > level06_disassembly.txt` but it was not useful), it's evident that the executable takes a file as an argument and passes it to the level06.php script.

## Vulnerability inside level06.php
- Upon closer inspection of the script, we discover that it uses the preg_replace method, which allows for replacing a pattern with a string within a string using regular expressions. The issue arises from the fact that until recently (the /e modifier was removed from PHP as of version 7.0, but this exercise hasn't been updated, and in any case, hackers can still potentially exploit PHP scripts created prior to this change), it was possible to use the /e modifier to evaluate the replacement string as PHP code. Our script precisely utilizes the /e modifier in this line:
```
$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
```

## Implications
This means that if we pass a file containing the pattern `[x (.*)\]` to level06 as an argument, it will pass it to `level06.php`, and whatever is included in the `(.*)` argument of x will be executed (\\2 being the second element of the pattern).
Hence, we create a file in the only location where we have permission to create a file, /tmp, containing the command we want the script to execute: `echo '[x {${exec(getflag)}}]' > /tmp/getflag`. Then, we pass this file as an argument when launching level06: `./level06 /tmp/getflag`, obtaining the flag:
```
PHP Notice:  Use of undefined constant getflag - assumed 'getflag' in /home/user/level06/level06.php(4) : regexp code on line 1
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub in /home/user/level06/level06.php(4) : regexp code on line 1
```

NB 
Starting with PHP 7.0, the /e modifier has been replaced with a callback function to mitigate this vulnerability. Instead of using preg_replace, it's mandatory to use preg_replace_callback with a callback function instead of the replacement string. So, in our case, the script should have been:
```
$a = preg_replace_callback("/(\[x (.*)\])/", function($matches) { return y($matches[2]); }, $a);
```


