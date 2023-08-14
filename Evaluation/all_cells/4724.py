df = pd.DataFrame({'Precision': p, 'Recall': r, 'F1-Score': f}, index=names_keep[1:])*100
print(df.round(2).to_latex())
df.mean().round(2)