
import pandas as pd

RAW_PATH = "tourism_project/data/tourism_updated.csv"

# Load the raw dataset
df2 = pd.read_csv(RAW_PATH)

# Expected columns
expected_columns = [
   "ProdTaken",
    "Age",
    "TypeofContact",
    "CityTier",
    "DurationOfPitch",
    "Occupation",
    "Gender",
    "NumberOfPersonVisiting",
    "NumberOfFollowups",
    "ProductPitched",
    "MaritalStatus",
    "NumberOfTrips",
    "Passport",
    "PitchSatisfactionScore",
    "OwnCar",
    "NumberOfChildrenVisiting",
    "Designation",
    "MonthlyIncome",
    "PreferredPropertyStar"
]

# Check for missing expected columns
missing = [c for c in expected_columns if c not in df2.columns]

if missing:
    raise ValueError(
        f"Dataset is missing expected columns: {missing}"
    )

# Check for unexpected columns
unexpected = [c for c in df2.columns if c not in expected_columns]

if unexpected:
    print("Unexpected columns found:", unexpected)
else:
    print("No unexpected columns found.")

# Dataset summary
print("\nDataset registered successfully.")
print(f"Rows: {df2.shape[0]}")
print(f"Columns: {df2.shape[1]}")

print("\nColumns:")
print(list(df2.columns))

print("\nMissing values:")
print(df2.isnull().sum())

print("\nPurchase distribution:")
print(df2["ProdTaken"].value_counts())
