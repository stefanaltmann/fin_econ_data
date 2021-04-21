import requests
import json
import urllib3

url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
key = 'Dataflow' #/IFS/M.GB.PMP_IX' # adjust codes here

# Navigate to series in API-returned JSON data
data = (requests.get(f'{url}{key}').json()
        )

print(data['Obs'][-1]) # Print latest observation

# Find the series id and text name.
url = "http://dataservices.imf.org/REST/SDMX_JSON.svc/Dataflow/"
seriesids = json.load(urllib3.urlopen(url))


df = pd.DataFrame(seriesids[’Structure’][’KeyFamilies’][’KeyFamily’])
for x in range(6, 13):
items = (str(df[’@id’][x]), str(df[’Name’][x][’#text’]))
print ’: ’.join(items)