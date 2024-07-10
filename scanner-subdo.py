import requests
from concurrent.futures import ThreadPoolExecutor

# Function to read subdomains from a file
def read_subdomains(filename):
    with open(filename, 'r') as file:
        subdomains = [line.strip() for line in file]
    return subdomains

def is_subdomain_alive(domain, subdomain, timeout=5):
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            return url
    except requests.ConnectionError:
        pass
    except requests.Timeout:
        print(f"Timeout for {url}")
    return None

def scan_subdomains(domain, subdomains, timeout=5):
    alive_subdomains = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(is_subdomain_alive, domain, subdomain, timeout) for subdomain in subdomains]
        for future in futures:
            result = future.result()
            if result:
                alive_subdomains.append(result)
    return alive_subdomains

if __name__ == "__main__":
    domain = input("Masukkan domain Anda: ")
    subdomains = read_subdomains('subdomains-10000.txt')
    print(f"Memindai subdomain untuk {domain}...\n")
    alive_subdomains = scan_subdomains(domain, subdomains)
    if alive_subdomains:
        print("Subdomain yang aktif ditemukan:")
        for subdomain in alive_subdomains:
            print(subdomain)
    else:
        print("Tidak ada subdomain yang aktif ditemukan.")
