from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()
    # header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    pdf.line(10,21,200,21)
    # lines
    for i in range(26):
        pdf.ln(10)
        pdf.line(10, 31 + i*10, 200, 31+i*10)
    # footer
    pdf.ln(5)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

    for i in range(row['Pages']-1):
        pdf.add_page()
        # lines
        for i in range(27):
            pdf.ln(10)
            pdf.line(10, 21 + i * 10, 200, 21 + i * 10)
        # footer
        pdf.ln(7)
        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

pdf.output("output.pdf")