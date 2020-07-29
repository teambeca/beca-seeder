import json
import requests

HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJoYWhhaGF5ZXNzcyIsImV4cCI6MzMxNTIzMDU2NjMsImlhdCI6MTU5NTM3OTY2M30.PbRYRGMxBvMTlMEY-3VM8vqTfUkfG0m2hwspbsQsPidAUypMq5YbQrvJNIybbUUzJlYiQU3bYtUx5FZ6WHkqIA"
}

with open("sentences.txt", "r", encoding="utf-8") as text_file:
    sentences = text_file.readlines()

sentences = list(filter(lambda _x: not _x.__eq__("\n"), sentences))
sentences = list(map(lambda _x: _x.strip(), sentences))

for _x in range(len(sentences)):
    DATA = {
        "text": sentences.pop().split(),
        "questionType": 1
    }

    DATA = json.dumps(DATA, ensure_ascii=False).encode("utf8")

    response = requests.post(
        "https://beca-api.herokuapp.com/admin/question",
        headers=HEADER,
        data=DATA
    )

    if response.status_code != 200:
        with open("leftovers.txt", "w", encoding="utf-8") as text_file:
            for _s in sentences:
                text_file.write(_s + "\n")
        print("Got error")
        print(response.json())
        break
