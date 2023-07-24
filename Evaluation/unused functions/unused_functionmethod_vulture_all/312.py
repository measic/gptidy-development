def portfolio_annualised_performance(weights, mean_returns, cov_matrix):
    """This function calculates annualised portfolio returns and volatility (risk).
    
    Parameters
    ----------
      `weights`: randomly generated weights for each stock in a portfolio
      `mean_returns`: mean of stock daily_returns
      `cov_matrix`: coeffecient matrix of all the daily_returns
    
    Returns
    -------
      Both annualised `standard_deviation` and `returns`.
    """
    annual_returns = np.sum(mean_returns * weights) * 252
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix,
                                           weights))) * np.sqrt(252)
    return std, annual_returns


#########################################################################################


def random_portfolio(mean_returns,
                     cov_matrix,
                     num_portfolios=10000,
                     risk_free_rate=0.00):
    """This function generates portfolios with random weights for each stock.
    
    Parameters
    ----------
      `mean_returns`: mean of stock daily_returns
      `cov_matrix`: coeffecient matrix of all daily_returns
      `num_portfolios`: default is `10000` but can be tuned
      `risk_free_rate`: default is `0.00` can vary from 0 through 1
    
    Returns
    -------
      `results` and `weights_record`.
    """

    results = np.zeros((3, num_portfolios))
    weights_record = []
    for i in range(num_portfolios):
        weights = np.random.rand(4)
        weights /= np.sum(weights)
        weights_record.append(weights)

        portfolio_std_dev, portfolio_return = portfolio_annualised_performance(
            weights=weights, mean_returns=mean_returns, cov_matrix=cov_matrix)

        results[0, i] = portfolio_std_dev
        results[1, i] = portfolio_return
        results[2, i] = (portfolio_return - risk_free_rate) / portfolio_std_dev
    return results, weights_record