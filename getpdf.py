import re
import codecs
import os

f = codecs.open('compiledxml.txt', 'r', encoding='utf-8')
fx = open('pdflinks.txt', 'w+', encoding='utf-8')

for line in f:

    all_pdfs = [x for x in line.split('http') if '.pdf' in x]

    for pdf in all_pdfs:
        fx.write(line.split("\t")[3] + "\t")

        pdf = pdf.split('"')
        pdf[0] = pdf[0].split('.pdf')
        fx.write("http" + pdf[0][0] + ".pdf\n")
