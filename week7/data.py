"""
Data Analysis & Visualization Assignment
Objective:
1. Load and analyze a dataset using pandas.
2. Create simple plots with matplotlib for visualization.
"""

# -----------------------------
# 📦 Import Libraries
# -----------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Make plots prettier
sns.set(style="whitegrid")

# -----------------------------
# Task 1: Load & Explore Dataset
# -----------------------------

try:
    # Load Iris dataset from sklearn
    iris_data = load_iris(as_frame=True)
    df = iris_data.frame

    print("✅ Dataset successfully loaded!\n")
except Exception as e:
    print(f"❌ Error loading dataset: {e}")
    exit()

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head(), "\n")

# Dataset structure
print("Dataset Info:")
print(df.info(), "\n")

# Check missing values
print("Missing Values in Dataset:")
print(df.isnull().sum(), "\n")

# Clean dataset (fill or drop missing values)
df = df.dropna()

# -----------------------------
# Task 2: Basic Data Analysis
# -----------------------------

# Basic statistics
print("Basic Statistics:")
print(df.describe(), "\n")

# Group by species and compute mean
group_means = df.groupby("target").mean()
print("Mean values grouped by species:")
print(group_means, "\n")

# Observations
print("📊 Observation: Sepal length and petal length vary greatly across species.\n")

# -----------------------------
# Task 3: Data Visualization
# -----------------------------

# 1. Line Chart (example: sepal length trend across dataset index)
plt.figure(figsize=(8, 4))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart: Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart (average petal length per species)
plt.figure(figsize=(8, 4))
sns.barplot(x="target", y="petal length (cm)", data=df, estimator="mean")
plt.title("Bar Chart: Avg Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Avg Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(8, 4))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot (sepal length vs petal length)
plt.figure(figsize=(8, 6))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="target", data=df, palette="deep")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
