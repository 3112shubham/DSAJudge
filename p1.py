import json
from firebase_config import db

with open("data.json", "r") as f:
    data = json.load(f)

for entry in data:
    model = entry["model"].split(".")[-1]
    pk = entry["pk"]
    fields = entry["fields"]
    db.collection(model).document(str(pk)).set(fields)
