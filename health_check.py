#!/usr/bin/env python3

import shutil
import psutil


"""
Docstring for health_check

Import the necessary Python libraries (eg. shutil, psutil) to write this script.

Report an error if CPU usage is over 80%
Report an error if available disk space is lower than 20%
Report an error if available memory is less than 100MB
Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"

Complete the script to check the system statistics every 60 seconds, 
and in event of any issues detected among the ones mentioned above, 
an email should be sent with the following content:

From: automation@example.com
To: student@example.com
Subject line:
Case

Subject line

CPU usage is over 80%

Error - CPU usage is over 80%

Available disk space is lower than 20%

Error - Available disk space is less than 20%

available memory is less than 100MB

Error - Available memory is less than 100MB

hostname "localhost" cannot be resolved to "127.0.0.1"

Error - localhost cannot be resolved to 127.0.0.1

E-mail Body: Please check your system and resolve the issue as soon as possible.
Note: There is no attachment file here, so you must be careful 
while defining the generate_email() method in the emails.py script 
or you can create a separate generate_error_report() method for handling non-attachment email.
"""