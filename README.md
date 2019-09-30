# WindowsPrivilegeEscalationSet

[中文](cn)


Privilege escalation tool sets on Windows. 

## netstat_join_tasklist.py

Get the process name corresponding to each port.

In Windows, `netstat` has a parameter `-b` that gives the name of the process corresponding to the port,
but using this parameter requires permissions that we may not have.
In fact, the `-o` parameter of `netstat` can give the process id corresponding to each port.
The command `tasklist` can give the name of the process corresponding to the process id.
So in order to get the process name corresponding to each port, 
we only need to join the output of `netstat` and `tasklist` without using the `-b` parameter.
This script is used to do this.

Our design is to redirect the output of `netstat` and `tasklist` to a file 
then parse it by Python, because there is probably no Python environment on Windows. 
Redirecting to a file makes it easy for us to transfer it to a machine with a Python environment.


## echo_translate.py

Use the `echo` command with copy and paste to implement text file transfer.

When we get a shell, we may want to transfer the file. If we only transfer a small text file, 
we can redirect each line of the file to the file on the remote host with the `echo` command. 
This script is used to generate these `echo` commands.

This script receives three parameters. 
The first parameter is a native file path, which is the file to be transferred.
The second parameter is a remote host file path, which is the target of the `echo` command redirect.
The third parameter is optional and will appear after all `echo` commands. 
It is a command that is executed in addition to the remote host.
