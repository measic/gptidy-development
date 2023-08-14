def getDataAndLabels(cases):
    labels_string = cases.cancer_type
    le = preprocessing.LabelEncoder()
    labels = le.fit_transform(labels_string)

    # Get rid of the cancer type and patient_id columns 
    data = cases[cases.columns[3:]]
    return {'data': data, 'labels': labels , 'label_encoder': le }


