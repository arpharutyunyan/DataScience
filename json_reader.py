import requests
import json

link = "https://swapi.dev/api/people"
req = requests.get(link)
reader=req.json()
res=json.dumps(reader)
with open("file.json", "w") as f:
    f.write(res)
