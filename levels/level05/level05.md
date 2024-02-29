# level05

## Initial Clue
Upon logging in as level05, an automatic message is displayed in the shell: "You have new mail." Investigating further, we find a file named `level05` in `/var/mail`. Reviewing its contents (`cat /var/mail/level05`), it reveals a cron job scheduled to execute a script located at `/usr/sbin/openarenaserver` every two minutes.

## Execution of Scheduled Script
Inspecting the script at `/usr/sbin/openarenaserver`, we find that it iterates over all files in the `/opt/openarenaserver` directory and executes them. This presents a vulnerability: any script placed in the `/opt/openarenaserver` directory will be executed.

## Crafting the Exploit Script
To exploit this vulnerability, we create our own script to retrieve the flag:
- `echo '#!/bin/bash' > /tmp/exploit.sh`
- `echo 'getflag > /tmp/flag' >> /tmp/exploit.sh`
- `chmod +x /tmp/exploit.sh`

## Retrieval of Flag
After two minutes, we check the `/tmp` directory and examine the contents of the newly created `flag` file, which contains the output of the `getflag` command executed by the script triggered by the cron job, that is the flag we need !
