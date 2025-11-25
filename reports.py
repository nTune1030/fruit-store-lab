#!/usr/bin/env python3

"""
Fruit Store Report Generator
----------------------------
This script compiles processed fruit data into a PDF report using ReportLab.

Key Features:
- Scans for text descriptions in ~/supplier-data/descriptions/.
- Formats data into an HTML-compatible string (Name + Weight).
- Generates a PDF file named 'processed.pdf' with a title and summary.

Dependencies:
- reportlab: For PDF generation.
"""

import os
from datetime import date
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


DESC_PATH = os.path.expanduser("~") + "/supplier-data/descriptions/"
REPORT_FILE = "/tmp/processed.pdf"

def generate_report(filename: str, title: str, paragraph: str):
    """
    Builds and saves a PDF report using the ReportLab library.

    Args:
        filename (str): The full path where the PDF will be saved (e.g., /tmp/processed.pdf).
        title (str): The main heading text for the PDF document.
        paragraph (str): The body text of the PDF. This string supports basic HTML 
                         tags like <br/> for line breaks and <b> for bold text.

    Returns:
        None: This function prints a success message to stdout upon completion.
    """
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    story = []

    # Add Title (Uses the 'title' argument passed from main)
    story.append(Paragraph(title, styles["h1"]))
    story.append(Spacer(1, 12))

    # Add Body Text (Uses the 'paragraph' argument passed from main)
    story.append(Paragraph(paragraph, styles["Normal"]))

    # Build
    report.build(story)
    print(f"PDF generated successfully: {filename}")

def process_data():
    """
    Iterates through fruit description text files to compile a summary.

    This function looks for .txt files in the DESC_PATH directory. It reads
    the first two lines (Name and Weight) and formats them into a single 
    string suitable for the PDF body.

    Returns:
        str: A formatted string containing all fruit names and weights, 
             separated by HTML line break tags (<br/>).
             Example: "name: Apple<br/>weight: 500 lbs<br/><br/>..."
    """
    summary = ""

    # Check if the directory exists
    if not os.path.exists(DESC_PATH):
        return "No data found."
    
    files = [f for f in os.listdir(DESC_PATH) if f.endswith('.txt')]

    for file in files:
        with open(os.path.join(DESC_PATH, file), 'r') as f:
            lines = f.readlines()
            name = lines[0].strip()
            weight = lines[1].strip()

            # Construct the string with HTML line breaks
            summary += f"name: {name}<br/>weight: {weight}<br/><br/>"

    return summary

if __name__ == "__main__":
    pdf_body = process_data() # Get the data

    # Define the title with today's date
    today = date.today().strftime("%B %d, %Y")
    pdf_title = f"Processed Update on {today}"

    generate_report(REPORT_FILE, pdf_title, pdf_body)