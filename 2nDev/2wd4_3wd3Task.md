3W - Net 101 日记本

- 任务目标：在CLI基础上完成极简交互笔记的网络版本(局域网)
- 需求如下：
    - 每次运行时合理打印出过往的所有笔记
    - 一次接受输入一行笔记
    - 在服务器端保存为文件
        - 在所有访问的客户端可以获得历史笔记
    - 支持多个客户端同时进行笔记记录
- 发布到各自仓库`_src/0m2py3w/3wex0/`目录中
- 关键技术
    - [UDP协议](https://en.wikipedia.org/wiki/User_Datagram_Protocol)
    - C/S 服务器/客户端架构系统

- Server 服务器端实现流程  
> socket()  
> bind()  
> listen()  
> accept() - possibly repeating the accept()  
```
# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()
```  
  
- Client 客户端实现流程
> socket()  
> connect()  
```
# Echo client program
import socket

HOST = 'daring.cwi.nl'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
```
