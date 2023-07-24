import seaborn as sns
import matplotlib.pyplot as plt

ax = sns.barplot(x=0, y=1, hue=2, data=degree_df)
ax.set_xlabel('Grado de nodo')
ax.set_ylabel('Cantidad de nodos con ese grado')
ax.set_title('Análisis sacando 2% distinguido')
plt.show()