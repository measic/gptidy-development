vote_dfs = pd.read_excel(os.path.join(PATH, 'source_data', '20161206_sov.xlsx'), sheetname=None, header=3)

# Since the sheet names get cut off, we can fix them using the Contents tab
contents = vote_dfs['Contents'].copy()
contents.columns = ['key', 'name']
contents = contents.iloc[1:]
contents['key'] = contents['key'].astype(int)
contents = contents.set_index('key').to_dict(orient='index')

fixed_names = {}
for cut_name in vote_dfs:
    if cut_name == 'Contents':
        continue
    key = int(cut_name[:3])
    if key in contents:
        prefix = cut_name[:6]
        postfix = contents[key]['name']
        fixed_names[prefix + postfix] = vote_dfs[cut_name]