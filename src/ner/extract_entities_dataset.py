import os
import json
import pandas as pd
 
from railway_ner import extract_entities
 
INPUT_FILE = "data/labelled/etcs_review_dataset.csv"
OUTPUT_FILE = "data/processed/etcs_entities.csv"
 
 
def load_dataset():
 
    encodings = [
        "utf-8",
        "cp1252",
        "latin1"
    ]
 
    for encoding in encodings:
 
        try:
 
            print(
                f"Trying encoding: {encoding}"
            )
 
            return pd.read_csv(
                INPUT_FILE,
                encoding=encoding
            )
 
        except Exception:
            pass
 
    raise Exception(
        "Unable to load dataset."
    )
 
 
def clean_text(text):
 
    if pd.isna(text):
        return ""
 
    text = str(text)
 
    return text.strip()
 
 
def main():
 
    print("\nLoading dataset...")
 
    df = load_dataset()
 
    print(
        f"Requirements loaded: {len(df)}"
    )
 
    os.makedirs(
        "data/processed",
        exist_ok=True
    )
 
    extracted_entities = []
 
    requirements_with_entities = 0
 
    entity_statistics = {}
 
    for index, text in enumerate(
        df["Requirement_Text"],
        start=1
    ):
 
        text = clean_text(text)
 
        entities = extract_entities(text)
 
        if entities:
 
            requirements_with_entities += 1
 
            for entity_type in entities:
 
                entity_statistics[
                    entity_type
                ] = (
                    entity_statistics.get(
                        entity_type,
                        0
                    ) + len(
                        entities[entity_type]
                    )
                )
 
        extracted_entities.append(
            json.dumps(
                entities,
                ensure_ascii=False
            )
        )
 
        if index % 100 == 0:
 
            print(
                f"Processed {index} requirements..."
            )
 
    df["Extracted_Entities"] = (
        extracted_entities
    )
 
    df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8-sig"
    )
 
    print("\n" + "=" * 60)
    print("ENTITY EXTRACTION COMPLETED")
    print("=" * 60)
 
    print(
        f"\nRequirements Processed: {len(df)}"
    )
 
    print(
        f"Requirements With Entities: "
        f"{requirements_with_entities}"
    )
 
    print(
        f"Output File: {OUTPUT_FILE}"
    )
 
    print("\nEntity Statistics")
    print("-" * 40)
 
    for entity, count in sorted(
        entity_statistics.items()
    ):
 
        print(
            f"{entity:<20} {count}"
        )
 
    print("\nSample Results")
    print("-" * 40)
 
    samples = df[
        df["Extracted_Entities"] != "{}"
    ].head(5)
 
    for _, row in samples.iterrows():
 
        print(
            f"\n{row['Requirement_ID']}"
        )
 
        print(
            row["Extracted_Entities"]
        )
 
 
if __name__ == "__main__":
    main()
 