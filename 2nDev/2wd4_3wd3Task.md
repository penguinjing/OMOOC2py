3W - Net 101 日记本

- 任务目标：在CLI基础上完成极简交互笔记的网络版本(局域网)
- 需求如下：
    - 每次运行时合理打印出过往的所有笔记
    - 一次接受输入一行笔记
    - 在服务器端保存为文件(有一个中央服务器运行服务器程序)
        - 在所有访问的客户端可以获得历史笔记
    - 支持多个客户端同时进行笔记记录
    - 通过UDP 协议
- 发布到各自仓库`_src/0m2py3w/3wex0/`目录中
- 关键技术
    - [UDP协议](https://en.wikipedia.org/wiki/User_Datagram_Protocol)
    - C/S 服务器/客户端架构系统

UDP特性[1. Demo参考](https://pymotw.com/2/socket/udp.html) [2.参考](http://www.tutorialspoint.com/python/python_networking.htm)  

UDP与TCP不同，其是面向消息的协议，不要求建立连接(握手)。

- Server 服务器端实现流程及代码示例  
> socket()  
> bind()  
> recvfrom() - possibly repeating the recvfrom()  
```
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)
    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data
    if data:
        sent = sock.sendto(data, address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
```  
  
- Client 客户端实现流程及代码示例
> socket()  
> sendto() or recvfrom()
> close()
```
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = 'This is the message.  It will be repeated.'

try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
```
输入 ?/h/H 打印当前帮助  
输入 q/bye 推出笔记  
输入 r/sync 同步笔记历史  

