# # Store school id, name, regions, etc. in list

# school_ids_list = []
# schools_list = []
# regions_list = []
# school_ids_list = []
# tuition_in_state_list = []
# tuition_out_state_list = []
# list_earnings_10_yrs_after_entry = []
# list_earnings_6_yrs_after_entry = []

# for page in range (0,105):
#     search_url = f'{url}{search}&page={page}&api_key={api_key}'
#     response = requests.get(search_url)
#     response_json = response.json()
       
#     for num in range(0,20):
#         school_id = response_json['results'][num]['id']
#         school_ids_list.append(school_id)
#         school_name = response_json['results'][num]['school.name']
#         schools_list.append(school_name)  
#         region_id = response_json['results'][num]['school.region_id']
#         regions_list.append(region_id)              
#         tuition_in = response_json['results'][num]['latest.cost.tuition.in_state']
#         tuition_in_state_list.append(tuition_in)  
#         tuition_out = response_json['results'][num]['latest.cost.tuition.out_of_state']
#         tuition_out_state_list.append(tuition_out)
#         earnings_10yrs_after = response_json['results'][num]['latest.earnings.10_yrs_after_entry.median']
#         earnings_6yrs_after = response_json['results'][num]['latest.earnings.6_yrs_after_entry.median']
#         list_earnings_10_yrs_after_entry.append(earnings_10yrs_after)
#         list_earnings_6_yrs_after_entry.append(earnings_6yrs_after)

# # set up school info in dataframe and export to CSV 
# schoolinfo_df = pd.DataFrame({
#     "school_id": school_ids_list,
#     "school": schools_list,
#     "region": regions_list,
#     "tuition_in_state": tuition_in_state_list,
#     "tuition_out_state": tuition_out_state_list,
#     "earnings6years": list_earnings_6_yrs_after_entry,
#     "earnings10years": list_earnings_10_yrs_after_entry,
# })

# schoolinfo_df.to_csv("cost_earnings_stat_final.csv", index=False, header=True)


                
            
