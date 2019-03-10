import tkinter
from tkinter.filedialog import askopenfilename
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import A4, letter
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

def choose_pdf_path() -> 'pdf_path': 
    """Prompts user to choose a pdf to read. Returns path"""
    tkinter.Tk().withdraw() 
    filename = askopenfilename() 
    return filename

def generate_header(left_text='', 
                    middle_text='', 
                    right_text=''):
    """Generates a pdf contraining specified header"""
    width, height = letter

    can = canvas.Canvas('header.pdf', pagesize=letter)
    can.drawString(x=0.075*width, y=0.96*height, text=left_text)
    can.drawCentredString(x=0.5*width, y=0.96*height, text=middle_text)
    can.drawRightString(x=0.925*width, y=0.96*height, text=right_text)

    # This might be used later, rather than saving a pdf file each time
    #can.getpdfdata()  

    can.save()

def generate_footer(left_text='', 
                    middle_text='', 
                    right_text=''):
    """Generates a pdf contraining specified footer"""
    width, height = letter

    can = canvas.Canvas('footer.pdf', pagesize=letter)
    can.drawString(x=0.075*width, y=0.03*height, text=left_text)
    can.drawCentredString(x=0.5*width, y=0.03*height, text=middle_text)
    can.drawRightString(x=0.925*width, y=0.03*height, text=right_text)

    # This might be used later, rather than saving a pdf file each time
    #can.getpdfdata()  

    can.save()

def merge_pdf(target_pdf, header='header.pdf', footer=None):
    pdf_writer = PdfFileWriter()

    header_page = PdfFileReader(header).getPage(0)
    if footer is not None:
        footer_page = PdfFileReader(footer).getPage(0)

    for page in range(target_pdf.getNumPages()):
        current_page = target_pdf.getPage(page)
        current_page.mergePage(header_page)
        if footer is not None:
            current_page.mergePage(footer_page)
        pdf_writer.addPage(current_page)
    
    with open('merged.pdf', 'wb') as fh:
        pdf_writer.write(fh)

    

if __name__ == "__main__":
    #choose_pdf_path()
    generate_header('Bjarke Hansen', 'ID', '4 pages')
    generate_footer('left', 'middle', 'right')
    target_pdf = PdfFileReader('Hand_in_2019.pdf')
    merge_pdf(target_pdf)
    