def make_export_table(model):
    kaggle_export = pd.DataFrame({
        'id': test['Id'],
        'SalePrice': preds[model]
    },
    columns = ['id', 'SalePrice'])
    return kaggle_export