import socket
import sys
from datetime import datetime

def get_ip(target_ip: str):
    try:
        ip = socket.gethostbyname(target_ip)
        print(f"Scanning the target IP: {ip}")
        return ip
    except socket.gaierror:
        print("Hostname could not be resolved")
        return None
    except socket.error:
        print("Could not connect to the server")
        return None

def post_scan(ip):
    try:
        print("-" * 50)
        print(f"Scanning Target: {ip}")
        print(f"Scanning started at: {datetime.now()}")
        print("-" * 50)

        for port in range(1, 65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((ip, port))

            if result == 0:
                print(f"Port {port} is Open - {format(port)}")
            sock.close()

    except KeyboardInterrupt:
        print("Exiting program")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()
    except socket.error:
        print("Could not connect to the server")
        sys.exit()


if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")
    ip = get_ip(target)

    if ip:
        post_scan(ip)
