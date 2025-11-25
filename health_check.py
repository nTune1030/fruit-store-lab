#!/usr/bin/env python3

"""
System Health Monitor
---------------------
Checks system resources (CPU, Disk, RAM, Network) and sends an alert email
if any metric exceeds critical thresholds.

Thresholds:
- CPU Usage: > 80%
- Disk Space: < 20% free
- Memory: < 100MB available
- Network: Localhost must resolve to 127.0.0.1
"""

import shutil
import psutil
import socket
import os
import emails  # local emails.py module

# --- CONFIGURATION ---
SENDER = "automation@example.com"
USER = os.environ.get('USER') # Dynamically get the user
RECIPIENT = f"{USER}@example.com"
BODY = "Please check your system and resolve the issue as soon as possible."

def check_cpu_usage():
    """Returns True if CPU usage is over 80%"""
    # Interval=1 blocks for 1 second to calculate the average usage
    usage = psutil.cpu_percent(interval=1)
    return usage > 80

def check_disk_usage():
    """Returns True if available disk space is less than 20%"""
    du = shutil.disk_usage("/")
    percent_free = (du.free / du.total) * 100
    return percent_free < 20

def check_memory_usage():
    """Returns True if available memory is less than 100MB"""
    # available is in bytes. 100MB = 100 * 1024 * 1024
    limit = 100 * 1024 * 1024
    mem = psutil.virtual_memory()
    return mem.available < limit

def check_localhost():
    """Returns True if localhost cannot be resolved to 127.0.0.1"""
    try:
        localhost = socket.gethostbyname('localhost')
        return localhost != "127.0.0.1"
    except:
        return True

def main():
    checks = [
        (check_cpu_usage, "Error - CPU usage is over 80%"),
        (check_disk_usage, "Error - Available disk space is less than 20%"),
        (check_memory_usage, "Error - Available memory is less than 100MB"),
        (check_localhost, "Error - localhost cannot be resolved to 127.0.0.1")
    ]

    # Iterate through the checks
    for check_func, error_subject in checks:
        if check_func():
            print(f"⚠️ Alert Triggered: {error_subject}")
            
            # Create the email
            # Pass 'None' for attachment_path, emails.py handles
            email = emails.generate_email(
                sender=SENDER, 
                recipient=RECIPIENT, 
                subject=error_subject, 
                body=BODY, 
                attachment_path=None
            )
            
            emails.send_email(email)
            print(f"✅ Email sent to {RECIPIENT}")

if __name__ == "__main__":
    main()