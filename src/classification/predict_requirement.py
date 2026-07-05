import joblib
 
MODEL_FILE = "models/svm_classifier.pkl"
VECTORIZER_FILE = "models/tfidf_vectorizer.pkl"
 
 
model = joblib.load(
    MODEL_FILE
)
 
vectorizer = joblib.load(
    VECTORIZER_FILE
)
 
 
print("\nRailway Requirement Classifier")
print("Type 'exit' to quit")
 
 
while True:
 
    text = input(
        "\nEnter Requirement:\n"
    )
 
    if text.lower() == "exit":
        break
 
    vec = vectorizer.transform(
        [text]
    )
 
    prediction = model.predict(
        vec
    )
 
    print(
        f"\nPredicted Category: {prediction[0]}"
    )
 