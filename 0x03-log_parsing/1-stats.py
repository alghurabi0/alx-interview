#!/usr/bin/python3
""" log parsing """
import sys
import re
import signal


info = {
        "file_size": 0,
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }


def signal_handler(signal, frame):
    """ signal handler func """
    print_info(info)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def main():
    """ log parsing problem """
    regex = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] "GET /projects/260 HTTP/1\.1" \d+ \d+$'  # noqa
    info = {
        "file_size": 0,
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    count = 0
    try:
        for line in sys.stdin:
            line = line.strip()
            if not re.match(regex, line):
                continue
            parts = line.split(" ")
            status = parts[7]
            size = parts[8]
            if not status.isdigit() or status not in info:
                continue
            info[status] += 1
            info["file_size"] += int(size)
            count += 1
            if count == 10:
                print_info(info)
                count = 0
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)


def print_info(info):
    """ helper print func """
    print(f"File size: {info['file_size']}")
    for c, count in info.items():
        if c.isdigit() and int(c) in [200, 301, 400, 401, 403, 404, 405, 500]:
            print(f"{c}: {count}")


if __name__ == "__main__":
    """ main execution of code """
    main()
