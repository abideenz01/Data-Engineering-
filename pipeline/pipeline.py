import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--month", type=int, default=12)

args = parser.parse_args()
month = args.month

df = pd.DataFrame({"day": [1, 2], "num_passenger": [3, 4]})
df['month']=month
print(df.head())
df.to_parquet(f"output_{month}.parquet")

print(f"hello pipeline, month={month}")
