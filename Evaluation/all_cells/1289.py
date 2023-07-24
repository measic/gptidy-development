#aggregate mean value for plotting
df0_10k_grouped = df0_10k_edit9.groupby(['region']).mean()

df10_18k_grouped = df10_18k_edit.groupby(['region']).mean()

df18_32_grouped = df18_32.groupby(['region']).mean()

df32_grouped = df32.groupby(['region']).mean()
