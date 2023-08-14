### Os dados de treino e teste são semelhantes nos outliers das idades, não tem necessidade de remover.
sns.boxplot(
    data = treino,
    x='Sobreviventes',
    hue='Sobreviventes',
    y='Idade',
    orient = "v", notch=False, palette="Set2",fliersize=5)