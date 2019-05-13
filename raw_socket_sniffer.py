import os
import socket
import argparse
import struct

ETH_P_ALL = 0x0003
ETH_SIZE = 14


def make_ethernet_header(raw_data):
    ether = struct.unpack('!6B6BH', raw_data)
    return {'dst': '%02x:%02x:%02x:%02x:%02x:%02x' % ether[:6],
            'src': '%02x:%02x:%02x:%02x:%02x:%02x' % ether[6:12],
            'ether_type': ether[12]}


# to define IP length
def check_ip_length(raw_data):
    ip_len = struct.unpack('!B', raw_data)
    ip_version = ip_len[0] / 16
    header_length = (ip_len[0] % 16) * 4
    print("\nIP HEADER")
    print("[version] %d" % ip_version)
    print("[header_length] %d" % header_length)
    return header_length


# We don't need to return all value just print them.
def make_ip_header(raw_data):
    head_ip = struct.unpack('!BHHHBBH4B4B', raw_data)
    print("[tos] %d" % head_ip[0])
    print("[total_length] %d" % head_ip[1])
    print("[identification] %d" % head_ip[2])
    print("[flag] %d" % (head_ip[3] >> 13))
    print("[offset] %d" % int(head_ip[3] ^ 0x1fff))
    print("[ttl] %d" % head_ip[4])
    print("[protocol] %d" % head_ip[5])
    print("[checksum] %d" % head_ip[6])
    print("[source_ip] %d.%d.%d.%d" % (head_ip[7], head_ip[8], head_ip[9], head_ip[10]))
    print("[destination_ip] %d.%d.%d.%d\n" % (head_ip[11], head_ip[12], head_ip[13], head_ip[14]))


def dumpcode(buf):
    print("%7s" % "offset", end='')

    for i in range(0, 16):
        print("%02x " % i, end='')

        if not (i % 16 - 7):
            print("- ", end='')

    print("")

    for i in range(0, len(buf)):
        if not i % 16:
            print("0x%04x" % i, end=' ')

        print("%02x" % buf[i], end=' ')

        if not (i % 16 - 7):
            print("- ", end='')

        if not (i % 16 - 15):
            print(" ")

    print("")


def sniffing(nic):
    if os.name == 'nt':
        address_familiy = socket.AF_INET
        protocol_type = socket.IPPROTO_IP
    else:
        address_familiy = socket.AF_PACKET
        protocol_type = socket.ntohs(ETH_P_ALL)

    with socket.socket(address_familiy, socket.SOCK_RAW, protocol_type) as sniffe_sock:
        sniffe_sock.bind((nic, 0))

        if os.name == 'nt':
            sniffe_sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            sniffe_sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        data, _ = sniffe_sock.recvfrom(65535)
        ethernet_header = make_ethernet_header(data[:ETH_SIZE])

        # ipv4 --> 0800 = 2048
        if ethernet_header['ether_type'] == 2048:

            for item in ethernet_header.items():
                print('{0}:{1}'.format(item[0], item[1]))

            ip_length = check_ip_length(data[ETH_SIZE:ETH_SIZE + 1])
            ip_header = make_ip_header(data[ETH_SIZE + 1:ETH_SIZE + ip_length])  # HOW TO SET?? -OK

            print("Raw Data")
            dumpcode(data)
        else:
            print("This is Not IP_PACKET")

        if os.name == 'nt':
            sniffe_sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


if __name__ == '__main__':
    repeater = 1
    while True:
        parser = argparse.ArgumentParser(description='This is a simple packet sniffer')
        parser.add_argument('-i', type=str, required=True, metavar='NIC name', help='NIC name')
        args = parser.parse_args()
        print("\n[%d] IP_PACKET" % a)
        sniffing(args.i)
        repeater = repeater + 1