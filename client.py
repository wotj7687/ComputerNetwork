import socket

import argparse



def run(host, port, fi):


    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as s:

        s.connect((host, port))  ## 상대방 IP주소, 상대방 port 번호

        s.sendall(fi.encode()) ##  string을 byte로 바꾸는 거

        resp = s.recv(30)
        
        filesize = int(resp.decode())

        data = s.recv(filesize)

        with open(fi, 'wb') as f:
                f.write(data)
        print("filesize : ", filesize)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Echo client -p port -i host")

    parser.add_argument("-p", help = "port_number", required = True)

    parser.add_argument("-i", help="host_name", required=True)

    parser.add_argument('-f', help="File_name", required = True)



    args = parser.parse_args()

    run(host=args.i, port=int(args.p), fi = args.f)