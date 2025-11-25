#!/usr/bin/env python3


"""
Docstring for emails

Define generate_email and send_email methods by importing necessary libraries.
"""

from email.message import EmailMessage
import smtplib


def generate_email(sender, recipient, subject, body, attachment_path=None):
    """Creates an EmailMessage object.

    Args:
        sender (str): The sender's email address.
        recipient (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body of the email.
        attachment_path (str, optional): The path to an attachment file. Defaults to None.

    Returns:
        EmailMessage: The created EmailMessage object.
    """
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if attachment_path:
        attachment_filename = attachment_path.split('/')[-1]
        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                                   maintype='application',
                                   subtype='octet-stream',
                                   filename=attachment_filename)
    return message


def send_email(message):
    """Sends the given EmailMessage object.

    Args:
        message (EmailMessage): The EmailMessage object to send.
    """
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
