## client.py
#현재 쌍방 채팅이 가능하게끔 설정을 해놓았습니다.

from socket import *
import threading
import time

def send(sock):
    while 1:
        sendData = input('')
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while 1:
        recvData = sock.recv(1024)
        print('상대방 :',recvData.decode('utf-8'))

port = 8080

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))

print('접속 완료.')

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()

while 1:
    time.sleep(1)
    pass