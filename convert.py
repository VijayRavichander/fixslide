import fitz  # PyMuPDF
import re
import typer
from tqdm import tqdm
from pathlib import Path
from typing_extensions import Annotated 


def main(
    pdf_path: Path = typer.Argument(..., help="Path to the pdf file"),
    save_name: Annotated[Path, "o"] = typer.Option(
        None, help="Name of the output file"
    )
): 

    # Open the PDF document
    doc = fitz.open(pdf_path)

    # Dictionary to store pages with valid numbers
    valid_pages = {}

    prev_num = 1
    # Iterate through each page in the document
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)  # Get the page
        width, height = page.rect.width, page.rect.height

        # Define the bottom-left corner
        crop_box_left = fitz.Rect(0, height * 0.9, width * 0.05, height)

        # Extract text from the bottom-left corner
        text = page.get_text("text", clip=crop_box_left)
        text = text.strip()
        if text == "":
            text = str(prev_num)
        else:
            prev_num = int(re.sub(r'[^0-9]', '', text)) + 1 

        valid_pages[text] = page_num + 1

    # Print the kept page numbers and their last occurrences
    for page_number, slide_number in valid_pages.items():
        print(f"Page Number: {page_number} on Slide Number: {slide_number}")


    # Create a new PDF document
    new_pdf = fitz.open()

    # Add valid pages to the new PDF
    for page_number, slide_number in valid_pages.items():
        slide_number = int(slide_number) - 1
        new_pdf.insert_pdf(doc, from_page=slide_number, to_page=slide_number)  # Copy only the valid page

    # Save the new PDF file
    new_pdf.save(save_name)
    new_pdf.close()

if __name__ == "__main__":
    typer.run(main)