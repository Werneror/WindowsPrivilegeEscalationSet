# WindowsPrivilegeEscalationSet

Windows下的提权工具集。


## netstat_join_tasklist.py

给出每个端口对应的进程名。

在Windows中，`netstat`有参数`-b`可以给出端口对应的进程名，但使用这个参数需要权限，
在提权时往往不具备这样的权限。其实`netstat`的`-o`参数可以给出每个端口对应的进程号，
而命令`tasklist`可以给出进程号对应的进程名。所以只需要组合一下就可以不使用`-b`参数
得到每个端口对应的进程名。这个脚本便用来做这件事。

之所以设计成将`netstat`和`tasklist`的输出重定向到文件，再用Python解析文件内容，
是因为Windows上很可能没有Python环境。重定向到文件，便可以将其传输到一个有Python
环境的地方再去解析它。
