import nmap
from utils import log_error

def nmap_scan(target_ip):
    nm = nmap.PortScanner()

    try:
        nm.scan(target_ip, arguments='-p 1-1024 -sV --open')
    except nmap.PortScannerError as e:
        log_error(f"Nmap scanning error: {e}")
        return []

    results = []
    for host in nm.all_hosts():
        results.append(f"Host: {host} ({nm[host].hostname()})\n")
        results.append(f"State: {nm[host].state()}\n")

        for proto in nm[host].all_protocols():
            results.append(f"Protocol: {proto}\n")

            lport = nm[host][proto].keys()
            for port in sorted(lport):
                service = nm[host][proto][port]
                results.append(f"Port: {port}\tState: {service['state']}\tService: {service['name']}\n")

    return results
