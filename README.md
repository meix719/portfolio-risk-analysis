# Portfolio Risk Analysis and Optimization

A Python-based portfolio risk analysis of five assets using 36 monthly observations (January 2019–December 2021). This project evaluates returns, volatility, covariance, risk-adjusted performance, downside exposure, stress scenarios, risk appetite, and Sharpe-ratio optimization.

## Key findings

| Measure | Original portfolio | Optimized portfolio |
|---|---:|---:|
| Average monthly return | 0.59% | 0.67% |
| Monthly volatility | 0.43% | 0.47% |
| Monthly Sharpe ratio | 0.62 | 0.73 |

**Other results:** Historical 95% loss VaR was 0.00% in this small, mostly positive sample; a hypothetical five-percentage-point negative shock reduced average monthly return to -4.41%. The Sharpe-optimized allocation concentrated 75.13% in Assets 4 and 5, highlighting concentration risk.

## Methods

1. Weighted monthly portfolio returns and trend visualization
2. Average return, sample volatility, and covariance-based variance validation
3. Monthly excess return and Sharpe ratio
4. Historical 95% Value at Risk
5. Five-percentage-point downward stress scenario
6. Conservative vs. aggressive allocation scenarios
7. Long-only Sharpe ratio maximization with SciPy SLSQP

See the [full report](report.md) for tables, methods, interpretation, and limitations. A [downloadable Word report](Unit_9_Portfolio_Risk_Analysis.docx) is also available (formatted from the repository report; the original class document is unchanged).

## How to run

1. Download or clone the repository.
2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. The synthetic dataset is already included in [`data/portfolio_returns.csv`](data/portfolio_returns.csv), containing 36 months of returns, weights, and risk-free rates. No separate data download is needed.
4. Run:

   ```bash
   python unit_9_py.py
   ```

The script prints results and saves `Monthly_Portfolio_Returns.png`.

## Data and limitations

The synthetic course dataset is included as a CSV under `data/` so results can be reproduced. The original Excel workbook and instructor notes are not redistributed. Results are an educational, in-sample exercise rather than real-time market estimates or investment advice. The historical 95% VaR estimate is especially limited by the 36-month sample. The stress scenario assumes a uniform fixed shock, and the optimization does not include transaction costs or out-of-sample validation.

## Tools

Python, pandas, NumPy, Matplotlib, SciPy, openpyxl.

**Author:** Mei Qiong Xue
