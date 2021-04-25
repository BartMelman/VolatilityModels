

### ARCH

$$
y_t = \epsilon_t \\
\epsilon_t = \sigma_t z_t \\
z_t \sim N(0,1) \\
\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 
$$

$$
\begin{align*}
    y_t & = \epsilon_t \\
    \epsilon_t & = \sigma_t z_t \\
    z_t & \sim N(0,1) \\
    \sigma_t^2 & = \omega + \alpha \epsilon_{t-1}^2 
\end{align*}
$$

$$
\begin{align*}
    p(y) & = \prod_{t=1}^T \frac{1}{\sqrt{2\pi}\sigma_t} e^{-\frac{1}{2} \frac{y_t^2}{\sigma_t^2}} \\
    \log{p(y)} & = \sum_{t=1}^T -\frac{1}{2} \log{2\pi} - \log{\sigma_t} - \frac{1}{2}\frac{y_t^2}{\sigma_t^2} \\
\end{align*}
$$