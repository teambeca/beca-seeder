import json
import pandas as pd

dataset = pd.read_csv("T3.csv", index_col=0)
dataset = dataset[:1900]

_json = {
    "type": "word",
    "texts": [(lambda x: x[0])(f) for f in dataset.values.tolist()]
}

with open("_json2.txt", "w", encoding="utf-8") as json_file:
    json.dump(_json, json_file, ensure_ascii=False)
