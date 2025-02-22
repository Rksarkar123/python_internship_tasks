import pandas as pd from sklearn.model_selection import train_test_split from sklearn.ensemble import RandomForestClassifier from sklearn.metrics import accuracy_score

Load dataset (example: spam email detection)

data = { "Feature1": [1, 0, 1, 0, 1, 0, 1, 0], "Feature2": [0, 1, 0, 1, 0, 1, 0, 1], "Label": [1, 0, 1, 0, 1, 0, 1, 0]  # 1 = Spam, 0 = Not Spam } df = pd.DataFrame(data)

Split data into training and testing sets

X = df.drop(columns=["Label"]) y = df["Label"] X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

Train model

model = RandomForestClassifier(n_estimators=100, random_state=42) model.fit(X_train, y_train)

Make predictions

y_pred = model.predict(X_test)

Evaluate model

accuracy = accuracy_score(y_test, y_pred) print(f"Model Accuracy: {accuracy:.2f}")