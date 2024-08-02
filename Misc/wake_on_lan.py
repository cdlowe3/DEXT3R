import wakeonlan

def send_wol(mac_address):
    
    wakeonlan.send_magic_packet(mac_address)
    print(f"Send WOL packet to {mac_address}")

if __name__ =="__main__":
    mac_address = ''
    send_wol(mac_address)