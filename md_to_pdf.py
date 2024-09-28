import markdown
import pdfkit

input_md_file_path = 'data/StatOasis/md/StatOasis_1.md'
output_pdf_file_path = 'data/StatOasis/pdf/StatOasis_1.pdf'

# Read the Markdown content
with open(input_md_file_path, 'r', encoding='utf-8') as f:
    markdown_text = f.read()

# Convert Markdown to HTML
html_text = markdown.markdown(markdown_text)

wkhtmltopdf = r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# Configure pdfkit to use wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf)



# Convert HTML to PDF
pdfkit.from_string(html_text, output_pdf_file_path, configuration=config)
