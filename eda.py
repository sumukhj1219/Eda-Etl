import pandas as pd

df_csv = pd.read_csv("choclates.csv")
df_json = pd.read_json("iris.json")

df_csv.columns = df_csv.columns.str.lower().str.strip()
df_json.columns = df_json.columns.str.lower().str.strip()

df_csv = df_csv.drop_duplicates()
df_json = df_json.drop_duplicates()

df_csv = df_csv.dropna()
df_json = df_json.dropna()

df_csv.to_csv("exported_chocolates.csv", index=False)
df_json.to_csv("exported_iris.csv", index=False)

combined = pd.concat([df_csv, df_json], ignore_index=True)
combined.to_csv("combined.csv", index=False)

print(df_csv.info())
print(df_json.info())




