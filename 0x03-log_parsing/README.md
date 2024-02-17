# 0x03. Log Parsing

This is a project that is part of the Holberton School curriculum. In this project, we are creating a script that parses logs.

This script parses logs from stdin and provides statistics about the logs.

The script reads logs line by line from the standard input.
Each log line is expected to have the following format:

    `<ip> - [<date>] "GET /projects/260 HTTP/1.1" <status> <size>`

Where:
    `<ip>` is the IP address of the client making the request.
    `<date>` is the date and time of the request.
    `<status>` is the HTTP status code of the response.
    `<size>` is the size of the response in bytes.

The script keeps track of the total size of all responses and the
number of occurrences of each recognized HTTP status code.
Recognized status codes are 200, 301, 400, 401, 403, 404, 405, and 500.

Every 10 lines, the script prints the total size so far and the
count of each recognized status code. If the script is interrupted
with a keyboard interrupt, it prints the current statistics before terminating.

This script uses regular expressions to parse the logs.
It uses a dictionary to keep track of the count of each status code.