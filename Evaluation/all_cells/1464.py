import json
with open('datalist.txt', 'w') as file:
    #sort_keys, indent and separators fields make the output file easier to read.
    json.dump(datalist, file, sort_keys=True, indent=4, separators=(',', ':'))
