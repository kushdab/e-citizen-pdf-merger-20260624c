# eCitizen Kenya PDF Merger (2026)

This CLI tool allows users to merge multiple eCitizen Kenya PDF documents (like ID copies, KRA PINs, Business Registration certificates) into a single file while applying a professional digital stamp to every page for tracking or verification purposes.

## Features
- Merges multiple PDF files in the specified order.
- Automatically adds a timestamped "ECITIZEN CERTIFIED COPY" stamp to the bottom right of every page.
- Lightweight and fast.

## Installation
1. Ensure you have Python 3.8+ installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
```bash
python merge.py doc1.pdf doc2.pdf -o merged_output.pdf -s "OFFICIAL COPY"
```

### Arguments
- `inputs`: List of PDF files to merge.
- `-o`, `--output`: Name of the resulting file (Default: `eCitizen_Merged_Document.pdf`).
- `-s`, `--stamp`: Custom text to display on the stamp.