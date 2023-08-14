# We keep only the rows which mention how much money has been granted (the amount column starts by a number)
# ie : we keep rows where the 'Approved Amount' column starts with a number
p3_grant_export_data = p3_grant_export_data[p3_grant_export_data['Approved Amount'].apply(lambda x : x[0].isdigit())]