import pandas as pd
df = pd.read_csv(r"C:\Users\Shalini B\Downloads\netflix_titles.csv\netflix_titles.csv")
print(df.head())
print(df.isnull().sum())
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna('Unknown')
df.dropna(subset=['date_added', 'rating'], inplace=True)
df.drop_duplicates(inplace=True)
df.columns = df.columns.str.lower().str.replace(" ", "_")
df['date_added'] = df['date_added'].str.strip()
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df.to_csv("cleaned_netflix.csv", index=False)
print("Data cleaned successfully!")


