import socket

def scan_ports(target_ip, target_ports):
    open_ports = []

    for port in target_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)

            try:
                sock.connect((target_ip, port))
                open_ports.append(port)
            except (socket.timeout, socket.error):
                pass

    return open_ports

if __name__ == "__main__":
    target_ip = "target_ip"  # Ip Address here
    ports_to_scan = [53, 80,] # modify 

    open_ports = scan_ports(target_ip, ports_to_scan)

    if open_ports:
        print(f"Open ports on {target_ip}: {open_ports}")
    else:
        print(f"No open ports found on {target_ip}")
