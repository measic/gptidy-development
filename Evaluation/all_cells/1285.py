#list containing 'bins' for tuition
quartile_bins = []

#bin_names are given after tuition is binned i.e
#the bin_names are up for change
bins = [0,10000,18000,32000,100000]
bin_names = ["less_10k","10k_18k","18k_32k", "greater_32k"]

#list reference for obtaining min, median, and max tution
tuition_list = region_stats['tuition_in_state']

#obtain 25th percentile, then append to list
twentyfive_Percentile = tuition_list.quantile(0.25)
quartile_bins.append(twentyfive_Percentile)

#obtain 50th percentile, then append to list
fifty_Percentile = tuition_list.quantile(0.50)
quartile_bins.append(fifty_Percentile)

#obtain 75th percentile, then append to list
seventyFive_Percentile = tuition_list.quantile(0.75)
quartile_bins.append(seventyFive_Percentile)

#obtain 100th percentile, then append to list
ninetyNine_Percentile = tuition_list.quantile(1)
quartile_bins.append(ninetyNine_Percentile)

#print bins list
quartile_bins