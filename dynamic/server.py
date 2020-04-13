from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/test":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello, world!')    
        elif self.path == "/home":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'home')
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'hi')
        
        
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()