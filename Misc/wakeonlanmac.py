import socket
import struct

def send_magic_packet(mac_address, broadcast_ip='255.255.255.255', port=9):
    # Normalize MAC address
    mac_address = mac_address.replace(':', '').replace('-', '').upper()
    if len(mac_address) != 12 or not all(c in '0123456789ABCDEF' for c in mac_address):
        raise ValueError("Invalid MAC address format")

    # Create magic packet
    magic_packet = b'\xFF' * 6 + (bytes.fromhex(mac_address) * 16)
    
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic_packet, (broadcast_ip, port))
        print(f"Magic packet sent to {mac_address} via {broadcast_ip}:{port}")

if __name__ == "__main__":
    # Replace with the MAC address of the target machine
    target_mac = 'xx:xx:xx:xx:xx:xx'
    
    # Optionally, you can specify a different broadcast IP or port
    send_magic_packet(target_mac)
