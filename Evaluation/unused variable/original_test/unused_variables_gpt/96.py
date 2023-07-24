with open("obj.json", "rt", encoding="utf8") as f:
    json_string = f.read()
    obj = json.loads(json_string)
    print(obj.keys())
    print(obj['name'], obj['since'])