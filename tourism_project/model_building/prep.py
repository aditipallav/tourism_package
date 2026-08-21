
import pandas as pd
from sklearn.model_selection import train_test_split

import pandas as pd

RAW_PATH = "tourism_project/data/tourism_updated.csv"

# Load the raw dataset
df2 = pd.read_csv(RAW_PATH)

# Separate features and target
X = df2.drop(columns=["ProdTaken"])
y = df2["ProdTaken"]

print("Features shape:", X.shape)
print("Target shape:", y.shape)

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Save the splits
X_train.to_csv("Xtrain.csv", index=False)
X_test.to_csv("Xtest.csv", index=False)
y_train.to_csv("ytrain.csv", index=False)
y_test.to_csv("ytest.csv", index=False)

print("\nData preparation completed successfully!")

print("X_train:", X_train.shape)
print("X_test :", X_test.shape)
print("y_train:", y_train.shape)
print("y_test :", y_test.shape)
