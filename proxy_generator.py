import requests

# Example websites to scrape proxies from
urls = [
    "https://www.sslproxies.org/",
    "https://free-proxy-list.net/",
    "https://www.us-proxy.org/",
]

def fetch_proxies(url):
    response = requests.get(url)
    # Simple extraction example (needs customization per site)
    proxies = set()  # Use a set to avoid duplicates
    for line in response.text.splitlines():
        if 'td>' in line:
            parts = line.split('<td>')
            if len(parts) > 2:
                ip = parts[1].split('</td>')[0]
                port = parts[2].split('</td>')[0]
                proxies.add(f"{ip}:{port}")
    return proxies

all_proxies = set()
for url in urls:
    all_proxies.update(fetch_proxies(url))

# Save the proxies to a file
with open('proxies.txt', 'w') as file:
    for proxy in all_proxies:
        file.write(proxy + '\n')

print(f"Fetched {len(all_proxies)} unique proxies.")
