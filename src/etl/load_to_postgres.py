import pandas as pd
from sqlalchemy import create_engine

DB_USER = "sandeepundurthi"   # your Mac username
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ecommerce_delay_db"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

df = pd.read_csv("data/processed/clean_shipping_data.csv")

df.to_sql(
    "shipment_data",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded into PostgreSQL successfully.")
print(f"Rows loaded: {len(df)}")
