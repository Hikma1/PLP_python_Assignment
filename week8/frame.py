# Check dimensions
print("\nDataFrame Dimensions (rows, columns):")
print(df.shape)

# Identify data types
print("\nData Types of Each Column:")
print(df.dtypes)

# Check for missing values in important columns
important_columns = ['cord_uid', 'title', 'abstract', 'publish_time', 'journal', 'source_x']
print("\nMissing Values in Important Columns:")
print(df[important_columns].isnull().sum())

# Generate basic statistics for numerical columns
print("\nBasic Statistics for Numerical Columns:")
print(df.describe())

# Calculate percentage of missing values per column
missing_percentage = df.isnull().mean() * 100
print("\nPercentage of Missing Values per Column:")
print(missing_percentage)

# Drop columns with >50% missing values (except critical ones)
threshold = 50
columns_to_drop = missing_percentage[missing_percentage > threshold].index
columns_to_drop = [col for col in columns_to_drop if col not in important_columns]  # Protect important columns
df_cleaned = df.drop(columns=columns_to_drop)
print("\nColumns dropped due to high missing values:", columns_to_drop)

# Handle missing values in important columns
df_cleaned = df_cleaned.dropna(subset=['title', 'abstract'])  # Drop rows with missing title or abstract
df_cleaned['journal'] = df_cleaned['journal'].fillna('Unknown')  # Fill missing journals
df_cleaned['publish_time'] = df_cleaned['publish_time'].fillna('Unknown')  # Fill missing publish_time

# Verify cleaning
print("\nMissing Values After Cleaning:")
print(df_cleaned[important_columns].isnull().sum())
# Convert publish_time to datetime, handle errors
df_cleaned['publish_time'] = pd.to_datetime(df_cleaned['publish_time'], errors='coerce')

# Extract year from publish_time
df_cleaned['year'] = df_cleaned['publish_time'].dt.year

# Create abstract word count column
df_cleaned['abstract_word_count'] = df_cleaned['abstract'].apply(lambda x: len(str(x).split()) if pd.notnull(x) else 0)

# Verify new columns
print("\nFirst 5 rows with new columns:")
print(df_cleaned[['publish_time', 'year', 'abstract_word_count']].head())