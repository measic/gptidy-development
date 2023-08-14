import json

json_string = json.dumps(obj)  # str을 반환 (유니코드)

with open("obj.json", "wt", encoding="utf8") as f:
    f.write(json_string)