## server.py

from socket import *
import threading
import time

#보내는 send함수
def send(sock):
    while 1:
        sendData = input('')
        sock.send(sendData.encode('utf-8'))

#받는 receive함수
def receive(sock):
    while 1:
        recvData = sock.recv(1024)
        print('상대방 :',recvData.decode('utf-8'))

port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)

#생성된 소켓의 번호와 실제 어드레스 패밀리를 연결해주는것
serverSock.bind(('',port)) #클라이언트에는 불필요, 서버를 운용할때에는 반드시 필요하다.

#상대방의 접속을 기다리는 단계로 넘어가겠다는 의미
serverSock.listen(1) # listen(1)은 총 1개의 동시접속까지 허용할것이다 라는 의미이다.

connectionSock, addr = serverSock.accept() #accept는 소켓에 누군가가 접속하여 연결되었을때에 비로소 결과값이 return되는 함수.

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr),'에서 접속되었습니다.')

#thread를 이용하여 순서 상관없이 동시적으로 작동할수 있게끔함.
#주의하여야 할 점은, args는 튜플같이 iterable한 변수만 입력될 수 있다는 것이다.
# 그런데 인자가 하나일 경우, (var) 식으로 괄호로 감싸기만 하면 파이썬 인터프리터는 이를 튜플이 아니라 그냥 var로 인식한다.
# 그러므로 인자가 하나라면 (var,) 식으로 입력해야만 튜플로 인식하므로 이 점을 유의해야 한다.
sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1) #1초마다 쉬게해줌
    pass