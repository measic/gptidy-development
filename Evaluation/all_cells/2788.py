with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    
    plt.figure(figsize=(10, 5))
    plt.subplot(121) 
    nx.draw(nx_multi_bbn, with_labels=True, font_weight='bold')
    plt.title('Multi-connected BBN')
    plt.subplot(122) 
    nx.draw(nx_singly_bbn, with_labels=True, font_weight='bold')
    plt.title('Singly-connected BBN')