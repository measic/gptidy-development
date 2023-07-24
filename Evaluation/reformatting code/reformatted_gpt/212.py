import random
import pandas as pd

y_competencia = random_grid_gb.predict_proba(X_competencia)

df = pd.DataFrame(index=range(501, 5000))
df['output'] = [round(x[1], 4) for x in y_competencia]
df.to_csv('lambda_null_y_competencia.csv')