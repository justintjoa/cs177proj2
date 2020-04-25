#Connect to cs177.seclab.cs.ucsb.edu on port 42293 to interact with your challenge!
import socket
import sys
from struct import *
from io import StringIO
from scapy.all import * 



a = IP(ttl=10)/ICMP(type=8)
a.src = '192.168.222.1'
a.dst = '192.168.222.2'
a.version = 4


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



# Connect the socket to the port where the server is listening
server_address = ('cs177.seclab.cs.ucsb.edu', 44765)
sock.connect(server_address)

division = 2

while(True):
    m_len = len(a)
    m_len = m_len.to_bytes(2,'big')
    output = m_len + bytes(a)
    sock.sendall(output)
    data = sock.recv(100)
    input_length = int.from_bytes(data[0:2], "big") + 2
    while (len(data) < input_length):
        data = data + sock.recv(100) 
    print(data)
    data = data[2:]
    pack_in = IP(data)
    pack_in.show()
    



