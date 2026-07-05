"""
ETCS Requirement Extractor
 
Version: 1.0
 
Purpose:
---------
Extract candidate requirement statements from ETCS documents.
 
Rules:
- Keep sentences containing:
    shall
    should
    must
 
Output:
---------
data/raw/etcs_requirements_raw.csv
"""
 
import re
import pandas as pd
from pathlib import Path
 
 
INPUT_FILE = "docs/etcs/etcs_text.txt"
OUTPUT_FILE = "data/raw/etcs_requirements_raw.csv"
 
 
def split_sentences(text):
 
    sentences = re.split(r'(?<=[.!?])\s+', text)
 
    return sentences
 
 
def is_requirement(sentence):
 
    keywords = ["shall", "should", "must"]
 
    sentence_lower = sentence.lower()
 
    return any(word in sentence_lower for word in keywords)
 
 
def extract_requirements(text):
 
    requirements = []
 
    sentences = split_sentences(text)
 
    counter = 1
 
    for sentence in sentences:
 
        sentence = sentence.strip()
 
        if len(sentence) < 10:
            continue
 
        if is_requirement(sentence):
 
            requirement = {
                "Requirement_ID":
                    f"REQ_{counter:05d}",
 
                "Requirement_Text":
                    sentence,
 
                "Source":
                    "Subset-026",
 
                "Section":
                    "",
 
                "Domain":
                    ""
            }
 
            requirements.append(requirement)
 
            counter += 1
 
    return requirements
 
 
def main():
 
    input_path = Path(INPUT_FILE)
 
    if not input_path.exists():
 
        print(f"File not found: {INPUT_FILE}")
        return
 
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
 
        text = file.read()
 
    requirements = extract_requirements(text)
 
    df = pd.DataFrame(requirements)
 
    df.to_csv(
        OUTPUT_FILE,
        index=False
    )
 
    print("-" * 50)
    print(f"Requirements found: {len(df)}")
    print(f"Saved to: {OUTPUT_FILE}")
    print("-" * 50)
 
 
if __name__ == "__main__":
 
    main()