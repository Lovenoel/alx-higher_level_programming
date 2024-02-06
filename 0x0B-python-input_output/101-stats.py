#!/usr/bin/python3
"""A module a script that reads stdin line by line and
computes metrics
"""
import sys


def print_stats(total_size, status_codes):
    """Prints the statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    """Parses a log line and returns file size and status code."""
    tokens = line.split()
    if len(tokens) >= 8:
        return int(tokens[-1]), int(tokens[-2])
    return 0, 0

if __name__ == "__main__":
    line_count = 0
    total_size = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            line_count += 1
            size, status = parse_line(line)
            total_size += size

            if status in status_codes:
                status_codes[status] += 1
            else:
                status_codes[status] = 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
