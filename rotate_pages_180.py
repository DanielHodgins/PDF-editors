#!/usr/bin/env python3
"""
Rotate all pages in a PDF file by 180 degrees.
"""

import sys
from PyPDF2 import PdfReader, PdfWriter


def rotate_pages_180(input_pdf, output_pdf):
    """
    Rotate all pages in the input PDF by 180 degrees and save to output PDF.
    
    Args:
        input_pdf: Path to the input PDF file
        output_pdf: Path to save the output PDF file
    """
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    total_pages = len(reader.pages)
    print(f"Total pages in input PDF: {total_pages}")
    print("Rotating all pages 180 degrees...")
    
    # Rotate each page by 180 degrees
    for i in range(total_pages):
        page = reader.pages[i]
        page.rotate(180)
        writer.add_page(page)
        print(f"Rotated page {i + 1}")
    
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)
    
    print(f"\nOutput saved to: {output_pdf}")
    print(f"All {total_pages} pages rotated 180 degrees")


def main():
    if len(sys.argv) != 3:
        print("Usage: python rotate_pages_180.py <input.pdf> <output.pdf>")
        print("Example: python rotate_pages_180.py input.pdf output.pdf")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    
    try:
        rotate_pages_180(input_pdf, output_pdf)
    except FileNotFoundError:
        print(f"Error: Input file '{input_pdf}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
