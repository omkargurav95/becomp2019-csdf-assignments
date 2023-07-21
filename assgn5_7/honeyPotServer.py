from http.server import BaseHTTPRequestHandler, HTTPServer
import time

LOG_FILE = "access_log.txt"

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Get the client IP address from the request headers
        client_ip = self.client_address[0]

        # Get the current timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # Log the client IP address and timestamp to the file
        with open(LOG_FILE, "a") as f:
            log_entry = f"{timestamp} - {client_ip}\n"
            f.write(log_entry)

        # Send a response back to the client
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Request received successfully.")

def run_server(server_class=HTTPServer, handler_class=RequestHandler, port=9000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print("\nServer stopped.")

if __name__ == "__main__":
    run_server()
