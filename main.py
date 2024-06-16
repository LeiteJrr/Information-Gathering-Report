from TechnicalInfo import get_tech_info
from PortScan import port_scan
from SubDomains import subdomain_scan_results

# webscraper.io
# hackthissite.org
target = input("What webpage would you like to investigate?: \n"
               "(Use the format 'example.com')\n"
               "> ")

filename = "Target Summary.pdf"
with open(filename, 'w') as f: # write data to file

    
    # scan for technical info and store results
    tech_scan_report = get_tech_info(target)

    if tech_scan_report:  
        f.write("\nTechnical Information:\n")
        for info in tech_scan_report:
            f.write(f"{info}.\n")
    else:
        f.write("No technical information found.\n")


    # scan ports and store the results
    port_scan_report = port_scan(target) 

    if port_scan_report:  
        f.write("\nOpen Ports:\n")
        for port, service in port_scan_report.items():
            f.write(f"Port {port} ({service}) is open.\n")
    else:
        f.write("No open ports found.\n")


    # scan subdomains and store results
    subdomain_scan_report = subdomain_scan_results(target)

    if subdomain_scan_report:
        f.write("\nSubdomains:\n")
        f.write(subdomain_scan_report["message"] + "\n")  # Write scan message
        if "subdomains" in subdomain_scan_report:  # Check if subdomains exist
            for subdomain in subdomain_scan_report["subdomains"]:
                f.write(f"{subdomain}\n")
        else:
            f.write("No subdomains found.\n")
    else:
        f.write(f"Error: {subdomain_scan_report['message']}\n")
