#!/usr/bin/env python
import Skype4Py
import socket

"""
Skype bot

"""

host = 'localhost'
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skype = Skype4Py.Skype()
skype.Attach()
s.bind((host,port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        skype.Friends
        for user in skype.Friends:
            chat = skype.CreateChatWith(user.Handle)
            chat.SendMessage(data)
    client.close()
