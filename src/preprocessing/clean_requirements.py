import pandas as pd
import re
 
INPUT_FILE = "data/raw/etcs_requirements_raw.csv"
OUTPUT_FILE = "data/processed/etcs_requirements_clean.csv"
 
 
REMOVE_PATTERNS = [
    r'figure\s+\d',
    r'table\s+\d',
    r'chapter\s+\d',
    r'notes?',
    r'justification',
    r'example'
]
 
 
def clean_text(text):
 
    text = str(text)
 
    text = text.replace("&nbsp;", " ")
    text = text.replace("â€“", "-")
    text = text.replace("ï‚·", "")
 
    text = re.sub(r'\s+', ' ', text)
 
    return text.strip()
 
 
def is_valid_requirement(text):
 
    text_lower = text.lower()
 
    for pattern in REMOVE_PATTERNS:
 
        if re.search(pattern, text_lower):
            return False
 
    return True
 
 
def main():
 
    df = pd.read_csv(INPUT_FILE)
 
    df["Requirement_Text"] = \
        df["Requirement_Text"].apply(clean_text)
 
    df = df[
        df["Requirement_Text"]
        .apply(is_valid_requirement)
    ]
 
    df.drop_duplicates(
        subset=["Requirement_Text"],
        inplace=True
    )
 
    df.to_csv(
        OUTPUT_FILE,
        index=False
    )
 
    print(f"Clean requirements: {len(df)}")
    print(f"Saved to: {OUTPUT_FILE}")
 
 
if __name__ == "__main__":
    main()