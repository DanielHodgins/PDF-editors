# PDF-editors
This is a repository of python scripts to fix common issues with PDFs.
Later this month (December 2025), I plan to make it into a nice app and wanted to have this current form as a checklist of things to add.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Scripts

### 1. Remove Odd Pages (`remove_odd_pages.py`)
Removes all odd-numbered pages from a PDF (keeps pages 2, 4, 6, 8, etc.).

**Usage:**
```bash
python remove_odd_pages.py input.pdf output.pdf
```

### 2. Remove Even Pages (`remove_even_pages.py`)
Removes all even-numbered pages from a PDF (keeps pages 1, 3, 5, 7, etc.).

**Usage:**
```bash
python remove_even_pages.py input.pdf output.pdf
```

### 3. Remove Every Nth Page (`remove_nth_pages.py`)
Removes every nth page from a PDF. For example, with n=7, it removes pages 7, 14, 21, 28, etc.

**Usage:**
```bash
python remove_nth_pages.py input.pdf output.pdf <n>
```

**Example:**
```bash
python remove_nth_pages.py input.pdf output.pdf 7
```

### 4. Rotate Pages 180 Degrees (`rotate_pages_180.py`)
Rotates all pages in a PDF by 180 degrees.

**Usage:**
```bash
python rotate_pages_180.py input.pdf output.pdf
```

## Requirements

- Python 3.6+
- PyPDF2 3.0.0+
