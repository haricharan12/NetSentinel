import concurrent.futures
from subdomain_enumeration import enumerate_subdomains
from nmap_scanning import nmap_scan

if __name__ == "__main__":
    target_domain = input("Enter the target domain (e.g., example.com): ")
    wordlist = input("Enter the path to the wordlist file: ")
    target_ip = input("Enter the target IP address for Nmap scanning: ")
    output_file = "scan_results.txt"

    with concurrent.futures.ThreadPoolExecutor() as executor:
        subdomain_results = executor.submit(enumerate_subdomains, target_domain, wordlist)
        nmap_results = executor.submit(nmap_scan, target_ip)

        valid_subdomains = subdomain_results.result()
        nmap_scan_results = nmap_results.result()

        with open(output_file, 'a') as file:
            file.write("\nValid Subdomains:\n")
            for valid_subdomain in valid_subdomains:
                file.write(valid_subdomain + '\n')

            file.write("\nNmap scan results:\n")
            file.writelines(nmap_scan_results)

    print(f"All scans complete. Results saved to {output_file}")
