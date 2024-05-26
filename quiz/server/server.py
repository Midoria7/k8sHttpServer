from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class EchoHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(post_data)

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8080), EchoHandler)
    print("Echo Server running on port 8080...")
    server.serve_forever()
