#!/usr/bin/python3
"""Module for parsing log information and present it to standard output.
"""

import re


def valid_log(log_string):
    """Validate log inputs.
    """
    patt = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] "GET \/projects\/260 HTTP\/1\.1" \d{3} \d+'
    return re.match(patt, log_string)

def display_log(**kwargs):
    """Prints infofmation to standard output.
    """
    for key in kwargs.keys():
        if not isinstance(kwargs.get(key), dict):
            print("File Size {}".format(kwargs.get(key)))
        else:
            for nested_k, nested_v in key.items():
                print(f"{nested_k}: {nested_v}")

def log_task():
    """Log parser.
    """
    while True:
        try:
            status_codes = {
                "200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0

            }
            size = 0
            for time in range(11):
                info = input("").strip()
                if valid_log(info):
                    info_list = info.split(" ")
                    fize_size = info_list[-1]
                    s_code = info_list[-2]
                    status_codes[s_code] = status_codes.get(s_code) + 1
                    size += int(fize_size)
                    sorted_keys_dict = {code: status_codes[code] for code in sorted(status_codes)}
            display_log(codes=sorted_keys_dict, size = size)
        except KeyboardInterrupt:
            display_log(codes=sorted_keys_dict, size = size)


if __name__ == '__main__':
    log_task()
