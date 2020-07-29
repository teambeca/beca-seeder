import json
import requests

HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJoYWhhaGF5ZXNzcyIsImV4cCI6MzMxNTIzMDU2NjMsImlhdCI6MTU5NTM3OTY2M30.PbRYRGMxBvMTlMEY-3VM8vqTfUkfG0m2hwspbsQsPidAUypMq5YbQrvJNIybbUUzJlYiQU3bYtUx5FZ6WHkqIA"
}

with open("sentences.txt", "r", encoding="utf-8") as text_file:
    sentences = text_file.readlines()

# sentences = sentences[0:10]

sentences = list(filter(lambda _x: not _x.__eq__("\n"), sentences))
sentences = list(map(lambda _x: _x.strip(), sentences))

texts = []
for _x in sentences:
    texts.append(_x)

_json = {
    "type": "sentence",
    "texts": texts
}

with open("_json.txt", "w", encoding="utf-8") as json_file:
    json.dump(_json, json_file, ensure_ascii=False)
