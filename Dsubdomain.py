import requests
from tqdm import tqdm

import pyfiglet


ascii_banner = pyfiglet.figlet_format("Sub-Domain")
print(ascii_banner)
print("-->                          -->                         -->Im D")

def enumerate_subdomains(domain):
    subdomains = []

   
    with open("wordlist.txt", "r") as file:
        payload_count = sum(1 for line in file)
        file.seek(0) 
        for line in tqdm(file, total=payload_count, desc="Enumerating Subdomains"):
            subdomain = line.strip()
            url = f"https://{subdomain}.{domain}"  
            try:
                response = requests.get(url , timeout=5)
                print(f"Attempting URL: {url} - Status Code: {response.status_code}")
                if response.status_code < 400:
                    subdomains.append(url)
            except requests.ConnectionError:
                pass

    return subdomains

if __name__ == "__main__":
    try:
        target_domain = input("Enter target domain: ")
        discovered_subdomains = enumerate_subdomains(target_domain)

        print("Discovered subdomains:")
        for subdomain in discovered_subdomains:
            print(subdomain)
    except KeyboardInterrupt: 
        print("\nProgram interrupted by Ctrl+C. Exiting...")
