#!/usr/bin/python3
"""
A  script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one, the line is skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:

Total file size: File size: <total size>

where <total size> is the sum of all previous <file size>

Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer,
does not print anything for this status code

format: <status code>: <number>
status codes is printed in ascending order
"""

import sys

if __name__ == '__main__':

    """Initialize file size and line count"""
    filesize, count = 0, 0

    """Status codes to track"""
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    """Define function to print statistics"""
    def print_stats(stats: dict, file_size: int) -> None:
         """Prints the accumulated file size and count of each status code."""
        print("File size: {:d}".format(filesize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        """Process each line of input from stdin"""
        for line in sys.stdin:
            count += 1
            data = line.split()

            """Update status code count if present in stats"""
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass

            """Add to file size if data is present"""
            try:
                filesize += int(data[-1])
            except BaseException:
                pass

            """Print stats every 10 lines"""
            if count % 10 == 0:
                print_stats(stats, filesize)

        """ Print final stats after processing """
        print_stats(stats, filesize)

    except KeyboardInterrupt:
        """Print stats if interrupted"""
        print_stats(stats, filesize)
        """Re-raise exception to terminate the program"""
        raise
