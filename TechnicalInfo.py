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
