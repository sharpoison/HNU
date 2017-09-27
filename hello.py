# -*-coding:GBK-*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import struct
import binascii
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

Pwron='\x4C\x69\x67\x68\x74\x6F\x6E\xFE\x05\x14\x52\x01\x11\x6C\xFF'
a=[0x4C, 0x69, 0x67, 0x68, 0x74, 0x6F, 0x6E, 0xFE,0x05, 0x14, 0x52, 0x01, 0x11, 0x6C, 0xFF]

    # 发送数据:
s.connect(('10.62.193.5', 4001))
#data=struct.pack("B",a)
    # 接收数据:
#print(data)


#data= binascii.a2b_hex ("4C696768746F6EFE05145201116CFF")
s.send('\x4C\x69\x67\x68\x74\x6F\x6E\xFE\x05\x14\x52\x01\x11\x6C\xFF')
print(s.recv(1024))
s.close()



