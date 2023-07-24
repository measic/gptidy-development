# concatenate all name fields from tasks separated by duration of 3 days
less_text = ' '.join(list(all_df[all_df['Duration'].astype('timedelta64[D]') < 3]['Name'].dropna()))
grtr_text = ' '.join(list(all_df[all_df['Duration'].astype('timedelta64[D]') >= 3]['Name'].dropna()))

less_wordcloud = generate_wordcloud(less_text)
grtr_wordcloud = generate_wordcloud(grtr_text)

# display wordclouds using matplotlib
f, axes = plt.subplots(1, 2, sharex=True)
f.set_size_inches(18, 10)
axes[0].imshow(less_wordcloud, interpolation="bilinear")
axes[0].set_title('<3 days', fontsize=36)
axes[0].axis("off")
axes[1].imshow(grtr_wordcloud, interpolation="bilinear")
axes[1].set_title('>=3 days', fontsize=36)
axes[1].axis("off")