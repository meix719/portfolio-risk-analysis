# UNIT 9: PORTFOLIO RISK ANALYSIS

# STEP 1: IMPORT

import pandas as pd
# pd = pandas, a library used to read Excel files and work with data tables.

import numpy as np
# np = NumPy, a library used for mathematical calculations.

import matplotlib.pyplot as plt
# plt = Matplotlib, used to create graphs and charts.


# STEP 2: IMPORT EXCEL DATA

# df = DataFrame, which is a table of rows and columns in Python.
# pd.read_excel() imports my Excel data into Python.
# sheet_name tells Python which Excel worksheet to read.
# The original Excel file is not changed.

df = pd.read_excel(
    "Risk Analytics - Class 9 - Dataset.xlsx",
    sheet_name="Dataset"
)


# STEP 3: EXPLORE THE DATASET

# print() displays information in the terminal.
# .head() shows the first 5 rows of my dataset.

print(df.head())


# .shape shows the number of rows and columns.
# The result is displayed as (rows, columns).

print("Dataset Shape:", df.shape)


# \n creates a new line in the terminal.
# .isnull() checks for missing values.
# .sum() counts the missing values in each column.

print("\nMissing Values:")
print(df.isnull().sum())


# STEP 4: CALCULATE MONTHLY PORTFOLIO RETURNS

# Portfolio Return = Sum of (Asset Return x Asset Weight)

# Each asset has a different return and portfolio weight.
# Multiplying the return by the weight gives the asset's
# contribution to the overall portfolio.

df["Portfolio_Return"] = (
    df["Asset_1_Return"] * df["Weight_Asset_1"] +
    df["Asset_2_Return"] * df["Weight_Asset_2"] +
    df["Asset_3_Return"] * df["Weight_Asset_3"] +
    df["Asset_4_Return"] * df["Weight_Asset_4"] +
    df["Asset_5_Return"] * df["Weight_Asset_5"]
)


# STEP 5: DISPLAY MONTHLY PORTFOLIO RETURNS

# df[["Month", "Portfolio_Return"]] selects only these two columns.
# .to_string() formats the output as text.
# index=False removes the automatic row numbers.
# {:.2%} converts decimals into percentages with 2 decimal places.
# Example: 0.0107 becomes 1.07%.

print("\nMonthly Portfolio Returns:")

print(
    df[["Month", "Portfolio_Return"]]
    .to_string(
        index=False,
        formatters={"Portfolio_Return": "{:.2%}".format}
    )
)

# STEP 6: CREATE A LINE GRAPH OF MONTHLY PORTFOLIO RETURNS

plt.figure(figsize=(12, 6))

# x-axis = Month
# y-axis = Portfolio_Return
plt.plot(df["Month"], df["Portfolio_Return"], marker="o")

# Add title and axis labels
plt.title("Monthly Portfolio Returns (2019–2021)")
plt.xlabel("Month")
plt.ylabel("Portfolio Return")

# Rotate x-axis labels so they are easier to read
plt.xticks(rotation=45)

# Add grid lines to make the chart easier to read
plt.grid(True)

# Adjust spacing so labels don't overlap
plt.tight_layout()

# Save the graph as an image for my report
plt.savefig("Monthly_Portfolio_Returns.png", dpi=300)

# Display the graph
plt.show()


# STEP 7: CALCULATE AVERAGE RETURN AND VOLATILITY

# This tells us how much the portfolio earned per month on average.

average_return = df["Portfolio_Return"].mean()

# .std() calculates standard deviation, also called volatility.
# It measures how much monthly returns fluctuate around the average.
# Higher volatility = greater fluctuations and higher variability in returns.
# Lower volatility = more consistent returns.

portfolio_volatility = df["Portfolio_Return"].std()


# :.3% converts decimals to percentages with 3 decimal places.

print("\nPortfolio Summary Statistics:")
print(f"Average Monthly Return: {average_return:.3%}")
print(f"Monthly Portfolio Volatility: {portfolio_volatility:.3%}")


# STEP 8: CALCULATE PORTFOLIO RISK USING COVARIANCE

# Create a list containing the five asset return columns.
# We only want asset returns, not market returns or weights.

asset_columns = [
    "Asset_1_Return",
    "Asset_2_Return",
    "Asset_3_Return",
    "Asset_4_Return",
    "Asset_5_Return"
]

# Create a list of the five asset weight columns.

weight_columns = [
    "Weight_Asset_1",
    "Weight_Asset_2",
    "Weight_Asset_3",
    "Weight_Asset_4",
    "Weight_Asset_5"
]

# .iloc[0] selects the first row of portfolio weights.
# We use this because our portfolio weights stay constant.
# .to_numpy() converts the weights into a NumPy array.

weights = df[weight_columns].iloc[0].to_numpy(dtype=float)

