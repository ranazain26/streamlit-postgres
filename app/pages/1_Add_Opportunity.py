import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# 1. Load your uploaded dataset file using pandas
filename = "diabetes.csv" 
df = pd.read_csv(filename)

# 2. Split features (X) and target label (y)
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# 3. Split into training and test datasets using an 80/20 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# 4. Initialize and train the Gaussian Naive Bayes Classifier
model = GaussianNB()
model.fit(X_train, y_train)

# 5. Make predictions and evaluate accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

# Print final results
print(f"Split {len(df)} rows into train={len(X_train)} and test={len(X_test)} rows")
print(f"Accuracy: {accuracy * 100:.3f}%")
