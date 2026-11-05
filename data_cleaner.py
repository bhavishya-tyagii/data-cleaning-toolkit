
import pandas as pd


def analyze_dataset(df):
    print("\n" + "=" * 45)
    print("       DATA CLEANING TOOLKIT")
    print("=" * 45)

    print("\n📊 Dataset Overview")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\n📋 Column Names")
    print(list(df.columns))

    print("\n❗ Missing Values")
    missing = df.isnull().sum()
    print(missing[missing > 0] if missing.any() else "No missing values found.")

    print("\n🔁 Duplicate Rows")
    print(f"Found: {df.duplicated().sum()}")

    print("\n📈 Numerical Summary")
    print(df.describe())


# Sample dataset
data = {
    "Name": ["Aarav", "Priya", "Rahul", "Neha", "Priya"],
    "Age": [20, 21, None, 22, 21],
    "Marks": [85, 92, 76, None, 92]
}

df = pd.DataFrame(data)

print("BEFORE CLEANING")
analyze_dataset(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numeric values with column averages
for column in df.select_dtypes(include="number").columns:
    df[column] = df[column].fillna(df[column].mean())

print("\n\nAFTER CLEANING")
analyze_dataset(df)

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\n✅ Cleaned dataset saved as cleaned_data.csv")
