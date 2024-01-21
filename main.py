import socket
import struct
import binascii
# from secret import interface

# MOVE THESE TO OTHER MODULE
https = 443

interface = "wlp2s0"
eth_length = 14



# EtherTypes
ethtypes = {
        2048    : "IPv4",
        2054    : "ARP"
}

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
            
            # unpacking ethernet header
            eth_header = packet[:eth_length]
            eth_header = struct.unpack("!6c6c2c", eth_header)

            # destination mac-address
            dest = []
            for a in eth_header[0:6]:
                a = int.from_bytes(a, "big")
                dest.append(hex(a).lstrip('0x'))
            dest = ':'.join(dest)

            # source mac-address
            source = []
            for a in eth_header[6:12]:
                a = int.from_bytes(a, "big")
                source.append(hex(a).lstrip('0x'))
            source = ':'.join(source)

            ethertype = int.from_bytes(packet[12:14], "big")
            ethertype = 40
            print(f'Destination MAC: {dest}')
            print(f'Source MAC: {source}')
            print(f'EtherType: {ethtypes[ethertype]}')
            print()
    except KeyboardInterrupt:
        print("\nParser stopped")
        exit()


if __name__ == "__main__":
    main()
