#https://opendata.cwa.gov.tw/dist/opendata-swagger.html
import json,urllib.request

url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-093?Authorization=CWA-AC53559C-E22B-44B0-B80A-AA40662B98A3&locationId=F-D0047-009'

data = urllib.request.urlopen(url).read()
output = json.loads(data)
location=output['records']['locations'][0]['location']


for i in location:
    print(f'{i}')


for i in location:
  name = i['locationName']
  lat=i['lat']
  print(name,lat)
