print('Loading case data ...')

#cases_800                    = pd.read_csv("pancancer_case_features_800.csv")
#cases_1000                   = pd.read_csv("pancancer_case_features_1000.csv")
#cases_1500                   = pd.read_csv("pancancer_case_features_1500.csv")
#cases_bestfit_8000           = pd.read_csv("pancancer_case_features_bestfit_8000_topgenes_1000.csv")
cases_bestfit_10000          = pd.read_csv("pancancer_case_features_bestfit_10000_topgenes_2000.csv")
cases_bestfit_15000          = pd.read_csv("pancancer_case_features_bestfit_15000_topgenes_3000.csv")
cases_bestfit_15000_allgenes = pd.read_csv("pancancer_case_features_bestfit_15000_topgenes_None.csv")
cases_allgenes               = pd.read_csv("pancancer_case_features_all.csv")
all_data = {
    #'800':                     getDataAndLabels(cases_800),
    #'1000':                    getDataAndLabels(cases_1000),
    #'1500':                    getDataAndLabels(cases_1500),
    'best_fit_10000':          getDataAndLabels(cases_bestfit_10000),
    'best_fit_15000':          getDataAndLabels(cases_bestfit_15000),
    'best_fit_15000_allgenes': getDataAndLabels(cases_bestfit_15000_allgenes),
    'genes_all':               getDataAndLabels(cases_allgenes)
}
print("done.")