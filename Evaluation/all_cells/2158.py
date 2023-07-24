# concatenate all name fields from overdue tasks
before_text = ' '.join(list(all_df[all_df['Overdue'].astype('timedelta64[D]') < 0]['Name'].dropna()))
sameday_text = ' '.join(list(all_df[all_df['Overdue'].astype('timedelta64[D]') == 0]['Name'].dropna()))
overdue_text = ' '.join(list(all_df[all_df['Overdue'].astype('timedelta64[D]') > 0]['Name'].dropna()))

before_wordcloud = generate_wordcloud(before_text)
sameday_wordcloud = generate_wordcloud(sameday_text)
overdue_wordcloud = generate_wordcloud(overdue_text)

# display wordclouds using matplotlib
f, axes = plt.subplots(2, 2, sharex=True)
f.set_size_inches(18, 10)
axes[0, 0].imshow(before_wordcloud, interpolation="bilinear")
axes[0, 0].set_title('Completed Before', fontsize=36)
axes[0, 0].axis("off")
axes[0, 1].imshow(sameday_wordcloud, interpolation="bilinear")
axes[0, 1].set_title('Completed Same Day', fontsize=36)
axes[0, 1].axis("off")
axes[1, 0].imshow(overdue_wordcloud, interpolation="bilinear")
axes[1, 0].set_title('Overdue', fontsize=36)
axes[1, 0].axis("off")
axes[1, 1].axis("off")