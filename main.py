import requests
import json
from colorama import init, Fore, Style

# Initialize colorama
init()

try:
    # Fetch JSON data directly from the URL
    response = requests.get("https://raw.githubusercontent.com/likhonsible/Online-BDIX-Server-Tester/main/target.json")
    response.raise_for_status()
    targets = response.json()

    for host in targets.get("hosts", []):
        try:
            response = requests.get(host, timeout=1)
            response.raise_for_status()
            status = response.status_code
        except requests.exceptions.RequestException as e:
            status = 'error'
            
            continue

        if status == 200:
            time = response.elapsed.total_seconds()
            size = len(response.content)
            speed = (size * 8) / (time * 1000000)
            print(f"{Fore.GREEN}Host: {host} | Speed: {speed:.2f} Mbps{Style.RESET_ALL}\n")

        response.close()

except KeyboardInterrupt:
    print(f"\n{Fore.RED}Script terminated by user (Ctrl+C).{Style.RESET_ALL}")
except requests.exceptions.RequestException as e:
    print(f"{Fore.RED}Error fetching targets from the URL.{Style.RESET_ALL}")
