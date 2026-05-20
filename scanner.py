import socket
from colorama import Fore, init

# Initialize colorama
init()

# Banner
print(Fore.CYAN + """
========================================
      ADVANCED NETWORK SCANNER
========================================
""")

# Target Input
target = input(Fore.YELLOW + "Enter Target IP or Domain: ")

# Common Ports
ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389]

print(Fore.BLUE + f"\n[+] Scanning Target: {target}\n")

# Scanning Logic
for port in ports:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(Fore.GREEN + f"[OPEN] Port {port}")
    else:
        print(Fore.RED + f"[CLOSED] Port {port}")

    s.close()

print(Fore.CYAN + "\n[✓] Scan Completed Successfully.")
