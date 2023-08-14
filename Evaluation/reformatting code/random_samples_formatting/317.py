#ignore
# 這個才是每次都須執行的
emb_inp = embedding_layer_en(inp)
emb_tar = embedding_layer_zh(tar)
print("emb_inp:", emb_inp)
print("-" * 20)
print("emb_tar:", emb_tar)