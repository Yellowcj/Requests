import requests
import json

agisurl = "http://server.arcgisonline.com/arcgis/rest/services?f=pjson"
r = requests.get(agisurl)

print(r.json())

decoded = json.loads(r.text)

print(decoded)

res = r.json()

print(res["currentVersion"])

