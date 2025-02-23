import pandas as pd
import seaborn as sns
df = sns.load_dataset('tips')
print(df.head())
print(df.describe())
df['total_bill'].mean()