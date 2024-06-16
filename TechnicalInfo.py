# Code program for technical information -- Liam, Johnny, Maryam

# Written by Maryam and Liam

import socket
import dns.resolver
import ping3

def check_ip_and_domain(target):
    try:
        ip_address = socket.gethostbyname(target)
        domain_name = socket.gethostbyaddr(ip_address)[0]
        return ip_address, domain_name
    except socket.gaierror:
        return "Invalid target", None

# gets DNS record for target site
!pip install dnspython

import socket
import dns.resolver

def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None

def get_dns_servers(domain):
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        return [str(rdata) for rdata in answers]
    except dns.resolver.NXDOMAIN:
        return None

# URL to pull DNS servers from
url = "https://webscraper.io/test-sites"
domain = url.split("//")[1].split("/")[0]

print(f"Gathering information for: {domain}")

# Get IP address
ip = get_ip(domain)
if ip:
    print(f"IP Address: {ip}")
else:
    print("IP Address: Not found")

# Get DNS servers
dns_servers = get_dns_servers(domain)
if dns_servers:
    print("DNS Servers:")
    for server in dns_servers:
        print(f" - {server}")
else:
    print("DNS Servers: Not found")
Collecting dnspython
  Downloading dnspython-2.6.1-py3-none-any.whl (307 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 307.7/307.7 kB 2.2 MB/s eta 0:00:00
Installing collected packages: dnspython
Successfully installed dnspython-2.6.1
Gathering information for: webscraper.io
IP Address: 18.172.134.35
DNS Servers:
 - ns-1178.awsdns-19.org.
 - ns-1975.awsdns-54.co.uk.
 - ns-43.awsdns-05.com.
 - ns-799.awsdns-35.net.
def get_dns_records(domain): #### not sure if it is working correctly #####
    records = {}
    try:
        answers = dns.resolver.resolve(domain, 'A')
        records['A'] = [str(r) for r in answers]
        
        answers = dns.resolver.resolve(domain, 'MX')
        records['MX'] = [str(r.exchange) for r in answers]
        
        answers = dns.resolver.resolve(domain, 'NS')
        records['NS'] = [str(r) for r in answers]
        
        return records
    except dns.resolver.NoAnswer:
        return "No DNS records found for the domain"
    except dns.resolver.NXDOMAIN:
        return "Domain does not exist"

def is_online(target):
  # checks if target site is online
  try:
    ping3.ping(target)
    return True
  except Exception:
    return False

def get_tech_info(Target):
    target = Target
    ip_address, domain_name = check_ip_and_domain(target)

    results = []
    if domain_name:
        IP = (f"IP Address of {target}: {ip_address}")
        results.append(IP)
        DNS = f"Domain Name of {target}: {domain_name}"
        results.append(DNS)

        # Check online status using ping3
        if is_online(target):
            results.append(f"{target} is online")
        else:
            results.append(f"{target} is offline")

        # Get DNS records
        dns_records = get_dns_records(domain_name)
        if isinstance(dns_records, str):
            results.append(dns_records)
        else:
            for record_type, values in dns_records.items():
                results.append(f"\n{record_type} records: {', '.join(values)}")

    else:
        results.append("Invalid target entered.") 

    return results
