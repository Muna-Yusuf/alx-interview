#!/usr/bin/python3
import sys
import signal

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    parts = line.split()
    if len(parts) < 9:
        continue

    try:
        ip = parts[0]
        date = parts[3][1:] + " " + parts[4][:-1]
        method = parts[5][1:]
        endpoint = parts[6]
        protocol = parts[7][:-1]
        status_code = int(parts[8])
        file_size = int(parts[9])
        
        if method != "GET" or endpoint != "/projects/260" or protocol != "HTTP/1.1":
            continue
        
        total_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1
        
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
    except Exception:
        continue

print_stats()
