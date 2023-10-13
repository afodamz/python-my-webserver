import http.server
import socketserver

# Set the port on which you want to run the server
port = 8000

# Create a custom handler to serve HTML and JavaScript files
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'  # Default page
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create the server with the custom handler
with socketserver.TCPServer(("", port), CustomHandler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()















