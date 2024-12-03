# Factor Analysis Tool

## Project Overview
The **Advanced Stock Analysis Tool** evaluates stock performance using key financial factors, such as **Market Influence**, **Firm Size**, **Debt Ratio**, **Price Momentum**, **Turnover Ratio**, **Liquidity Factor**, and **Volatility Factor**. This tool provides both single-factor and multi-factor analysis, offering deep insights into stock behaviors and trends.

## Features
1. **View Historical Closing Prices**:
   - Retrieve and save the historical closing prices of a stock.
2. **Retrieve Detailed Stock Data**:
   - Access comprehensive metrics such as turnover rate, market value, and total debt.
3. **Perform Factor Analysis**:
   - **Single-Factor Analysis**: Choose a specific factor to analyze its relationship with stock performance.
   - **Multi-Factor Analysis**: Combine multiple factors for a holistic analysis.
4. **Exit**:
   - Terminate the program.

## How to Use
### Prerequisites
- Python 3.11 or above.
- Data files (`closeprice.csv`, `volume.csv`, etc.) in the working directory.

### Running the Program
1. Clone this repository:
   ```
   git clone 
   ```
2. Navigate to the project directory:
   ```
   cd FactorAnalysisTool
   ```
3. Install the required packages:
   ```
   pip install pandas numpy statsmodels matplotlib networkx
   ```
4. Run the program:
   ```
   python FactorAnalysisTool.py
   ```

### Example Usage
#### Single Factor Analysis
Run the program and select Option 3 from the menu.
Enter a valid stock symbol (e.g., AMZN.O).
Choose Single-Factor Analysis and select a factor from the list:
Market Influence
Firm Size
Debt Ratio
Price Momentum
Turnover Ratio
Liquidity Factor
Volatility Factor
Multi-Factor Analysis
Select Multi-Factor Analysis from the menu.
Choose multiple factors by entering their corresponding numbers separated by spaces.

#### Multi-Factor Analysis
Select Multi-Factor Analysis from the menu.
Choose multiple factors by entering their corresponding numbers separated by spaces.

## Required Python Packages
- `pandas`
- `numpy`
- `statsmodels`
- `matplotlib`
- `networkx`

Install them using:
```
pip install pandas numpy statsmodels matplotlib networkx
```

## Repository Structure
```
.
├── FactorAnalysisTool.py                 
├── FinancialAnalysisToolkit.py
├── README.md                  
└── Data files (*.csv)         

```

