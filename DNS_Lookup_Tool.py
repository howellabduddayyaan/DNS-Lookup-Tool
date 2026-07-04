# =======================
# === DNS Lookup Tool ===
# =======================

import socket

print("\n=======================")
print("=== DNS Lookup Tool ===")
print("=======================")

domain = input("\nEnter a domain (e.g. google.com): ")

# _________________________________________________________________________________________________

try:

    ip_address = socket.gethostbyname(domain)

    print("\n=== DNS Information ===\n")

    print(f"Domain Name : {domain}")
    print(f"IP Address  : {ip_address}")
    
except socket.gaierror:
    print("\nError: Unable to detect the domain")
    
# _________________________________________________________________________________________________