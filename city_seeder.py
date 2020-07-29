import json

with open("locations.json", "r", encoding="utf-8") as json_file:
    raw_data = json.load(json_file)
raw_data = raw_data[0]

locations = []
for x in raw_data["cities"]:
    locations.append(x["name"])

with open("_json3.txt", "w", encoding="utf-8") as json_file:
    json.dump(locations, json_file, ensure_ascii=False)
