import os
import sys
import random
import socket

count=0;
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',1337))
while True:
   
    print("connected")
    st='connection done'
    byt = random._urandom(1084)
    #byt=st.encode()
    s.send(byt)
    count=count + 1

