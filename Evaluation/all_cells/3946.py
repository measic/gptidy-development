def portfolio_optimization_random_ef(mean_returns,
                                     cov_matrix,
                                     num_portfolios=10000,
                                     risk_free_rate=0.00):
    """This function plots the random simulation of efficient frontier.
    
    Parameters
    ----------
      `mean_returns`: mean of stock daily_returns
      `cov_matrix`: coeffecient matrix of all daily_returns
      `num_portfolios`: default is `10000` but can be tuned
      `risk_free_rate`: default is `0.00` can vary from 0 through 1
    
    Prints
    ------
      Prints the summary of `portfolio` and `sharpe` results.
    
    Plots
    -----
      The simulation which is generated at random.
    """
    results, weights = random_portfolio(
        mean_returns=mean_returns,
        cov_matrix=cov_matrix,
        num_portfolios=25000,
        risk_free_rate=0.0178)

    max_sharpe_id = np.argmax(results[2])
    std, ret = results[0, max_sharpe_id], results[1, max_sharpe_id]
    max_sharpe_allocation = pd.DataFrame(
        weights[max_sharpe_id],
        index=dataframe.columns,
        columns=['allocation'])
    max_sharpe_allocation['allocation'] = max_sharpe_allocation[
        'allocation'].apply(lambda x: round(x * 100, 2))
    max_sharpe_allocation = max_sharpe_allocation.T

    min_sharpe_id = np.argmin(results[2])
    std_min, ret_min = results[0, min_sharpe_id], results[1, min_sharpe_id]
    min_sharpe_allocation = pd.DataFrame(
        weights[min_sharpe_id],
        index=dataframe.columns,
        columns=['allocation'])
    min_sharpe_allocation['allocation'] = min_sharpe_allocation[
        'allocation'].apply(lambda x: round(x * 100, 2))
    min_sharpe_allocation = min_sharpe_allocation.T

    print('-' * 70)
    print("  Maximum Sharpe ratio Portfolio Allocation\n")
    print("    Annualised Return : {:.3f}".format(ret))
    print("    Annualised Volatility : {:.3f}".format(std))
    display.display(max_sharpe_allocation)
    print('-' * 70)
    print("  Minimum Sharpe ratio Portfolio Allocation\n")
    print("    Annualised Return : {:.3f}".format(ret_min))
    print("    Annualised Volatility : {:.3f}".format(std_min))
    display.display(min_sharpe_allocation)
    print('-' * 70)

    plt.figure(figsize=(15, 7))
    plt.scatter(
        results[0, :],
        results[1, :],
        c=results[2, :],
        cmap='Set1_r',
        s=10,
        alpha=0.3)
    plt.colorbar()
    plt.scatter(std, ret, marker='*', s=300, c='g', label='Max Sharpe ratio')
    plt.scatter(
        std_min, ret_min, marker='*', s=300, c='r', label='Min Sharpe ratio')
    plt.title('Portfolio Optimization Random Efficient Frontier')
    plt.xlabel('Annualised Volatility')
    plt.ylabel('Annualised Returns')
    plt.legend()
    plt.show()


portfolio_optimization_random_ef(
    mean_returns=mean_returns,
    cov_matrix=cov_matrix,
    num_portfolios=25000,
    risk_free_rate=0.0178)