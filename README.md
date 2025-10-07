# 🔒 PDF Protection Tool Using Python

## 📘 Overview
The **PDF Protection Tool** is a Python-based project that allows users to add **password protection** to existing PDF files.  
It demonstrates the use of file handling, encryption, and command-line arguments in Python, providing a practical understanding of how to secure sensitive documents programmatically.

---

## 🎯 Objective
To develop a Python script that:
- Accepts an existing PDF file as input  
- Applies password encryption  
- Saves the new file as a protected PDF  

---

## 🧠 Key Concepts Covered
- **File Handling** (Reading and writing files in binary mode)
- **Functions and Arguments**
- **Exception Handling**
- **Command-Line Arguments (`sys.argv`)**
- **Working with PDFs using PyPDF2**
- **Encryption for Document Security**

---

## ⚙️ How It Works
1. The user provides:
   - Input PDF file name  
   - Output (protected) PDF file name  
   - Password for encryption  

2. The script:
   - Reads the input PDF in binary mode  
   - Copies all pages to a new PDF  
   - Applies password protection using PyPDF2  
   - Saves the encrypted version as a new file  

3. Any errors (missing file, invalid PDF, etc.) are handled gracefully using `try/except`.

---

## 🧩 Project Structure
📂 PDF-Protection-Tool
┣ 📜 pdf_protector.py # Main script
┣ 📄 example.pdf # Sample PDF for testing
┗ 📘 README.md # Project documentation


---

## 🧰 Prerequisites
Make sure you have **Python 3.x** installed on your system.  
Install the required library before running the script:

```bash
pip install PyPDF2

🚀 How to Run the Project

Place your unprotected PDF (e.g., example.pdf) in the same directory as the script.

Open a terminal in that directory.

Run the following command:

python pdf_protector.py input.pdf output.pdf yourpassword

✅ Example:
python pdf_protector.py example.pdf protected.pdf mypass123


After running, a new file protected.pdf will be created — open it, and you’ll be asked to enter the password.

🧾 Sample Output
✅ Encrypted file saved as protected.pdf


If there’s an issue:

❌ Error: File 'example.pdf' not found.

🧠 How Password Protection Works

The script uses PyPDF2.PdfReader to read existing PDFs.

PyPDF2.PdfWriter is used to create a new file and add pages.

The encrypt(password) function applies password-based encryption to the new file.

Once saved, the output PDF requires the password to open.

🧰 Technologies Used
Tool / Library	Purpose
Python 3	Programming language
PyPDF2	Reading and encrypting PDF files
sys	Handling command-line arguments
🧩 Error Handling

The script gracefully manages:

FileNotFoundError: Input file doesn’t exist

PdfReadError: Invalid or corrupted PDF

Other unexpected errors

This ensures smooth execution and user feedback.

🌟 Expected Learning Outcomes

By completing this project, you will:

Understand file handling and binary data in Python

Learn PDF manipulation using PyPDF2

Understand basic encryption and decryption concepts

Gain confidence in building command-line Python tools
