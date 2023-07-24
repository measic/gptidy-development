# Pegamos os índices para representar os usuários ao invés de seus
# nomes ("s002", "s003", ...)
labels = np.array([users.index(rec) for rec in recordings[:,0]])
print(labels)