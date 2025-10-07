import PyPDF2

with open("encrypted.pdf", "rb") as f:
    reader = PyPDF2.PdfReader(f)
    print(reader.is_encrypted)  # should print True
