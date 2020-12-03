import pdfkit
import os


pdfkit.from_file('index.html', 'out.pdf', css='css.css')