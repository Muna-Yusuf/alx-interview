#!/usr/bin/python3
import sys
import signal

# Initialize statistics
total_file_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_counter = 0

def print_stats():
    """Print the current statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def sig_handler(sig, frame):
    """Handle the keyboard interrupt (CTRL + C) to print stats."""
    print_stats()
    sys.exit(0)

# Register signal handler for keyboard interrupt
signal.signal(signal.SIGINT, sig_handler)

# Process each line from standard input
for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 7:
            continue
        
        # Extract necessary parts
        request = parts[5] + ' ' + parts[6] + ' ' + parts[7]
        status_code = parts[8]
        file_size = parts[9]
        
        # Validate format
        if not request.startswith('"GET /projects/260 HTTP/1.1"'):
            continue
        
        # Update total file size
        total_file_size += int(file_size)
        
        # Update status counts
        if status_code.isdigit():
            code = int(status_code)
            if code in status_counts:
                status_counts[code] += 1
        
        # Increment line counter
        line_counter += 1
        
        # Print stats after every 10 lines
        if line_counter % 10 == 0:
            print_stats()
    
    except Exception:
        continue

# Print final statistics
print_stats()
