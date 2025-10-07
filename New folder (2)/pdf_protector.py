import sys       
import PyPDF2

"""  We use sys.argv to handle command-line arguments dynamically.
This lets users specify different files and passwords each time. """


def create_password_protected_pdf(input_pdf, output_pdf, password):
    try:
        # Open the original PDF in binary read mode
        with open(input_pdf, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()

            # Copy all pages from reader to writer
            for page in reader.pages:
                writer.add_page(page)

            # Encrypt the new PDF
            writer.encrypt(password)

            # Write to the output file
            with open(output_pdf, "wb") as output:
                writer.write(output)

        print(f"✅ Encrypted file saved as {output_pdf}")

    except FileNotFoundError:
        print(f"❌ Error: File '{input_pdf}' not found.")
    except PyPDF2.errors.PdfReadError:
        print("❌ Error: Invalid or corrupted PDF file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

""" 🔸 with open(..., "rb") and "wb"

"rb" means read binary — PDFs are binary files, not plain text.

"wb" means write binary — to write the new encrypted PDF.

🔸 PdfReader and PdfWriter

PdfReader reads existing PDFs.

PdfWriter creates new PDFs or modifies existing ones.

🔸 writer.add_page(page)

Copies each page into the new (protected) PDF.

🔸 writer.encrypt(password)

Adds encryption so a password is required to open the new file.

🔸 try/except

Prevents crashes if files are missing, corrupted, or unreadable """

def main():
    if len(sys.argv) != 4:
        print("Usage: python pdf_protector.py <input_pdf> <output_pdf> <password>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]

    create_password_protected_pdf(input_pdf, output_pdf, password)

""" Why sys.argv?

Makes the script flexible (works with any file)

Avoids hardcoding paths/passwords """

if __name__ == "__main__":
    main()

""" It ensures that your script runs only when executed directly —
not when imported in another file. """



""" 
Advanced Enhancements 

Future Improvements:

Feature 	               Description	                      Implementation
GUI                    ADD a Tkinter interface	            Use tkinter.filedialog
Batch Encryption	   Encrypt multiple PDFs	            Loop through file list
Dual Passwords	       Add user & owner passwords	        writer.encrypt(user_pwd, owner_pwd)
Stronger Encryption	    Use pikepdf for AES-256	            Advanced option
Drag & Drop	              Use PyQt5 GUI	                    User-friendly desktop tool """