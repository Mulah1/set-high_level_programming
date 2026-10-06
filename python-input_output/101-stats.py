#!/usr/bin/python3
"""Read stdin line by line and computes metrics."""

import sys


def print_stats(total_size, status_codes):
    """Print statistics.

    Args:
        total_size (int): Total file size
        status_codes (dict): Dictionary of status codes and their counts
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{}: {}".format(status_code, status_codes[status_code]))


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
                print()
        except (IndexError, ValueError):
            pass
except KeyboardInterrupt:
    print_stats(total_size, status_codes)
