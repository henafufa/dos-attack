import os
import sys
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',1337))
s.listen(1)
conn ,addr=s.accept()
data=conn.recv(2000)
data.decode()

