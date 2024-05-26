import http.client
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class ProxyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length).decode('utf-8'))
        
        # Connect to the echo server
        conn = http.client.HTTPConnection(post_data['server_ip'], post_data['server_port'])
        conn.request("POST", "", json.dumps(post_data['message']), headers={"Content-Type": "application/json"})
        response = conn.getresponse()
        response_data = response.read()
        
        # Send the echo server's response back to the client
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response_data)

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8888), ProxyHandler)
    print("Proxy Server running on port 8888...")
    server.serve_forever()
