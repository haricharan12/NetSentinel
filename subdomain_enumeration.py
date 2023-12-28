import requests
from tqdm import tqdm
from utils import read_wordlist, log_error, REQUEST_TIMEOUT

def enumerate_subdomains(target_domain, wordlist):
    subdomains = read_wordlist(wordlist)
    valid_subdomains = []

    with tqdm(total=len(subdomains), desc="Subdomain Enumeration", unit="subdomain") as pbar:
        for subdomain in subdomains:
            full_url = f"http://{subdomain}.{target_domain}"
            try:
                response = requests.get(full_url, timeout=REQUEST_TIMEOUT)
                response.raise_for_status()

                if response.status_code < 400:
                    print(f"Valid subdomain: {full_url}")
                    valid_subdomains.append(full_url)

            except requests.RequestException as e:
                log_error(f"Error checking {full_url}: {e}")

            pbar.update(1)

    return valid_subdomains
