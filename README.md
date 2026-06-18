# PDF Text Mining and WordCloud Analysis

A Python text-mining project that extracts text from PDF documents, cleans and preprocesses the content, and generates a WordCloud visualization showing the most prominent terms.

## Project objective

The project demonstrates a simple end-to-end natural-language-processing workflow for unstructured PDF content. It is intended as an educational example of document extraction, text cleaning, frequency analysis, and visual communication.

## Main workflow

1. Load a PDF document.
2. Extract text from its pages.
3. Normalize the text and remove unwanted characters.
4. Remove common stopwords.
5. Save the cleaned text.
6. Generate and export a WordCloud image.

## Features

- PDF text extraction
- Basic text normalization
- Stopword removal
- Word-frequency visualization
- Export of cleaned text
- Export of the final WordCloud image
- Notebook-based workflow suitable for Jupyter or Google Colab

## Technologies used

- Python
- pypdf
- NLTK
- wordcloud
- matplotlib
- Jupyter Notebook

## Repository structure

```text
notebooks/
  pdf_text_mining_wordcloud.ipynb
data/
  source_document.pdf
outputs/
  cleaned_text.txt
  wordcloud_output.png
docs/
  project_report.docx
README.md
requirements.txt
LICENSE
.gitignore
```

Some binary source and report files may need to be added manually when they are available.

## How to run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/pdf_text_mining_wordcloud.ipynb
```

Place the source PDF in the expected data location, update the file path in the notebook when necessary, and run the cells from top to bottom.

## Expected outputs

- Extracted and cleaned text
- A visual WordCloud of prominent terms
- A reproducible notebook showing the processing steps

## Limitations

- Results depend on the quality and layout of the PDF.
- Scanned image-only PDFs require OCR, which is not included in the current workflow.
- WordCloud size represents frequency, not contextual importance or sentiment.
- Basic stopword removal may not remove domain-specific filler words.

## Future improvements

- Add OCR support for scanned PDFs
- Add n-gram and keyword analysis
- Add sentiment or topic analysis
- Compare multiple documents
- Add configurable stopword lists
- Export a summary report automatically

## Author

**Muhammad Kamil Shah**  
BS Data Science

## License

This project is licensed under the MIT License.
