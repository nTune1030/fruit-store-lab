#!/usr/bin/env python3

"""
report_email.py
---------------
The 'Manager' script. It coordinates:
1. reports.py -> To generate the PDF.
2. emails.py  -> To send the PDF via email.
"""

import os
import datetime
import reports
import emails

def main():
    # Configuration
    SENDER = "automation@example.com"
    
    # Dynamic User Retrieval
    USER = os.environ.get('USER')
    RECIPIENT = f"{USER}@example.com"
    SUBJECT = "Upload Completed - Online Fruit Store"
    BODY = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    ATTACHMENT_PATH = "/tmp/processed.pdf"

    print("Generating PDF...")
    
    # process_data function from reports.py module
    summary_paragraph = reports.process_data()
    
    today = datetime.date.today().strftime("%B %d, %Y")
    title = f"Processed Update on {today}"
    
    reports.generate_report(ATTACHMENT_PATH, title, summary_paragraph)

    print(f"Sending Email to {RECIPIENT}...")
    
    # Email object using emails.py module
    message = emails.generate_email(
        sender=SENDER,
        recipient=RECIPIENT,
        subject=SUBJECT,
        body=BODY,
        attachment_path=ATTACHMENT_PATH
    )
    
    emails.send_email(message)
    print("✅ Email sent successfully.")

if __name__ == "__main__":
    main()