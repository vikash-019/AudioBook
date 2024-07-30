import pyttsx3
import PyPDF2
from PyPDF2 import PdfReader
pdf = PdfReader(open('chapter1.pdf', 'rb'))
number_of_pages = len(pdf.pages)
print(number_of_pages)
speaker = pyttsx3.init()
from PyPDF2 import PdfReader
with open('chapter1.pdf', 'rb') as file:
    pdf = PdfReader(file)
    page = pdf.pages[12]
    text = page.extract_text()
    print(text)
speaker.say(text)
speaker.runAndWait()