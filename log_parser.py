# log_parser.py
# Simple log parser for error detection

logfile = "/var/log/messages"

print("Parsing log file:", logfile)

error_keywords = ["error", "failed", "critical", "panic"]

with open(logfile, "r") as f:
    for line in f:
        if any(keyword in line.lower() for keyword in error_keywords):
            print("ERROR FOUND:", line.strip())
