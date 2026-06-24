import argparse
import os
from datetime import datetime
from io import BytesIO
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red

def create_stamp_overlay(text):
    """Creates a temporary PDF in memory with the stamp text."""
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica-Bold", 10)
    can.setStrokeColor(red)
    can.setFillColor(red)
    # Position: Bottom Right corner
    can.drawString(400, 20, f"{text} | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    can.save()
    packet.seek(0)
    return PdfReader(packet)

def merge_and_stamp(input_pdfs, output_path, stamp_text):
    """Merges PDFs and applies a stamp to every page."""
    writer = PdfWriter()
    stamp_pdf = create_stamp_overlay(stamp_text)
    stamp_page = stamp_pdf.pages[0]

    print(f"[*] Processing {len(input_pdfs)} files...")

    for pdf_path in input_pdfs:
        if not os.path.exists(pdf_path):
            print(f"[!] Warning: File {pdf_path} not found. Skipping.")
            continue
        
        try:
            reader = PdfReader(pdf_path)
            for page in reader.pages:
                # Apply the stamp overlay to the page
                page.merge_page(stamp_page)
                writer.add_page(page)
            print(f"[+] Added: {pdf_path}")
        except Exception as e:
            print(f"[!] Error processing {pdf_path}: {e}")

    if len(writer.pages) > 0:
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        print(f"[SUCCESS] Documents merged and stamped into: {output_path}")
    else:
        print("[ERROR] No pages were processed. Output file not created.")

def main():
    parser = argparse.ArgumentParser(
        description="eCitizen Kenya PDF Merger & Stamper - 2026 Edition"
    )
    parser.add_argument(
        "inputs", 
        nargs="+", 
        help="Input PDF files to merge (e.g., id.pdf pin.pdf business.pdf)"
    )
    parser.add_argument(
        "-o", "--output", 
        default="eCitizen_Merged_Document.pdf", 
        help="Output filename (default: eCitizen_Merged_Document.pdf)"
    )
    parser.add_argument(
        "-s", "--stamp", 
        default="ECITIZEN CERTIFIED COPY", 
        help="Custom stamp text"
    )

    args = parser.parse_args()

    # Basic validation
    valid_files = [f for f in args.inputs if f.lower().endswith('.pdf')]
    if not valid_files:
        print("[ERROR] No valid PDF files provided.")
        return

    merge_and_stamp(valid_files, args.output, args.stamp)

if __name__ == "__main__":
    main()