# .cov() calculates the covariance between every pair of assets.
# The result is a 5-by-5 covariance matrix.

cov_matrix = df[asset_columns].cov()

print("\nAsset Covariance Matrix:")
print(cov_matrix.round(6))

# Calculate portfolio variance using asset weights and covariance.
# @ means matrix multiplication.
# .to_numpy() converts the covariance table into a numerical array.

portfolio_variance = weights @ cov_matrix.to_numpy() @ weights

# np.sqrt() calculates the square root.
# Square root of variance = standard deviation (volatility).

covariance_volatility = np.sqrt(portfolio_variance)

print(f"\nCovariance-Based Portfolio Volatility: {covariance_volatility:.2%}")

# Compare with the standard deviation calculated in Step 7.

print(f"Original Portfolio Volatility: {portfolio_volatility:.2%}")


# STEP 9: CALCULATE SHARPE RATIO

# Sharpe Ratio measures the excess return earned for each unit of portfolio risk.

# .mean() calculates the average monthly risk-free rate.
# We use the average because the rate changes over time.

average_risk_free_rate = df["Risk-Free Rate (%)"].mean()

# Excess return = Portfolio return - Risk-free rate.
# This shows how much more the portfolio earned
# compared to a relatively risk-free investment.

excess_return = average_return - average_risk_free_rate

# Sharpe Ratio = Excess Return / Portfolio Volatility.
# Higher Sharpe Ratios indicate better risk-adjusted returns.

sharpe_ratio = excess_return / portfolio_volatility

# Display the results.
# :.2% formats values as percentages.
# :.2f displays a number with two decimal places.

print("\nSharpe Ratio Analysis:")
print(f"Average Risk-Free Rate: {average_risk_free_rate:.2%}")
print(f"Excess Monthly Return: {excess_return:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")


# STEP 10: CALCULATE HISTORICAL VALUE AT RISK (VaR)

# VaR estimates potential losses at a selected confidence level.
# We use monthly portfolio returns and 95% confidence.

confidence_level = 0.95

tail_probability = 1 - confidence_level

# .quantile() finds a percentile of the dataset.
# A 5th percentile tells us the return threshold
# below which approximately 5% of observations fall.

var_threshold = df["Portfolio_Return"].quantile(tail_probability)

# Convert the return threshold into a nonnegative loss estimate.
# max(0, ...) prevents a positive return from being called a loss.

var_95 = max(0, -var_threshold)

# Count how many months actually had negative returns.
# .sum() counts the True values.

negative_months = (df["Portfolio_Return"] < 0).sum()

print("\nHistorical Value at Risk Analysis:")
print(f"Confidence Level: {confidence_level:.0%}")
print(f"5th Percentile Return: {var_threshold:.2%}")
print(f"Monthly VaR (95%): {var_95:.2%}")
print(f"Months with Negative Returns: {negative_months}")


# STEP 11: PORTFOLIO STRESS TESTING

# Stress testing evaluates portfolio performance
# under unfavorable market conditions.

# Simulate a negative 5-percentage-point shock.
# -0.05 represents a decrease of 5 percentage points.

shock_factor = -0.05

# Apply the shock to all five asset returns.
# asset_columns is the list we created in Step 8.

stressed_returns = df[asset_columns] + shock_factor

# Calculate portfolio returns after the shock.
# .dot(weights) multiplies each asset return by its weight
# and adds the weighted returns together.

df["Stressed_Portfolio_Return"] = stressed_returns.dot(weights)

# Display the first 5 months to compare
# original returns with stressed returns.

print("\nOriginal vs. Stressed Portfolio Returns:")

print(
    df[["Month", "Portfolio_Return", "Stressed_Portfolio_Return"]]
    .head()
    .to_string(
        index=False,
        formatters={
            "Portfolio_Return": "{:.2%}".format,
            "Stressed_Portfolio_Return": "{:.2%}".format
        }
    )
)

# Calculate the average return after the market shock.

stressed_average = df["Stressed_Portfolio_Return"].mean()

# Calculate the volatility after the shock.
# .std() measures the fluctuation in stressed returns.

stressed_volatility = df["Stressed_Portfolio_Return"].std()

# Count how many months have negative stressed returns.

stressed_negative_months = (
    df["Stressed_Portfolio_Return"] < 0
).sum()

# Display the summary results.

print("\nStress Testing Summary:")
print(f"Original Average Return: {average_return:.2%}")
print(f"Stressed Average Return: {stressed_average:.2%}")
print(f"Original Volatility: {portfolio_volatility:.2%}")
print(f"Stressed Volatility: {stressed_volatility:.2%}")
print(f"Negative Months After Stress: {stressed_negative_months}")


# STEP 12: RISK APPETITE TESTING

# Risk appetite measures how much risk an investor is willing to accept to achieve higher returns.
# We will compare three portfolios:
# 1. Original
# 2. Conservative
# 3. Aggressive

