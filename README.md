# Fix Slides

<!-- warning -->
> **Warning:** Made explicitly for CSCI 544 - [Applied Natural Language Processing](https://swabhs.com/f24-csci544-appliednlp/)

This Python script is a command-line tool for extracting slides from a PDF presentation. It uses the PyMuPDF library to identify and extract the unique pages that likely represent individual slides in a presentation.

## Prerequisites

Before using this tool, ensure you have the following dependencies installed:

- Python 3.x
- PyMuPDF (also known as Fitz)
- Typer
- tqdm

You can install the necessary dependencies using `pip`. For example:

```bash
pip install PyMuPDF typer tqdm
```
<!-- Usage
To use the script, open your terminal and run the script with the following command: -->

## Usage

### Colab Version
Download the convert.ipynb and import it to Colab and download the compressed PDF

### Script
To use the script, open your terminal and run the script with the following command:

```bash
python convert.py <pdf_path> --save-name <output_pdf_name>
```

OR

```bash
python convert.py <pdf_path> <output_pdf_name>
```

For more information, run the script with the `--help` flag:

```bash
python convert.py --help
```


Highly Inspired by (https://github.com/manncodes/fixslide/tree/master)