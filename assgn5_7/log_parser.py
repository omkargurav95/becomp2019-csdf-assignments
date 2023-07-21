import time

LOG_FILE = "access_log.txt"
THRESHOLD_REQUESTS = 10
TIME_WINDOW_SECONDS = 60 * 5

def detect_ddos():
    ip_request_count = {}
    current_time = int(time.time())

    # Read the log file and parse the timestamps and IP addresses
    with open(LOG_FILE, 'r') as f:
        for line in f:
            log_entry = line.strip().split(" - ")
            if len(log_entry) == 2:
                timestamp_str, ip_address = log_entry
                timestamp = int(time.mktime(time.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")))
                if current_time - timestamp <= TIME_WINDOW_SECONDS:
                    ip_request_count[ip_address] = ip_request_count.get(ip_address, 0) + 1

    # Check for potential DDoS attacks
    for ip, request_count in ip_request_count.items():
        if request_count > THRESHOLD_REQUESTS:
            print(f"Possible DDoS detected from {ip} with {request_count} requests.")
            # Add your DDoS mitigation actions here, e.g., blocking the IP address, alerting, etc.

if __name__ == "__main__":
    detect_ddos()
