# Problem statement: Write a function to parse a log file & extract details of Errors & Warnings
# recorded into a separate file.
import re

# opening input log file in read mode
with open("session.log", "r") as log_file:
    # opening output log file in write mode
    with open("error_warning.log", "w") as new_file:
        for line in log_file:
            if re.search(r'(Error|Warning)', line, re.I):
                # writing lines which contains errors/warnings to output file
                new_file.write(line)