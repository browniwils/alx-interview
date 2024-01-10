#!/usr/bin/python3
"""Module for parsing log information and present it to standard output.
"""

import re


def valid_log(log_string):
    """Validate log inputs.
    """
    patt = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    req_info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(patt[0], patt[1], patt[2],
                                            patt[3], patt[4])
    match = re.fullmatch(log_format, log_string)
    if match is not None:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        req_info['status_code'] = status_code
        req_info['file_size'] = file_size
    return req_info


def display_log(file_size, status_stats):
    """Prints infofmation to standard output.
    """
    print('File size: {:d}'.format(file_size), flush=True)
    for status_code in sorted(status_stats.keys()):
        num = status_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, file_size, status_stats):
    """Update metrics of HTPP.
    """
    line_info = valid_log(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_stats.keys():
        status_stats[status_code] += 1
    return file_size + line_info['file_size']


def log_task():
    """Log parser.
    """
    line_num = 0
    file_size = 0
    status_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            file_size = update_metrics(
                line,
                file_size,
                status_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                display_log(file_size, status_stats)
    except (KeyboardInterrupt, EOFError):
        display_log(file_size, status_stats)


if __name__ == '__main__':
    log_task()
