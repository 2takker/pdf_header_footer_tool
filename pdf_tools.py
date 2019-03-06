import tkinter
from tkinter.filedialog import askopenfilename
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import A4

def choose_pdf_path() -> 'pdf_path': 
    """Prompts user to choose a pdf to read. Returns path"""
    tkinter.Tk().withdraw() 
    filename = askopenfilename() 
    return filename

def generate_header(left_text:str='', middle_text='', right_text=''):
    """Generates a pdf contraining specified header"""
    width, height = A4

    can = canvas.Canvas('header.pdf', pagesize=A4)
    can.drawString(x=0.075*width, y=0.97*height, text=left_text)
    can.drawCentredString(x=0.5*width, y=0.97*height, text=middle_text)
    can.drawRightString(x=0.925*width, y=0.97*height, text=right_text)

    # This might be used later, rather than saving a pdf file each time
    #can.getpdfdata()  

    can.save()


if __name__ == "__main__":
    #choose_pdf_path()
    generate_header('left', 'middle', 'right')
    