# CONSERVATIVE PORTFOLIO
# Allocate more to Assets 3 and 5 because they have relatively low historical volatility.

conservative_weights = np.array([0.10, 0.15, 0.30, 0.10, 0.35])


# AGGRESSIVE PORTFOLIO
# Allocate more to Assets 1 and 4 to seek higher returns,
# while accepting greater fluctuations.

aggressive_weights = np.array([0.30, 0.15, 0.10, 0.35, 0.10])


# Check that the weights add up to 100%.
# np.sum() adds all the weights together.

print("\nPortfolio Weight Checks:")
print(f"Conservative Total: {np.sum(conservative_weights):.0%}")
print(f"Aggressive Total: {np.sum(aggressive_weights):.0%}")


# Calculate monthly returns for both scenarios.
# .dot() multiplies each asset return by its weight
# and adds them together.

df["Conservative_Return"] = df[asset_columns].dot(conservative_weights)

df["Aggressive_Return"] = df[asset_columns].dot(aggressive_weights)


# Calculate the average monthly return using .mean().

conservative_average = df["Conservative_Return"].mean()
aggressive_average = df["Aggressive_Return"].mean()


# Calculate monthly volatility using .std().

conservative_volatility = df["Conservative_Return"].std()
aggressive_volatility = df["Aggressive_Return"].std()


# Compare the average returns and volatility.

print("\nRisk Appetite Testing Results:")

print("\nOriginal Portfolio:")
print(f"Average Return: {average_return:.2%}")
print(f"Volatility: {portfolio_volatility:.2%}")

print("\nConservative Portfolio:")
print(f"Average Return: {conservative_average:.2%}")
print(f"Volatility: {conservative_volatility:.2%}")

print("\nAggressive Portfolio:")
print(f"Average Return: {aggressive_average:.2%}")
print(f"Volatility: {aggressive_volatility:.2%}")


# STEP 13: PORTFOLIO OPTIMIZATION

# Portfolio optimization identifies the asset weights that maximize risk-adjusted returns (Sharpe Ratio).

# Import minimize() from SciPy.
# It finds the weights that minimize a mathematical function.

from scipy.optimize import minimize

# Calculate the average monthly return for each asset.
# .mean() calculates each column's average.

asset_average_returns = df[asset_columns].mean().to_numpy()

# Create a function to calculate the negative Sharpe Ratio.
# def is used to define a function in Python.
# We use a negative value because minimize() finds the minimum,
# while our goal is to MAXIMIZE the Sharpe Ratio.

def negative_sharpe(weights):

    # Calculate the portfolio's weighted average return.
    expected_return = np.dot(weights, asset_average_returns)

    # Calculate volatility using the covariance matrix.
    risk = np.sqrt(weights @ cov_matrix.to_numpy() @ weights)

    # Calculate Sharpe Ratio and make it negative.
    return -(expected_return - average_risk_free_rate) / risk


# Set the constraint that all portfolio weights must total 100%.
# np.sum(weights) - 1 must equal zero.

constraint = {
    "type": "eq",
    "fun": lambda weights: np.sum(weights) - 1
}

# Set each asset weight between 0% and 100%.
# This means we do not allow short selling.

bounds = [(0, 1)] * 5

# Run the optimization.
# weights = original portfolio weights (starting point).
# SLSQP is an optimization method that supports constraints.

optimized_result = minimize(
    negative_sharpe,
    weights,
    method="SLSQP",
    bounds=bounds,
    constraints=constraint
)

# Check whether Python found a solution.

print("\nOptimization Successful:", optimized_result.success)

# Extract the optimized weights.

optimized_weights = optimized_result.x

# Display the new allocation for each asset.
# enumerate() gives each asset a number, starting from 1.

print("\nOptimized Portfolio Weights:")

for i, weight in enumerate(optimized_weights, start=1):
    print(f"Asset {i}: {weight:.2%}")


# Calculate the optimized portfolio's monthly returns.

df["Optimized_Return"] = df[asset_columns].dot(optimized_weights)


# Calculate optimized average return and volatility.

optimized_average = df["Optimized_Return"].mean()
optimized_volatility = df["Optimized_Return"].std()

# Calculate optimized Sharpe Ratio.

optimized_sharpe = (
    optimized_average - average_risk_free_rate
) / optimized_volatility


# Compare original and optimized results.

print("\nPortfolio Optimization Comparison:")

print(f"Original Average Return: {average_return:.2%}")
print(f"Optimized Average Return: {optimized_average:.2%}")

print(f"Original Volatility: {portfolio_volatility:.2%}")
print(f"Optimized Volatility: {optimized_volatility:.2%}")

print(f"Original Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"Optimized Sharpe Ratio: {optimized_sharpe:.2f}")