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
