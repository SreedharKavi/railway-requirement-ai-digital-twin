import pandas as pd
 
INPUT_FILE = "data/processed/etcs_requirements_clean.csv"
OUTPUT_FILE = "data/labelled/etcs_prelabelled_dataset.csv"
 
 
CATEGORY_RULES = {
 
    "Safety": [
        "emergency",
        "safe",
        "safety",
        "danger",
        "hazard",
        "protection",
        "integrity",
        "braking",
        "fail",
        "failure"
    ],
 
    "Performance": [
        "speed",
        "distance",
        "accuracy",
        "latency",
        "time",
        "performance",
        "capacity",
        "rate",
        "timeout"
    ],
 
    "Operational": [
        "mode",
        "driver",
        "transition",
        "shunting",
        "mission",
        "operation",
        "operational",
        "level"
    ],
 
    "Environmental": [
        "temperature",
        "humidity",
        "environment",
        "vibration",
        "emc",
        "climatic",
        "weather"
    ],
 
    "Functional": [
        "calculate",
        "receive",
        "transmit",
        "send",
        "store",
        "generate",
        "process",
        "display",
        "communicate"
    ]
}
 
 
def assign_category(text):
 
    text = str(text).lower()
 
    for category, keywords in CATEGORY_RULES.items():
 
        for keyword in keywords:
 
            if keyword in text:
                return category
 
    return "Review"
 
 
def main():
 
    df = pd.read_csv(INPUT_FILE)
 
    df["Suggested_Category"] = (
        df["Requirement_Text"]
        .apply(assign_category)
    )
 
    df.to_csv(
        OUTPUT_FILE,
        index=False
    )
 
    print("-" * 60)
 
    print("Pre-labelling Completed")
 
    print("-" * 60)
 
    print(
        df["Suggested_Category"]
        .value_counts()
    )
 
    print("-" * 60)
 
    print(f"Saved: {OUTPUT_FILE}")
 
 
if __name__ == "__main__":
    main()