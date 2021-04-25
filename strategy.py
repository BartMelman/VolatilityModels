import math

def getProfit(returnLoss, returnGain, transactionReturn = 0):
    # number of days of profit to return to original price
    numProfitDays = math.log(1/(1+returnLoss))/math.log(1+returnGain)

    # profit is (-) loss + profit + (-) transaction costs
    profit = returnLoss + numProfitDays * returnGain + 2 * abs(returnLoss) * transactionReturn

    return profit

import pandas as pd

def getEarnings(ticker, method= 'YahooFinance'):
    # Get a dataframe with earningsdates from yahoofinance
    # Example url : https://finance.yahoo.com/calendar/earnings/?day=2018-04-17&symbol=aapl
    # Return a table (dataframe)
    ticker = ticker.lower()
    if method == 'YahooFinance':
        dfs = pd.read_html('https://finance.yahoo.com/calendar/earnings/?day=2018-04-17&symbol={ticker}')
        earningsDF = dfs[0]
        if 'Symbol' not in earningsDF.columns:
            raise ValueError("Incorrect table selected")
    else:
        raise ValueError("Method not in options", method)

    return earningsDF