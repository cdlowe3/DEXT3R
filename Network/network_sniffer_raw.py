import socket
import struct

def unpack_ipv4_header(packet):
    """
    Unpack IPv4 header to get protocol information.
    """
    ip_header = packet[0:20]
    ip_header_unpacked = struct.unpack('!BBHHHBBH4s4s', ip_header)
    protocol = ip_header_unpacked[6]
    return protocol

def unpack_tcp_header(packet):
    """
    Unpack TCP header to get port information.
    """
    tcp_header = packet[20:40]
    tcp_header_unpacked = struct.unpack('!HHLLBBHHH', tcp_header)
    source_port = tcp_header_unpacked[0]
    destination_port = tcp_header_unpacked[1]
    return source_port, destination_port

def process_packet(packet):
    """
    Process the packet to extract HTTP and DNS requests.
    """
    protocol = unpack_ipv4_header(packet)
    
    if protocol == 6:  # TCP
        source_port, destination_port = unpack_tcp_header(packet)
        
        if destination_port == 80:
            payload = packet[40:]
            try:
                http_data = payload.decode('utf-8', errors='ignore')
                if 'Host:' in http_data:
                    lines = http_data.split('\r\n')
                    for line in lines:
                        if line.startswith('Host:'):
                            host = line.split(' ')[1]
                            print(f"HTTP Host: {host}")
            except Exception as e:
                pass
    
    if protocol == 17:  # UDP
        udp_header = packet[20:28]
        udp_header_unpacked = struct.unpack('!HHHH', udp_header)
        source_port = udp_header_unpacked[0]
        destination_port = udp_header_unpacked[1]
        
        if destination_port == 53:
            payload = packet[28:]
            try:
                dns_data = payload.decode('utf-8', errors='ignore')
                if 'A' in dns_data:
                    print(f"DNS Query: {dns_data}")
            except Exception as e:
                pass

def start_sniffing(interface):
    """
    Start sniffing packets on the specified network interface.
    """
    try:
        # Create a raw socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        sock.bind(('0.0.0.0', 0))
        
        # Set the socket to promiscuous mode
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        
        while True:
            packet = sock.recvfrom(65565)[0]
            process_packet(packet)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Network Packet Sniffer")
    parser.add_argument('-i', '--interface', required=True, help="Network interface to sniff on (e.g., eth0, wlan0)")

    args = parser.parse_args()
    start_sniffing(args.interface)
