import socket
import struct
import binascii
# from secret import interface

# MOVE THESE TO OTHER MODULE
https = 443

interface = "wlp2s0"

def main():
    # @todo 
    # create error handling
    # look into ntohs 


    
    # create raw socket
    mysocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))


    # set network interface mode to promiscuous
    mysocket.bind((interface, 0))

    try:
        while True:
            # recieve packet
            packet = mysocket.recvfrom(65535)
            packet = packet[0]
            eth_length = 14

            eth_header = packet[:eth_length]
            eth_header = struct.unpack("!6c6c2c", eth_header)
            dest = []
            for a in eth_header[0:6]:
                a = int.from_bytes(a, "big")
                dest.append(hex(a).lstrip('0x'))
            print(':'.join(dest))
            print()
    except KeyboardInterrupt:
        print("\nParser stopped")
        exit()


if __name__ == "__main__":
    main()
