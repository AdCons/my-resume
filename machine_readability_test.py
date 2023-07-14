from pypdf import PdfReader

reader = PdfReader("Adrian Constante_Resume.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
print(text)