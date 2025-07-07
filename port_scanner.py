import socket
import csv
from datetime import datetime

target = input("Enter Target IP Address (e.g. 192.168.56.101): ")

ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389]
filename = f"scan_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Port", "Status"])

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        status = "Open" if result == 0 else "Closed"
        print(f"Port {port}: {status}")
        writer.writerow([port, status])
        sock.close()

print(f"\n Scan complete! Results saved in {filename}")
