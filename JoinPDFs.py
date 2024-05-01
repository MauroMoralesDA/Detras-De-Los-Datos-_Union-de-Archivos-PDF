import os
import PyPDF2

def merge_pdfs_in_directory(directory, output_filename):
    pdf_writer = PyPDF2.PdfWriter()
    files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    files.sort()  # Optional: sort the file names

    for filename in files:
        filepath = os.path.join(directory, filename)
        pdf_reader = PyPDF2.PdfReader(filepath)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)
    print(f'Merged PDF saved as {output_filename}')

if __name__ == '__main__':
    # Directory containing PDFs
    directory = r'C:\Users\DELL\Desktop\Facturas'
    # Output merged PDF
    output_filename = r'C:\Users\DELL\Desktop\Facturas\merged_output.pdf'
    merge_pdfs_in_directory(directory, output_filename)
