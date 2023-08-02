def qda(data):
    term1 = 0.5*np.dot((data-sample_mean_c1).T, np.linalg.inv(sample_cov_c1)).dot(data-sample_mean_c1)
    term2 = 0.5*np.dot((data-sample_mean_c2).T, np.linalg.inv(sample_cov_c2)).dot(data-sample_mean_c2)
    term3 = 0.5*(np.log(np.linalg.norm(sample_cov_c1)))
    term4 = 0.5*(np.log(np.linalg.norm(sample_cov_c2)))
    term5 = np.log(pi_2/pi_1)
    
    result = term1 - term2 + term3 - term4 + term5
    
    return result