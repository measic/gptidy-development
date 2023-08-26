def make_pca(Table,All_Data,n,name='PCA_test',whiten=False):
    pca = PCA(n_components=n,whiten=whiten)
    pca.fit(All_Data[Table.keys()])
    trans_PCA=pca.transform(Table)
    #Saving the components of the PCA
    components=pca.components_
    PCA_table=pandas.DataFrame(components,columns=Table.keys(),index=['%s_%i'%(name,i+1) for i in range(n)])
    PCA_table.to_csv('%s_components.csv'%name)
    #pca.explained_variance_ratio_##pca.get_params()
    #Needs to return the PCA transformation
    return pandas.DataFrame(trans_PCA,columns=['%s_%i'%(name,i+1) for i in range(n)],index=Table.index)
#pandas.concat([Trial_data[Protein[:4]],make_pca(Trial_data[Protein[:4]],Dream9,3),make_pca(Trial_data[Protein[:4]],Dream9,2,'Whiten_PCA',True)],axis=1).T