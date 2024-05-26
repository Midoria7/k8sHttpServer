import http.client
import json
import sys

def send_post_request(proxy_ip, proxy_port, server_ip, server_port, message):
    conn = http.client.HTTPConnection(proxy_ip, proxy_port)
    payload = {
        'server_ip': server_ip,
        'server_port': server_port,
        'message': message
    }
    conn.request("POST", "", json.dumps(payload), headers={"Content-Type": "application/json"})
    response = conn.getresponse()
    print(response.read().decode())

if __name__ == "__main__":
    proxy_ip = sys.argv[1]
    proxy_port = int(sys.argv[2])
    server_ip = sys.argv[3]
    server_port = int(sys.argv[4])
    message = sys.argv[5]
    send_post_request(proxy_ip, proxy_port, server_ip, server_port, message)
