if msig.sequence_type == 'many2many':
    plot_confusion_matrix(y_true[:, -1], y_pred[:, -1], figsize=(8, 6), filename=os.path.join(msig.out_dir, 'confusion_matrix.png'))
else:
    plot_confusion_matrix(y_true[0], y_pred[0], figsize=(8, 6), filename=os.path.join(msig.out_dir, 'confusion_matrix.png'))