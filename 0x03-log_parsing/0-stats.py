#!/usr/bin/python3
import sys
import signal

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) != 9:
            continue
        ip, dash, date, method, url, protocol, status, size = parts
        if method != '"GET' or url != '/projects/260' or protocol != 'HTTP/1.1"':
            continue
        status = int(status)
        size = int(size)
        total_size += size
        if status in status_counts:
            status_counts[status] += 1
    except Exception:
        continue
    line_count += 1
    if line_count % 10 == 0:
        print_stats()

print_stats()
