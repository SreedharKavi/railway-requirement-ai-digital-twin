import json
import pandas as pd
 
from railway_ner import extract_entities
 
INPUT_FILE = "data/labelled/etcs_review_dataset.csv"
OUTPUT_FILE = "data/processed/etcs_entities.csv"
 
 
def load_dataset():
 
    try:
        return pd.read_csv(
            INPUT_FILE,
            encoding="utf-8"
        )
 
    except UnicodeDecodeError:
 
        print("UTF-8 failed. Using Latin1...")
 
        return pd.read_csv(
            INPUT_FILE,
            encoding="latin1"
        )
 
 
def main():
 
    print("Loading ETCS dataset...")
 
    df = load_dataset()
 
    extracted_entities = []
 
    for text in df["Requirement_Text"]:
 
        entities = extract_entities(
            str(text)
        )
 
        extracted_entities.append(
            json.dumps(
                entities,
                ensure_ascii=False
            )
        )
 
    df["Extracted_Entities"] = extracted_entities
 
    df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8"
    )
 
    print("\n" + "=" * 60)
    print("ENTITY EXTRACTION COMPLETED")
    print("=" * 60)
 
    print(f"\nRequirements Processed: {len(df)}")
    print(f"Output File: {OUTPUT_FILE}")
 
    entity_count = sum(
        1 for item in extracted_entities
        if item != "{}"
    )
 
    print(
        f"Requirements With Entities: {entity_count}"
    )
 
    print("\nDone.")
 
 
if __name__ == "__main__":
    main()
 