top10_df = df.where(df['Country'].isin(top_10_list))
plot_heatmap(top10_df, 'AssessJob1')    
plt.title('Importance of Industry to assess potential job', fontsize=18)