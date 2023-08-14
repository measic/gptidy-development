pop_df = pd.read_excel(os.path.join(PATH, 'source_data', '2010_Pop_Block_County.xls'), sheetname='San Francisco County', header=4)

pop_df = pd.read_excel(os.path.join(PATH, 'source_data', '2010_Pop_Block_County.xls'), sheetname='San Francisco County', header=4)
pop_df = pop_df.drop('BLOCKS', axis='index').reset_index()
pop_df = pop_df.rename(columns={'index': 'block_str'})

records = []
for ix, row in pop_df.iterrows():
    splits = row['block_str'].split(', ')
    record = row[[x for x in row.index if x != 'block_str']].to_dict()
    record['block'] = str(splits[0].split('Block ')[-1])
    record['block_group'] = str(splits[1].split('Block Group ')[-1])
    census_tract = '0' + str(splits[2].split('Census Tract ')[-1].replace('.', ''))
    census_tract += '0' * (6-len(census_tract))  # Even if it doesn't have a decimal part, needs to be 6 characters
    record['census_tract'] = census_tract
    records.append(record)
pop_df = pd.DataFrame(records)

pop_df.columns = [to_appropriate_column_name(x) for x in pop_df.columns]
str_columns = ['block', 'block_group', 'census_tract']
nonstr_columns = [x for x in pop_df.columns if x not in str_columns]
pop_df.loc[:, nonstr_columns] = pop_df[nonstr_columns].astype(int)
pop_df = pop_df[str_columns + nonstr_columns]
pop_df.to_csv(os.path.join(PATH, 'derived_data', 'SF_2010_pop_block.csv'))
pop_df.head()