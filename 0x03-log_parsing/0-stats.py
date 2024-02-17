#!/usr/bin/python3
"""
This script parses logs from stdin and provides statistics about the logs.

The script reads logs line by line from the standard input.
Each log line is expected to have the following format:

    <ip> - [<date>] "GET /projects/260 HTTP/1.1" <status> <size>

Where:
    <ip> is the IP address of the client making the request.
    <date> is the date and time of the request.
    <status> is the HTTP status code of the response.
    <size> is the size of the response in bytes.

The script keeps track of the total size of all responses and the
number of occurrences of each recognized HTTP status code.
Recognized status codes are 200, 301, 400, 401, 403, 404, 405, and 500.

Every 10 lines, the script prints the total size so far and the
count of each recognized status code. If the script is interrupted
with a keyboard interrupt, it prints the current statistics before terminating.

This script uses regular expressions to parse the logs.
It uses a dictionary to keep track of the count of each status code.

This script does not take any command line arguments.
It reads the logs from standard input.
"""
import sys
import re


ip_pat = r".+"
date_pat = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\]"
status_pat = r".+"
size_pat = r"\d+"
pattern = re.compile((
    f'(?P<ip>{ip_pat})\\s?-\\s?(?P<date>{date_pat})'
    f' "GET /projects/260 HTTP/1.1" (?P<status>{status_pat})'
    f' (?P<size>{size_pat})'
))

recognized_codes = (200, 301, 400, 401, 403, 404, 405, 500)


def main():
    """The main function"""

    total_size = 0
    count = 0
    status_map = {}

    def print_stats():
        print(f"File size: {total_size}")
        for status in recognized_codes:
            if status not in status_map:
                continue
            print(f"{status}: {status_map[status]}")

    def process_line(line: str):
        nonlocal count, total_size

        match = pattern.match(line)
        if not match:
            return
        total_size += int(match["size"])
        try:
            status = int(match["status"])
            status_map.setdefault(status, 0)
            status_map[status] += 1
        except ValueError:
            pass
        count += 1

    while 1:
        if count == 10:
            print_stats()
            count = 0

        try:
            line = sys.stdin.readline()
            if not line:
                print_stats()
                break
            process_line(line)
        except KeyboardInterrupt:
            count = 0
            print_stats()
            raise


if __name__ == "__main__":
    main()
