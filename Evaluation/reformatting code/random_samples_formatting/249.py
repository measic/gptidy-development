def prepare_analysis(df):
    
    acc_2 = pd.DataFrame(np.transpose(df))

    acc_2.columns = ['Acc_train','Beta', 'Learning_Rate', 'Learning_Decay', 'Acc_valid']
    acc_2['Group'] = acc_2['Beta'] + acc_2['Learning_Rate'] + acc_2['Learning_Decay']
    
    return acc_2

acc = prepare_analysis(all_acc)
acc['counter'] = acc.groupby(['Beta','Learning_Rate','Learning_Decay']).cumcount()+1
acc = acc.sort_values(['Beta', 'Learning_Rate', 'Learning_Decay', 'counter'])
