import numpy as np
import scipy.stats as st


def pricesToReturns(prices, returnMethod='relative'):
    if returnMethod == 'absolute':
        returns = prices.diff()
    elif returnMethod == 'relative':
        returns = prices.pct_change()
    elif returnMethod == 'log':
        returns = np.log(1+prices.pct_change())
    else:
        raise ValueError('method not in options', method)

    return returns


def getLikelihood(returns, vol, indices=None):
    zScores = returns / vol
        
    if indices is None:
        zScores = zScores[zScores.notnull()]
    else:
        zScores = zScores.loc[indices]

    likelihood = np.log((st.norm.sf(zScores)/vol.loc[zScores.index])).mean()
    
    return likelihood


class MA():
    def __init__(self, windowSize=10):
        self.windowSize=windowSize

    def fit(self, prices=None):
        return None

    def predict(self, returns):
        vol = returns.pow(2).shift(1).rolling(window=self.windowSize).mean().pow(0.5) 
        return vol

    def getLikelihood(self, returns, indices=None, returnMethod='relative'):
        vol = self.predict(returns)
        likelihood = getLikelihood(returns, vol, indices)
        return likelihood


class EMA():
    def __init__(self, span=10):
        self.span=span

    def fit(self, prices=None):
        return None

    def predict(self, returns):
        vol = returns.pow(2).shift(1).ewm(span=self.span,adjust=False).mean().pow(0.5)
        return vol

    def getLikelihood(self, returns, indices=None, returnMethod='relative'):
        vol = self.predict(returns)
        likelihood = getLikelihood(returns, vol, indices)
        return likelihood
        
