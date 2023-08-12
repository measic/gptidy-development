# building list out of each value of hotel name
rows = []
def createRow(x):    
    new_list = x.tolist()
    new_list.insert(0,x.name)
    rows.append(new_list)
    
#converting the list to multi-columns data frame
normal_dataFrame.groupby("Hotel Name")["Normal"].transform( createRow )  # group by returns for each hotel a list of his normalized prices
vector = pd.DataFrame.from_records(rows)

# NOTES
# Vector - each row represents a hotel along with his 160 normalized prices
