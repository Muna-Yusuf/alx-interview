#!/usr/bin/python3
import sys
import signal

# Dictionary to hold the count of status codes
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
line_count = 0

def print_stats():
    global total_file_size, status_counts
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()

        # Check if the line format is correct
        if (len(parts) != 9 or parts[5] != '"GET' or
            parts[6] != '/projects/260' or parts[7] != 'HTTP/1.1"'):
            continue
        
        try:
            status_code = int(parts[8])
            file_size = int(parts[9])
        except (ValueError, IndexError):
            continue

        # Update metrics
        if status_code in status_counts:
            status_counts[status_code] += 1
        total_file_size += file_size
        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print_stats()
