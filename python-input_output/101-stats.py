#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics for HTTP logs.
"""
import sys


def print_stats(size, status_codes):
    """
    Prints accumulated metrics regarding total size and status code
    frequencies.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    size = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()

            try:
                size += int(data[-1])
            except (IndexError, ValueError):
                pass

            try:
                code = data[-2]
                if code in status_codes:
                    status_codes[code] += 1
            except IndexError:
                pass

            if count % 10 == 0:
                print_stats(size, status_codes)

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
