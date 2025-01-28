import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import pickle

def train_model(data_path):
    # Load dataset
    data = pd.read_csv(data_path)
    
    # Preprocessing
    X = data[['Temperature', 'Run_Time']]
    y = data['Downtime_Flag']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    # Save model
    with open('data/model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    return {"accuracy": accuracy, "f1_score": f1}

def load_model():
    with open('data/model.pkl', 'rb') as f:
        return pickle.load(f)

def make_prediction(data, model):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    confidence = model.predict_proba(df).max()
    return {"Downtime": "Yes" if prediction[0] == 1 else "No", "Confidence": round(confidence, 2)}
