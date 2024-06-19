#!/usr/bin/python3
"""Script that reads stdin line by line, parses the log format"""
import sys
import signal

total_size = 0
status_counts = {
        200: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
        }


def print_stats():
    """function prints the current stats"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def signal_handler(sig, frame):
    """to handel the signal"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

line_count = 0

for line in sys.stdin:
    parts = line.split()
    if len(parts) > 6:
        try:
            size = int(parts[-1])
            code = int(parts[-2])
            total_size += size
            if code in status_counts:
                status_counts[code] += 1
        except ValueError:
            continue
    line_count += 1
    if line_count % 10 == 0:
        print_stats()

print_stats()
