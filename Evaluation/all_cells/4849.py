#load 
with open("GRUmodel_128_64_log.pkl", "rb") as file:
    logs["GRU"] = pickle.load(file)

with open("GRUmodel_128_128_log.pkl", "rb") as file:
     logs["GRU_128"] = pickle.load(file)

with open("GRUmodel_128_256_log.pkl", "rb") as file:
    logs["GRU_256"] = pickle.load(file)

with open("GRUmodel_128_64_64_log.pkl", "rb") as file:
    logs["GRU_64_64"] = pickle.load(file)
    