import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import joblib
import os

# Load dataset
data = pd.read_csv('data/raw/default_of_credit_card_clients.csv')

# Features and target
X = data.drop('default.payment.next.month', axis=1)
y = data['default.payment.next.month']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = GradientBoostingClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model.pkl')
print("✅ Model trained and saved to model.pkl")
