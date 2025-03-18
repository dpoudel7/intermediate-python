import requests

# Example URL (replace with actual URL in training)
url = "https://www.maxi.rs/online/Smrznuti-proizvodi/c/06"

# TODO: Basic GET request
# Show proper headers setup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

# Make request with proper error handling
response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()

# Print the source code
print(response.text)