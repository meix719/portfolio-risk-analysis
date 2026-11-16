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

See [full report](report.md) for tables, methods, interpretation, and limitations.

## How to run

1. Download or clone the repository.
2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Place an **authorized copy** of the course workbook named `Risk Analytics - Class 9 - Dataset.xlsx` alongside `unit_9_py.py`. It must include a worksheet named `Dataset` with these columns: `Month`, `Asset_1_Return` through `Asset_5_Return`, `Weight_Asset_1` through `Weight_Asset_5`, and `Risk-Free Rate (%)`.
4. Run:

   ```bash
   python unit_9_py.py
   ```

The script prints results and saves `Monthly_Portfolio_Returns.png`.

## Data and limitations

The underlying Excel dataset was supplied for coursework and is **not redistributed** in this public repository. Results are an educational, in-sample exercise rather than real-time market estimates or investment advice. The historical 95% VaR estimate is especially limited by the 36-month sample. The stress scenario assumes a uniform fixed shock, and the optimization does not include transaction costs or out-of-sample validation.

## Tools

Python, pandas, NumPy, Matplotlib, SciPy, openpyxl.

**Author:** Mei Qiong Xue
