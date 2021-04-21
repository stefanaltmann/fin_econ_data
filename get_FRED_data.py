import pandas as pd
import requests

keys_file = open('keys.txt')
try:
    lines = keys_file.readlines()
    fred_api_key = lines[1].rstrip()
finally:
    keys_file.close()

url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
key = 'Dataflow' #/IFS/M.GB.PMP_IX' # adjust codes here

# Navigate to series in API-returned JSON data
data = (requests.get(f'{url}{key}').json()
        )
url_obs = 'https://api.stlouisfed.org/fred/series/observations?'

seriesids = {
    # interest rate spreads

    'T10Y2Y': '10Y treasury minus 2Y treasury',
    'T10YIE': '10Y breakeven inflation rate',
    'T10Y3M': '10Y treasury minus 3M treasury'
}

data = pd.DataFrame()


for id in seriesids:
    query = requests.get(f'{url_obs}series_id={id}&api_key={fred_api_key}&file_type=json').json()
    query = pd.DataFrame(query['observations'])
    query['id'] = id
    query['description'] = seriesids[id]
    data = data.append(query)

data[['date', 'id', 'description', 'value']].to_csv('data.csv', index=False)

