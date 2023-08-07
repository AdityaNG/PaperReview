"""CLI interface for paperreview project.
"""
import argparse
import os

from .constants import Q_SUMMARY
from .helper import (
    ask_paper_text,
    download_pdf_from_url,
    extract_text_from_pdf,
)


def main():
    parser = argparse.ArgumentParser(
        description="Summarize a PDF using GPT-4."
    )
    parser.add_argument(
        "pdf_file", type=str, help="Path or URL to the PDF file"
    )
    args = parser.parse_args()

    pdf_path = args.pdf_file
    # if URL, download PDF file
    if pdf_path.startswith("http"):
        print("Downloading PDF file...")
        pdf_path = download_pdf_from_url(pdf_path)

    text = extract_text_from_pdf(pdf_path)
    question = Q_SUMMARY

    print("Reading the paper...")
    answer = ask_paper_text(text, question)

    print(answer)
    output_path = os.path.splitext(pdf_path)[0] + ".txt"
    with open(output_path, "w") as f:
        f.write(f"Question: {question}\nAnswer: {answer}")


if __name__ == "__main__":
    main()
