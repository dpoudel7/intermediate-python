import requests
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

"""
Demonstrate basic HTTP requests using the requests library.
"""
print("HTTP REQUESTS DEMONSTRATION")
print("---------------------------")
print("HTTP is the foundation of web communication. Let's explore basic requests.\n")

# GET request - retrieving data
print("1. GET REQUEST (Retrieving Data)")
try:
    response = requests.get('https://httpbin.org/get')
    print(f"   Status Code: {response.status_code}")
    print(f"   Response headers: {dict(response.headers)}")
    print(f"   Response body: {response.text[:200]}...")  # First 200 chars
except Exception as e:
    print(f"   Error making GET request: {e}")
print()

# POST request - sending data
print("2. POST REQUEST (Sending Data)")
try:
    data = {'name': 'John Doe', 'company': 'Salesforce', 'role': 'Developer'}
    response = requests.post('https://httpbin.org/post', json=data)
    print(f"   Status Code: {response.status_code}")
    print(f"   Sent data: {data}")
    print(f"   Response body: {response.text[:200]}...")  # First 200 chars
except Exception as e:
    print(f"   Error making POST request: {e}")
print()

# PUT request - updating data
print("3. PUT REQUEST (Updating Data)")
try:
    data = {'id': 123, 'name': 'John Doe Updated', 'company': 'Salesforce', 'role': 'Senior Developer'}
    response = requests.put('https://httpbin.org/put', json=data)
    print(f"   Status Code: {response.status_code}")
    print(f"   Sent data: {data}")
    print(f"   Response body: {response.text[:200]}...")  # First 200 chars
except Exception as e:
    print(f"   Error making PUT request: {e}")
print()

# DELETE request - removing data
print("4. DELETE REQUEST (Removing Data)")
try:
    response = requests.delete('https://httpbin.org/delete')
    print(f"   Status Code: {response.status_code}")
    print(f"   Response body: {response.text[:200]}...")  # First 200 chars
except Exception as e:
    print(f"   Error making DELETE request: {e}")
print()

# Request with custom headers
print("5. REQUEST WITH CUSTOM HEADERS")
try:
    headers = {
        'User-Agent': 'Python HTTP Demo',
        'Authorization': 'Bearer fake-token-for-demo',
        'X-Custom-Header': 'Custom Value'
    }
    response = requests.get('https://httpbin.org/headers', headers=headers)
    print(f"   Status Code: {response.status_code}")
    print(f"   Sent headers: {headers}")
    print(f"   Response body: {response.text[:200]}...")  # First 200 chars
except Exception as e:
    print(f"   Error making request with custom headers: {e}")
print()

# Different status codes
print("6. HTTP STATUS CODES")
status_urls = {
    200: 'https://httpbin.org/status/200',  # OK
    404: 'https://httpbin.org/status/404',  # Not Found
    500: 'https://httpbin.org/status/500'   # Server Error
}

for status, url in status_urls.items():
    try:
        response = requests.get(url)
        print(f"   URL: {url}")
        print(f"   Expected Status: {status}, Actual Status: {response.status_code}")
    except Exception as e:
        print(f"   Error making request to {url}: {e}")
print()

# Common status code meanings
print("7. COMMON HTTP STATUS CODES")
status_codes = {
    "2xx - Success": {
        "200 OK": "Request succeeded",
        "201 Created": "Resource created successfully",
        "204 No Content": "Request succeeded but no content returned"
    },
    "3xx - Redirection": {
        "301 Moved Permanently": "Resource has been permanently moved",
        "302 Found": "Resource temporarily moved",
        "304 Not Modified": "Resource hasn't changed (used with caching)"
    },
    "4xx - Client Errors": {
        "400 Bad Request": "Invalid syntax in request",
        "401 Unauthorized": "Authentication required",
        "403 Forbidden": "Server understood but refuses (authorization)",
        "404 Not Found": "Resource doesn't exist"
    },
    "5xx - Server Errors": {
        "500 Internal Server Error": "Server encountered an error",
        "502 Bad Gateway": "Server as gateway received invalid response",
        "503 Service Unavailable": "Server temporarily unavailable"
    }
}

for category, codes in status_codes.items():
    print(f"   {category}")
    for code, description in codes.items():
        print(f"     {code}: {description}")
print()
