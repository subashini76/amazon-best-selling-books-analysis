import pandas as pd

# -----------------------------
# Step 1: Load the CSV file
# -----------------------------
df = pd.read_csv("bestsellers.csv")

# -----------------------------
# Step 2: Explore the Data
# -----------------------------
print("First 5 rows of the dataset:")
print(df.head())

print("\nShape of the dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nSummary statistics:")
print(df.describe())

# -----------------------------
# Step 3: Clean the Data
# -----------------------------

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Rename columns for clarity
df.rename(columns={
    "Name": "Title",
    "User Rating": "Rating",
    "Year": "Publication Year"
}, inplace=True)

# Convert Price column to float
df["Price"] = df["Price"].astype(float)

# -----------------------------
# Step 4: Analysis
# -----------------------------

# Author popularity analysis
author_counts = df["Author"].value_counts()
print("\nTop authors by number of bestsellers:")
print(author_counts)

# Average rating by genre
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print("\nAverage rating by genre:")
print(avg_rating_by_genre)

# -----------------------------
# Step 5: Export Results
# -----------------------------

# Export top 10 authors
author_counts.head(10).to_csv("top_authors.csv")

# Export average rating by genre
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")

print("\nAnalysis complete! Files exported successfully.")
