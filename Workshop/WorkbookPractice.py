import pandas as pd
import requests
from PIL import Image
from io import BytesIO

name = input('Enter name: ')
print(f'Hello {name}')

url = "https://www.clipartmax.com/png/middle/331-3315172_prairie-view-a-m-football-logo.png"
response = requests.get(url)
print(response)

pic = Image.open(BytesIO(response.content))
pic.show()

df = pd.read_csv(r'C:\\Users\devri\Documents\ChevronWorkshop\Salaries.csv')

print(df.count())

print((df['BasePay'].sum())/(df['BasePay'].count()))

print(len(df['JobTitle'].unique()))

print((df[(df.BasePay > 80000) & (df.BasePay < 120000)])['BasePay'].count())

df.groupby('Year').TotalPay.mean().plot(kind = 'bar')

newurl = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv"

evdf = pd.read_csv(
    newurl,
    sep=',',
    encoding='utf-8',
)

display(evdf)