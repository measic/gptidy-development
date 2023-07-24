# Create Pandas DataFrame for results
pd.DataFrame(data={"date": date_array, "density": density_array, 
                   "frustration_score": frustration_array}).to_csv("ResultCSVs/structbal_quant_%s_res.csv" % (dataset))