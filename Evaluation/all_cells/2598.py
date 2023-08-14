X = img.reshape(-1, 3).astype(int)
N, D = X.shape
print("flatten pixel matrix shape:", X.shape)