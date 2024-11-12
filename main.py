import argparse
from reader import extract_text_from_pdf
from segment import segmenter
from embedding import generate_embeddings
from pine import batch_upsert

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process a PDF file.')
    parser.add_argument('pdf_path', type=str, help='Path to the PDF file')
    args = parser.parse_args()

    extracted_text = extract_text_from_pdf(args.pdf_path)
    chunks = segmenter(extracted_text)
    embeddings = generate_embeddings(chunks, 512, False)
    batch_upsert(chunks, embeddings, 100)
