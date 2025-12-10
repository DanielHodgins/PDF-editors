#!/usr/bin/env python3
"""
Remove every nth page from a PDF file.
For example, with n=7, removes pages 7, 14, 21, 28, etc.
"""

import sys
from PyPDF2 import PdfReader, PdfWriter


def remove_nth_pages(input_pdf, output_pdf, n):
    """
    Remove every nth page from the input PDF and save to output PDF.
    
    Args:
        input_pdf: Path to the input PDF file
        output_pdf: Path to save the output PDF file
        n: Remove every nth page (e.g., 7 removes pages 7, 14, 21...)
    """
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    total_pages = len(reader.pages)
    print(f"Total pages in input PDF: {total_pages}")
    print(f"Removing every {n}th page...")
    
    removed_pages = []
    
    # Add pages to writer, skipping every nth page
    for i in range(total_pages):
        page_number = i + 1
        # Check if this is an nth page (7, 14, 21, etc.)
        if page_number % n == 0:
            removed_pages.append(page_number)
            print(f"Removing page {page_number}")
        else:
            writer.add_page(reader.pages[i])
    
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)
    
    print(f"\nOutput saved to: {output_pdf}")
    print(f"Pages in output: {len(writer.pages)}")
    print(f"Removed pages: {removed_pages}")


def main():
    if len(sys.argv) != 4:
        print("Usage: python remove_nth_pages.py <input.pdf> <output.pdf> <n>")
        print("Example: python remove_nth_pages.py input.pdf output.pdf 7")
        print("  (This removes pages 7, 14, 21, 28, etc.)")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    
    try:
        n = int(sys.argv[3])
        if n <= 0:
            print("Error: n must be a positive integer")
            sys.exit(1)
    except ValueError:
        print("Error: n must be a valid integer")
        sys.exit(1)
    
    try:
        remove_nth_pages(input_pdf, output_pdf, n)
    except FileNotFoundError:
        print(f"Error: Input file '{input_pdf}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
