import os
import joblib
import pandas as pd
 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
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
        df = pd.read_csv(
            DATA_FILE,
            encoding="utf-8"
        )
 
    except UnicodeDecodeError:
 
        print("UTF-8 failed. Trying Latin1...")
 
        df = pd.read_csv(
            DATA_FILE,
            encoding="latin1",
            on_bad_lines="skip"
        )
 
    return df
 
 
def prepare_dataset(df):
 
    df["Requirement_Text"] = (
        df["Requirement_Text"]
        .astype(str)
        .str.strip()
    )
 
    df["Final_Category"] = (
        df["Final_Category"]
        .astype(str)
        .str.strip()
    )
 
    df = df[
        df["Requirement_Text"] != ""
    ]
 
    df = df[
        df["Final_Category"] != ""
    ]
 
    df = df[
        df["Final_Category"] != "Review"
    ]
 
    return df
 
 
def main():
 
    print("\nLoading dataset...")
 
    df = load_dataset()
 
    df = prepare_dataset(df)
 
    print("\nDataset Summary")
    print("-" * 50)
 
    print(f"Total labelled records: {len(df)}")
 
    print("\nClass Distribution")
    print(df["Final_Category"].value_counts())
 
    print("-" * 50)
 
    X = df["Requirement_Text"]
 
    y = df["Final_Category"]
 
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )
 
    print("\nVectorizing text...")
 
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        max_features=5000,
        ngram_range=(1, 2)
    )
 
    X_train_tfidf = vectorizer.fit_transform(
        X_train
    )
 
    X_test_tfidf = vectorizer.transform(
        X_test
    )
 
    print("Training SVM model...")
 
    model = LinearSVC(
        random_state=42
    )
 
    model.fit(
        X_train_tfidf,
        y_train
    )
 
    predictions = model.predict(
        X_test_tfidf
    )
 
    accuracy = accuracy_score(
        y_test,
        predictions
    )
 
    print("\n")
    print("=" * 60)
    print("MODEL RESULTS")
    print("=" * 60)
 
    print(
        f"\nAccuracy: {accuracy * 100:.2f}%"
    )
 
    print("\nClassification Report")
    print("-" * 60)
 
    print(
        classification_report(
            y_test,
            predictions
        )
    )
 
    print("\nConfusion Matrix")
    print("-" * 60)
 
    print(
        confusion_matrix(
            y_test,
            predictions
        )
    )
 
    os.makedirs(
        "models",
        exist_ok=True
    )
 
    joblib.dump(
        model,
        MODEL_FILE
    )
 
    joblib.dump(
        vectorizer,
        VECTORIZER_FILE
    )
 
    print("\n")
    print("=" * 60)
    print("MODEL SAVED")
    print("=" * 60)
 
    print(
        f"\nClassifier: {MODEL_FILE}"
    )
 
    print(
        f"Vectorizer: {VECTORIZER_FILE}"
    )
 
 
if __name__ == "__main__":
    main()
 