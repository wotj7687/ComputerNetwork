## client.py

import socket
import argparse

def run(host, port, st):
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as s:
        s.connect((host, port))  ## 상대방 IP주소, 상대방 port 번호
        s.sendall(st.encode())
        resp = s.recv(1024)
        print(resp.decode())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo client -p port -i host")
    parser.add_argument("-p", help = "port_number", required = True)
    parser.add_argument("-i", help="host_name", required=True)
    parser.add_argument('-s', help="String", required = True)

    args = parser.parse_args()
    run(host=args.i, port=int(args.p), st = args.s)