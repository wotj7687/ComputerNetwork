import socket ## 원격지 호스트의 프로세스와 통신하도록 만든 인터페이스
import glob
import os
import argparse



def run_server(port,dire):

    host = '' ##127.0.0.1 Loopback


    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:

        ## family=socket.AF_INET 인터넷연결?, type=secket.SOCK_STREAM TCP타입으로 하겠다.

        

        s.bind((host,port)) ##자신의 IP와 Port번호 소켓에 등록, 포트 연다

        s.listen(1) ## max 1 client 요청 수신 대기 모드 진입

        conn, addr = s.accept() ##client 요청 수락

        msg = conn.recv(30)

        msg = msg.decode() #byte를 string으로 바꾸는 거
        file_link = dire + "/" + msg

        if os.path.exists(dire + "/" + msg):
                conn.sendall(str(os.path.getsize(file_link)).encode()) 

                with open(file_link, 'rb') as f:
                        data = f.read(os.path.getsize(file_link))
                        conn.sendall(data)
                print ("filesize : ", os.path.getsize(file_link))
        else:
                print("-1")



        

        

 
        conn.close()



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Echo server -p port")

    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-d', help="file_directory", required=True)



    args = parser.parse_args()

    run_server(port=int(args.p), dire = args.d)