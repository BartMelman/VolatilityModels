
### Market Description
- The price discovery process of stocks mean that stocks can be mean reverting. 
- In aggregate, stocks increase in value


### Stock Returns
- The returns of stocks are asymmetricly distributed.
- The average stock returns are positive


### Difference between Stocks

Process of continuous incrementing stock returns vs
$$
\begin{aligned}
\textrm{profit 1 day} & = r\\
\textrm{profit n days} & = \lim_{\epsilon \to 0} n \epsilon \\
& = \ln{1+r}
\end{aligned}
$$

*Proof*
$$
\begin{aligned}
(1+\epsilon)^n & = 1 + r\\
n &  = \frac{\ln{1+r}}{\ln{1+\epsilon}}\\
\lim_{\epsilon \to 0} n \epsilon & = \frac{\epsilon \ln{1+r}}{\ln{1+\epsilon}}\\
& = \ln{1+r}
\end{aligned}
$$

Return adjusted profit
$$
\begin{aligned} 
    profit & = \frac{r-\ln{1+r}}{|r|} 
\end{aligned}   
$$

### Hold or rebalance

Hold
$$
profit = r_{t-1} + 
$$


Rebalancing
$$

$$

Ideal stock
- the expected profit based on the volatility should be higher than the volatility (mean reversion)
- compare 1 month ahead vol versus daily vol


Stock algorithm
- Rebalance portfolio with top 100 stocks

$$
\begin{aligned}
    R_t & = \sum_{i=1}^n w_i R_i  \quad \textrm{s.t.} \quad \bm{w}' \iota = 1 
\end{aligned}
$$

