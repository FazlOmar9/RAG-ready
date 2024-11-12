# RAG-ready

RAG-ready pipelines your PDF preprocessing, chunking, vectorisation and storage to Pinecone. Go from documents to a rag ready pinecone index in one go. Be it for search applications, chatbot development or recommendation systems - RAG-ready simplifies it all.

## Requirements

- Python 3.6+
- `.env` file with the following keys:
  - `JINA_API_KEY`
  - `PINECONE_API_KEY`
  - `PINECONE_INDEX_NAME`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/FazlOmar9/RAG-ready.git
    cd RAG-ready
    ```

2. Create a virtual environment:

    ```sh
    python -m venv .venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```sh
        .venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source .venv/bin/activate
        ```

4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

5. Create a [.env]() file in the root directory with the following content:

    ```properties
    JINA_API_KEY=your_jina_api_key
    PINECONE_API_KEY=your_pinecone_api_key
    PINECONE_INDEX_NAME=your_pinecone_index_name
    ```

## Usage

1. Place your PDF file in the [documents]() directory.

2. Run the main script with the path to your PDF file as an argument:

    ```sh
    python main.py documents/your_pdf_file.pdf
    ```

This will extract text from the PDF, segment it, generate embeddings, and upload the vectors to Pinecone.
