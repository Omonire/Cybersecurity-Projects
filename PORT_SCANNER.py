import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...\n")
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except:
            pass

    if open_ports:
        print(f"Open Ports: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    target = input("Enter Target IP or Host: ").strip()
    port_range = input("Enter Port Range (e.g. 20-100): ").strip()

    try:
        start_port, end_port = map(int, port_range.split("-"))
        scan_ports(target, start_port, end_port)
    except:
        print("[ERROR] Invalid port range format.")
