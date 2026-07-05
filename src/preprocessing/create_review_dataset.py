import pandas as pd
 
INPUT_FILE = "data/labelled/etcs_prelabelled_dataset.csv"
OUTPUT_FILE = "data/labelled/etcs_review_dataset.csv"
 
 
def main():
 
    df = pd.read_csv(INPUT_FILE)
 
    if "Final_Category" not in df.columns:
        df["Final_Category"] = ""
 
    df.to_csv(
        OUTPUT_FILE,
        index=False
    )
 
    print("-" * 60)
    print("Review Dataset Created")
    print("-" * 60)
    print(f"Rows: {len(df)}")
    print(f"Saved: {OUTPUT_FILE}")
 
 
if __name__ == "__main__":
    main()