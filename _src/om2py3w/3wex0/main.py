# -*- encoding: utf-8 -*-
#! /usr/bin/env python
'''
文件说明： 这是个Net局域网版本的极简交互式笔记程序
作者信息： penguinjing
版本自述:  0.0.1
程序参考： https://pymotw.com/2/socket/udp.html
'''
# 全局引用
import socket
import sys

# 全局变量
# PATH = "/path/2/work dir"

# 函式撰写区

def setupserver():
    # Echo Server programe part
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = ('localhost', 9009)
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

def setupclient():
    # Echo client program part
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

    server_address = ('localhost', 9009)
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

def main(): 
    if argv[1] = 'c':
        setupclient()

    elif argv[1] = 's':
        setupserver()

    else:
        print 'no specify mode, please run it again.'
        print 'python main.py [s|c]'
        print '       s - server mode'
        print '       c - client mode'

# 自检区
if __name__ == "__main__": 
    main()