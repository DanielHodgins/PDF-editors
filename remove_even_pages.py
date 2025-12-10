#!/usr/bin/env python3
"""
Remove even-numbered pages from a PDF file.
Keeps pages 1, 3, 5, 7, etc. (odd page numbers)
"""

import sys
from PyPDF2 import PdfReader, PdfWriter


def remove_even_pages(input_pdf, output_pdf):
    """
    Remove even-numbered pages from the input PDF and save to output PDF.
    
    Args:
        input_pdf: Path to the input PDF file
        output_pdf: Path to save the output PDF file
    """
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    total_pages = len(reader.pages)
    print(f"Total pages in input PDF: {total_pages}")
    
    # Keep odd-numbered pages (index 0, 2, 4... which are pages 1, 3, 5...)
    for i in range(0, total_pages, 2):
        writer.add_page(reader.pages[i])
        print(f"Keeping page {i + 1}")
    
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)
    
    print(f"Output saved to: {output_pdf}")
    print(f"Pages in output: {len(writer.pages)}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python remove_even_pages.py <input.pdf> <output.pdf>")
        print("Example: python remove_even_pages.py input.pdf output.pdf")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    
    try:
        remove_even_pages(input_pdf, output_pdf)
    except FileNotFoundError:
        print(f"Error: Input file '{input_pdf}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
