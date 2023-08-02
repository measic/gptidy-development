def roc_auc(labels, predictions, thresholds, get_fpr_tpr=True):
    tpr = []
    fpr = []
    for th in thresholds:
        variable_def = tf.where(tf.greater_equal(predictions, th) & tf.equal(labels, 1))
        tp = tf.size(variable_def)
        tn_cases = tf.where(tf.less(predictions, th) & tf.equal(labels, 0))
        tn = tf.size(tn_cases)
        fp_cases = tf.where(tf.greater_equal(predictions, th) & tf.equal(labels, 0))
        fp = tf.size(fp_cases)
        fn_cases = tf.where(tf.less(predictions, th) & tf.equal(labels, 1))
        fn = tf.size(fn_cases)
        tpr_th = tp / (tp + fn)
        fpr_th = fp / (fp + tn)
        tpr.append(tpr_th)
        fpr.append(fpr_th)
    auc_score = 0
    for i in range(0, len(thresholds) - 1):
        height_step = tf.abs(fpr[i + 1] - fpr[i])
        b1 = tpr[i]
        b2 = tpr[i + 1]
        step_area = height_step * (b1 + b2) / 2
        auc_score += step_area
    return (auc_score, fpr, tpr)