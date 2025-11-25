# Fruit Store Automation System 🍎 🍋 🍇

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Status](https://img.shields.io/badge/Status-Complete-green)

This project is an **ETL (Extract, Transform, Load) Automation Pipeline** designed to update an online fruit store's catalog. It processes raw supplier data (images and text), uploads it to a production Django web server via REST API, generates PDF reports, and sends email notifications to stakeholders.

It also includes a system health monitoring daemon to alert administrators of high CPU/RAM usage or network failures.

---

## 🏗️ Architecture & Workflow

The system handles the data lifecycle through four distinct modules:


1.  **Image Processing:** Converts large `.TIFF` files into web-friendly `.JPEG` format (600x400px).
2.  **Data Upload:** Parses unstructured text descriptions into structured JSON and uploads to a Django API.
3.  **Reporting:** Generates a PDF summary of the uploaded inventory and emails it to the supplier.
4.  **Monitoring:** Runs background health checks on system resources.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Image Manipulation:** `Pillow` (PIL)
* **Web/API:** `requests` (REST API interaction)
* **Reporting:** `reportlab` (PDF Generation)
* **Email:** `smtplib`, `email.message`
* **System Ops:** `psutil`, `shutil`, `os`

---

## 📂 Project Structure

| Script | Description |
| :--- | :--- |
| `changeImage.py` | Iterates through supplier images, converts RGBA to RGB, resizes to 600x400, and saves as JPEG. |
| `supplier_image_upload.py` | Uploads the processed JPEG images to the web server's `/upload/` endpoint. |
| `run.py` | Parses product description `.txt` files into a Python dictionary (JSON payload) and POSTs them to the `/fruits/` API endpoint. |
| `report_email.py` | Generates a PDF summary of the new fruit catalog (`processed.pdf`) and emails it as an attachment. |
| `health_check.py` | Checks CPU usage (>80%), Disk space (<20%), and Memory (<500MB). Sends an email alert if critical. |

---

## 🚀 Setup & Usage

### 1. Prerequisites
Ensure you have the required libraries installed. It is recommended to use a **Virtual Environment**.

```bash
pip install requests pillow reportlab psutil
```

### 2. Environment Variables
To send emails securely (without hardcoding passwords), this project relies on environment variables:

```
export EMAIL_USER="your_email@gmail.com"
export EMAIL_PASS="your_app_password" # Generated via Google App Passwords
```

### 3. Running the Pipeline  
#### Step 1: Process Images
```bash
./changeImage.py
```
#### Step 2: Upload Images
```bash
./supplier_image_upload.py
```
#### Step 3: Upload Descriptions
```bash
./run.py
```
#### Step 4: Generate Report & Email
```bash
./report_email.py
```

---

## 🩺 System Health Check

The `health_check.py` script is designed to run as a background process (cron job) to monitor server stability.
```bash
# Run manually
./health_check.py

# Example Cron Job (Runs every minute)
* * * * * /path/to/health_check.py
```

---

## 📜 Context

This project was built as the **Capstone** for the **Google IT Automation with Python Professional Certificate**. It simulates a real-world scenario involving legacy data migration and cloud operations.
