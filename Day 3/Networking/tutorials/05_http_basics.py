import requests
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

# Create a simple HTTP server
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    A simple HTTP request handler that demonstrates a basic HTTP server.
    """
    def do_GET(self):
        """Handle GET requests."""
        # Parse the path to get query parameters
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        if path == '/':
            # Serve a basic HTML page
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Python HTTP Server Demo</title>
            </head>
            <body>
                <h1>Hello from Python HTTP Server!</h1>
                <p>This is a simple demonstration of a Python HTTP server.</p>
            </body>
            </html>
            """
            
            self.wfile.write(html.encode('utf-8'))
            
        elif path == '/api/data':
            # Serve some JSON data
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            data = {
                "message": "This is data from the API",
                "items": ["apple", "banana", "orange"],
                "count": 3
            }
            
            self.wfile.write(json.dumps(data).encode('utf-8'))
            
        else:
            # Handle 404 Not Found
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Resource not found'.encode('utf-8'))
    
    def do_POST(self):
        """Handle POST requests."""
        path = self.path
        
        if path == '/api/submit':
            # Get the content length to read the body
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            # Try to parse as JSON
            try:
                json_data = json.loads(post_data)
                response_data = {
                    "status": "success",
                    "message": "Data received",
                    "data": json_data
                }
                
                self.send_response(201)  # Created
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response_data).encode('utf-8'))
                
            except json.JSONDecodeError:
                # Not valid JSON
                self.send_response(400)  # Bad Request
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                error_response = {
                    "status": "error",
                    "message": "Invalid JSON data"
                }
                
                self.wfile.write(json.dumps(error_response).encode('utf-8'))
        else:
            # Endpoint not found
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Resource not found'.encode('utf-8'))

def run_http_server(port=8000):
    """Run a simple HTTP server on the specified port."""
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Starting HTTP server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down server...")
        httpd.server_close()

if __name__ == "__main__":
    # For demonstration, call the function that showcases HTTP requests

    # To run the HTTP server (uncomment to use):
    run_http_server(8000)
    # 
    # You can then access:
    # - http://localhost:8000/ for HTML page
    # - http://localhost:8000/api/data for JSON data
    # - POST to http://localhost:8000/api/submit with JSON body