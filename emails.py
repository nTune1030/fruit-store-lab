#!/usr/bin/env python3

"""
emails.py
---------
Handles creating and sending emails.
"""

import email.message
import mimetypes
import os
import smtplib

def generate_email(sender: str, recipient: str, subject: str, body: str, attachment_path=None):
    """Creates an EmailMessage object with correct MIME types."""
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if attachment_path:
        # Use 'os.path.basename' (Safer than split)
        attachment_filename = os.path.basename(attachment_path)
        
        # Guess the correct MIME type (e.g., 'application/pdf')
        mime_type, _ = mimetypes.guess_type(attachment_path)
        
        # Fallback if not recognized
        if mime_type is None:
            mime_type = 'application/octet-stream'
            
        # Split 'application/pdf' into 'application' and 'pdf'
        main_type, sub_type = mime_type.split('/', 1)

        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                                   maintype=main_type,
                                   subtype=sub_type,
                                   filename=attachment_filename)
    
    return message

def send_email(message):
    """Sends the message to the configured SMTP server."""
    # In the lab, this connects to localhost.
    # If running locally on WSL to test, you'd use your GMail settings here.
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()