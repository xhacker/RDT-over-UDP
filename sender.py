from socket import socket, AF_INET, SOCK_DGRAM
from sys import argv
from common import ip_checksum

SEGMENT_SIZE = 200

if __name__ == "__main__":
    dest_addr = argv[1]
    dest_port = int(argv[2])
    dest = (dest_addr, dest_port)
    listen_addr = argv[3]
    listen_port = int(argv[4])
    listen = (listen_addr, listen_port)
    filename = argv[5]

    with open(filename) as f:
        content = f.read()

    send_sock = socket(AF_INET, SOCK_DGRAM)
    recv_sock = socket(AF_INET, SOCK_DGRAM)

    recv_sock.bind(listen)

    offset = 0

    while offset < len(content):
        if offset + SEGMENT_SIZE > len(content):
            segment = content[offset:]
        else:
            segment = content[offset:offset + SEGMENT_SIZE]
        offset += SEGMENT_SIZE

        ack_received = False
        while not ack_received:
            send_sock.sendto(ip_checksum(segment) + segment, dest)

            message, address = recv_sock.recvfrom(4096)
            print message
            if message == "ACK":
                ack_received = True
