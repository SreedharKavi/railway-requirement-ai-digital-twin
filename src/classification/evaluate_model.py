import pandas as pd
import joblib
 
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
 
DATA_FILE = "data/labelled/etcs_review_dataset.csv"
 
MODEL_FILE = "models/svm_classifier.pkl"
VECTORIZER_FILE = "models/tfidf_vectorizer.pkl"
 
 
def load_dataset():
 
    try:
        df = pd.read_csv(DATA_FILE, encoding="utf-8")
 
    except UnicodeDecodeError:
 
        df = pd.read_csv(
            DATA_FILE,
            encoding="latin1"
        )
 
    return df
 
 
def main():
 
    df = load_dataset()
 
    df = df.dropna(
        subset=["Requirement_Text", "Final_Category"]
    )
 
    df = df[
        df["Final_Category"] != "Review"
    ]
 
    model = joblib.load(MODEL_FILE)
 
    vectorizer = joblib.load(
        VECTORIZER_FILE
    )
 
    X = vectorizer.transform(
        df["Requirement_Text"]
    )
 
    y = df["Final_Category"]
 
    predictions = model.predict(X)
 
    print("\nAccuracy:")
    print(
        f"{accuracy_score(y, predictions) * 100:.2f}%"
    )
 
    print("\nClassification Report")
 
    print(
        classification_report(
            y,
            predictions
        )
    )
 
    print("\nConfusion Matrix")
 
    print(
        confusion_matrix(
            y,
            predictions
        )
    )
 
 
if __name__ == "__main__":
    main()