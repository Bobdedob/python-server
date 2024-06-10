```python
# Import the HTTP server module
import http.server

# Define the handler for the server
class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    pass

# Create and start the server
server_address = ('', 8000)  # You can change the port number if needed
httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
print('Server running at http://localhost:8000')
httpd.serve_forever()
