import pandas as pd
import seaborn as sns

df = pd.read_csv('assets/annual-enterprise-survey-2021-financial-year-provisional-csv.csv')
df.head()

sns.scatterplot(x=df['Year'],
                y=df['Units'])
