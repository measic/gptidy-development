def roc_auc(labels, predictions, thresholds, get_fpr_tpr=True):
    tpr = []
    fpr = []
    for th in thresholds:    
        # Compute number of true positives
        tp_cases = tf.where((tf.greater_equal(predictions, th)) & 
                            (tf.equal(labels, 1)))
        tp = tf.size(tp_cases)
        
        # Compute number of true negatives
        tn_cases = tf.where((tf.less(predictions, th)) & 
                            (tf.equal(labels, 0)))
        tn = tf.size(tn_cases)
        
        # Compute number of false positives
        fp_cases = tf.where((tf.greater_equal(predictions, th)) & 
                            (tf.equal(labels,0)))
        fp = tf.size(fp_cases)
        
        # Compute number of false negatives
        fn_cases = tf.where((tf.less(predictions, th)) & 
                            (tf.equal(labels,1)))
        fn = tf.size(fn_cases)
        
        # Compute True Positive Rate for this threshold
        tpr_th = tp/(tp + fn)
        
        # Compute the False Positive Rate for this threshold
        fpr_th = fp/(fp + tn)
        
        # Append to the entire True Positive Rate list
        tpr.append(tpr_th)
        
        # Append to the entire False Positive Rate list
        fpr.append(fpr_th)
        
    # Approximate area under the curve using Riemann sums and the trapezoidal rule
    auc_score = 0
    for i in range(0, len(thresholds)-1):
        height_step = tf.abs(fpr[i+1]-fpr[i])
        b1 = tpr[i]
        b2 = tpr[i+1]
        step_area = height_step*(b1+b2)/2
        auc_score += step_area
    return auc_score, fpr, tpr