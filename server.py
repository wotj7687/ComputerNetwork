## server.py

import socket ## 원격지 호스트의 프로세스와 통신하도록 만든 인터페이스
import argparse

def run_server(port=4000):
    host = '' ##127.0.0.1 Loopback

    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        ## family=socket.AF_INET 인터넷연결?, type=secket.SOCK_STREAM TCP타입으로 하겠다.
        
        s.bind((host,port)) ##자신의 IP와 Port번호 소켓에 등록, 포트 연다
        s.listen(1) ## max 1 client 요청 수신 대기 모드 진입

        conn, addr = s.accept() ##client 요청 수락
        msg = conn.recv(1024)
        print(msg.decode()) ## msg is a binary data, so we need to decode it/ 받은 값이 이진수여서 decode를 통해 바꿔줘야한다.

        
        
        conn.sendall(msg[::-1]) ## client에서 보내준 문자열을 거꾸로 만들어주는 코드
        conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Echo server -p port")
    parser.add_argument('-p', help="port_number", required=True)

    args = parser.parse_args()
    run_server(port=int(args.p))

