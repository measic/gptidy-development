df_per_day = pd.read_csv("../data/log_data_per_day.csv")

df_per_day = df_per_day.sort_values("date").reset_index()

df_per_day.drop(columns=["Unnamed: 0","index"],axis=1,inplace=True)

df_per_day.head()