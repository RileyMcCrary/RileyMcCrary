from fpdf import FPDF

#what to put on the shirt
user = input("Name: ")
text = user + " took CS50"


pdf = FPDF()
pdf.add_page()
pdf.set_margin(0)
pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png")
pdf.set_font("helvetica", "B", 20)
pdf.set_text_color(255, 255, 255)
pdf.cell(150, -275, text, align='R')
pdf.output("shirtificate.pdf")
