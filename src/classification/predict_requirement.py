import joblib
 
MODEL_FILE = "models/svm_classifier.pkl"
VECTORIZER_FILE = "models/tfidf_vectorizer.pkl"
 
model = joblib.load(MODEL_FILE)
vectorizer = joblib.load(VECTORIZER_FILE)
 
while True:
 
    text = input("\nEnter Requirement:\n")
 
    vec = vectorizer.transform([text])
 
    prediction = model.predict(vec)
 
    print(
        "\nPredicted Category:",
        prediction[0]
    )
 