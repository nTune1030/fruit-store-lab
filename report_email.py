#!/usr/bin/env python3

"""
Docstring for report_email

Import all the necessary libraries(os, datetime and reports) 
that will be used to process the text data from the 
supplier-data/descriptions directory into the format below:

name: Apple
weight: 500 lbs
[blank line]
name: Avocado
weight: 200 lbs
[blank line]

Once you have completed this, call the main method which will 
process the data and call the generate_report method from the reports module:
if __name__ == "__main__":

Pass the following arguments to the reports.generate_report method:
the text description processed from the text files as the paragraph argument.
the report title as the title argument.
the file path of the PDF to be generated as the attachment argument.

(use ‘/tmp/processed.pdf')
reports.generate_report(attachment, title, paragraph)

Once you define the generate_email and send_email methods,
call the methods under the main method after creating the PDF report:

Use the following details to pass the parameters to emails.generate_email():

From: automation@example.com
To: student@example.com
Subject line: Upload Completed - Online Fruit Store
E-mail Body: All fruits are uploaded to our website successfully. A detailed list is attached to this email.
Attachment: Attach the path to the file processed.pdf
"""