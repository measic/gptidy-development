df_per_day["client-ip-unique-count-MEAN"] =df_per_day["client-ip-unique-count"].mean()


df_per_day["AE"]=np.abs(
    df_per_day["client-ip-unique-count"]- 
    df_per_day["client-ip-unique-count-MEAN"]
)

print("Mean Absolute Error: ",df_per_day.AE.mean())