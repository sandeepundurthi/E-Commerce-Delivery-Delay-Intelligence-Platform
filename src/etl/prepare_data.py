import pandas as pd

df = pd.read_csv("data/raw/shipping_data.csv")

df.columns = (
    df.columns
    .str.lower()
    .str.replace(".", "_", regex=False)
)

df = df.rename(columns={
    "reached_on_time_y_n": "reached_on_time"
})

df["is_delayed"] = df["reached_on_time"].apply(lambda x: 0 if x == 1 else 1)

df.to_csv("data/processed/clean_shipping_data.csv", index=False)

print("Clean data saved successfully.")
print(df.head())
print(df.shape)
