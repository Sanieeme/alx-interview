#!/usr/bin/python3


import sys
import signal

# Initialize variables
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Function to handle keyboard interruption (CTRL + C)
def handle_interrupt(signal, frame):
    print("\nProcess interrupted.")
    print_statistics()
    sys.exit(0)

# Function to print the statistics
def print_statistics():
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

# Attach the keyboard interrupt handler
signal.signal(signal.SIGINT, handle_interrupt)

# Read from stdin line by line
try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split(' ')
        
        # Ensure the line is in the correct format
        if len(parts) >= 6:
            try:
                # Extract relevant parts
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                # Check if status code is valid
                if status_code in status_codes:
                    total_file_size += file_size
                    status_codes[status_code] += 1
                    line_count += 1
                    
                    # Print statistics after every 10 lines
                    if line_count % 10 == 0:
                        print_statistics()
                        # Reset for the next batch of lines
                        total_file_size = 0
                        status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
                        line_count = 0
            except ValueError:
                # Skip lines where the file size or status code isn't an integer
                continue
except KeyboardInterrupt:
    # This block will catch keyboard interrupts gracefully
    print("\nProcess interrupted. Exiting.")
    print_statistics()
