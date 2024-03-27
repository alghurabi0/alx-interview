#!/usr/bin/python3
""" log parsing """
import sys
import re
import signal


ctrl_c_pressed = False


def signal_handler(signal, frame):
    """ signal handler func """
    global ctrl_c_pressed
    ctrl_c_pressed = True


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
            line = line.split(" ")
            status = line[7]
            size = line[8]
            if status not in info:
                continue
            info[status] += 1
            info["file_size"] += int(size)
            count += 1
            if count == 10:
                count = 0
                print_info(info)
    except KeyboardInterrupt:
        if ctrl_c_pressed:
            print_info(info)


def print_info(info):
    """ helper pring func """
    print(f"File size: {info['file_size']}")
    if info['200'] != 0:
        print(f"200: {info['200']}")
    if info['301'] != 0:
        print(f"301: {info['301']}")
    if info['400'] != 0:
        print(f"400: {info['400']}")
    if info['401'] != 0:
        print(f"401: {info['401']}")
    if info['403'] != 0:
        print(f"403: {info['403']}")
    if info['404'] != 0:
        print(f"404: {info['404']}")
    if info['405'] != 0:
        print(f"405: {info['405']}")
    if info['500'] != 0:
        print(f"500: {info['500']}")


if __name__ == "__main__":
    """ main execution of code """
    main()
