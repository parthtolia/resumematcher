from pdf_parser import extract_text_from_pdf

text = extract_text_from_pdf("resumes/Mayuri Buran.pdf")
print(text[:500])