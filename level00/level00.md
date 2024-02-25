[README.md](../README.md)
# Level00

While looking in the directory structure, we found this file:

```sh
ls -la /usr/sbin

...
----r--r--  1 flag00  flag00      15 Mar  5  2016 john
...
```

This file is owned by the user we are searching for.

Upon examining the contents of the file:
```sh
cat /usr/sbin/john

cdiiddwpgswtgt
```

We encountered a seemingly encrypted string. To decrypt it, we employed various techniques, starting with the Caesar Cipher:

**Caesar Cipher:**
Using an online tool like Cryptii, we applied a rotation of 15 characters.

This decrypted message provided us with a clue. We proceeded to log in as user flag00 using the command:

```sh
su flag00
```
Subsequently, we executed the getflag command, which rewarded us with the following token:

```sh
Check flag. Here is your token: x24ti5gi3x0ol2eh4esiuxias
```

This token likely serves as an authentication key or further instruction for our investigation.