"""
Title: netstat_join_tasklist.py
Date: September 28, 2019
Author: Werner <me@werner.wiki>
Homepage: https://blog.werner.wiki/
Verify: Windows Server 2003, Windows 7, Windows 10

Check the process name corresponding to each port when there is no netstat `-b` permission.

Usage:
    netstat -ano > temp.txt
    tasklist /V /fo csv >> temp.txt
    python netstat_join_tasklist.py temp.txt
    del temp.txt
"""


import os
import sys


def print_usage():
    print("""Usage:
    netstat -ano > temp.txt
    tasklist /V /fo csv >> temp.txt
    python netstat_join_tasklist.py temp.txt
    del temp.txt""")


def extract_netstat_output(text):
    """
    Example input:
  TCP    0.0.0.0:49668          0.0.0.0:0              LISTENING       4124
  TCP    0.0.0.0:49679          0.0.0.0:0              LISTENING       952
  UDP    0.0.0.0:68             *:*                                    2220
  UDP    0.0.0.0:500            *:*                                    4616
    """
    netstat_output = list()
    for line in text.split('\n'):
        if line.strip().startswith('TCP') or line.strip().startswith('UDP'):
            pid = line.split(' ')[-1].strip()
            netstat_output.append({'pid': pid, 'line': line})
    return netstat_output


def extract_tasklist_output(text):
    """
    Example input:
"Image Name","PID","Session Name","Session#","Mem Usage","Status","User Name","CPU Time","Window Title"
"System Idle Process","0","Services","0","8 K","Unknown","NT AUTHORITY\SYSTEM","477:02:40","N/A"
"System","4","Services","0","4,164 K","Unknown","N/A","1:33:11","N/A"
"Registry","120","Services","0","33,772 K","Unknown","N/A","0:00:10","N/A"
"smss.exe","484","Services","0","612 K","Unknown","N/A","0:00:00","N/A"
"csrss.exe","720","Services","0","2,244 K","Unknown","N/A","0:00:06","N/A"
    """
    tasklist_output = list()
    for line in text.split('\n'):
        if line.strip().startswith('"'):
            split_result = line[1:].split('","')
            pid = split_result[1].strip()
            # If you want to modify the output column, change it here.
            output_line = '\t'.join([split_result[0], split_result[6]])
            tasklist_output.append({'pid': pid, 'line': output_line})
    return tasklist_output


def netstat_join_tasklist(netstat_output, tasklist_output):
    result = list()
    for port in netstat_output:
        for task in tasklist_output:
            if port['pid'] == task['pid']:
                result.append('{}\t{}'.format(port['line'], task['line']))
    return result


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_usage()
    elif not os.path.exists(sys.argv[1]):
        print("The file `{}` does not exists.".format(sys.argv[1]))
    else:
        with open(sys.argv[1], 'r') as f:
            text = f.read()
        netstat_output = extract_netstat_output(text)
        tasklist_output = extract_tasklist_output(text)
        result = netstat_join_tasklist(netstat_output, tasklist_output)
        for line in result:
            print(line)
