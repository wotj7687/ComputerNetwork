## server.py

import socket ## 원격지 호스트의 프로세스와 통신하도록 만든 인터페이스
import argparse
from threading import Thread


def threaded(c):
        while True:
                data = c.recv(1024)
                if not data: break
                
                print(data.decode())
                c.sendall(data[::-1])
        c.close()

def run_server():
    host = '' ##127.0.0.1 Loopback

    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        ## family=socket.AF_INET 인터넷연결?, type=secket.SOCK_STREAM TCP타입으로 하겠다.
        
        s.bind((host,int(args.p))) ##자신의 IP와 Port번호 소켓에 등록, 포트 연다
        s.listen(5) ## max 1 client 요청 수신 대기 모드 진입


        while True:
                
                conn, addr = s.accept() ##client 요청 수락

                t = Thread(target = threaded, args=(conn,))
                t.start()

        s.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Echo server -p port")
    parser.add_argument('-p', help="port_number", required=True)

    args = parser.parse_args()
    run_server()

