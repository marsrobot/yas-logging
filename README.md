# yas-logging
Yet Another Structured Logging for Python

## Requirements
- A Python logging framework supports logging structured information
- It enriches the logging with code line, process ID, thread ID, user, environment, etc.
- Its API is compatible with Python logging interface.

## Usage
- Clone the code
- Add the directory yas-logging to PYTHONPATH
- Run python3 yas_logging_demo.py for testing

## Sample Output
[TIME] [HOSTNAME]:[USERNAME] [LOGGERNAME:*INFO*] Hello World debug */yas-logging/examples/yas_logging_demo.py:32 [PROCESSID]:[THRADID]
[TIME] [HOSTNAME]:[USERNAME] [LOGGERNAME:*INFO*] Hello World info */yas-logging/examples/yas_logging_demo.py:33 [PROCESSID]:[THRADID]
[TIME] [HOSTNAME]:[USERNAME] [LOGGERNAME:*ERROR*] Hello World error: division by zero */yas-logging/examples/yas_logging_demo.py:37 [PROCESSID]:[THRADID]
