import re
from pathlib import Path
 
import pandas as pd
from pypdf import PdfReader
 
 
PDF_FOLDER = "docs/etcs"
OUTPUT_FILE = "data/raw/etcs_requirements_raw.csv"
 
 
def extract_text_from_pdf(pdf_file):
 
    text = ""
 
    try:
 
        reader = PdfReader(pdf_file)
 
        for page in reader.pages:
 
            page_text = page.extract_text()
 
            if page_text:
                text += page_text + "\n"
 
    except Exception as e:
 
        print(f"Error reading {pdf_file}: {e}")
 
    return text
 
 
def split_sentences(text):
 
    text = text.replace("\n", " ")
 
    sentences = re.split(r'(?<=[.!?])\s+', text)
 
    return sentences
 
 
def is_requirement(sentence):
 
    keywords = [
        "shall",
        "should",
        "must"
    ]
 
    sentence = sentence.lower()
 
    return any(k in sentence for k in keywords)
 
 
def main():
 
    requirements = []
 
    counter = 1
 
    pdf_files = Path(PDF_FOLDER).glob("*.pdf")
 
    for pdf_file in pdf_files:
 
        print(f"Processing {pdf_file.name}")
 
        text = extract_text_from_pdf(pdf_file)
 
        sentences = split_sentences(text)
 
        for sentence in sentences:
 
            sentence = sentence.strip()
 
            if len(sentence) < 20:
                continue
 
            if is_requirement(sentence):
 
                requirements.append({
                    "Requirement_ID":
                        f"REQ_{counter:05d}",
 
                    "Requirement_Text":
                        sentence,
 
                    "Source":
                        pdf_file.name,
 
                    "Section":
                        "",
 
                    "Domain":
                        ""
                })
 
                counter += 1
 
    df = pd.DataFrame(requirements)
 
    df.drop_duplicates(
        subset=["Requirement_Text"],
        inplace=True
    )
 
    df.to_csv(
        OUTPUT_FILE,
        index=False
    )
 
    print("\nCompleted")
    print(f"Requirements Extracted: {len(df)}")
    print(f"Saved: {OUTPUT_FILE}")
 
 
if __name__ == "__main__":
    main()
 