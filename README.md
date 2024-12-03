# Factor Analysis Tool

## Project Overview
The Factor Analysis Tool is designed to analyze stock performance using various financial factors, such as Market Factor, Size Factor, Value Factor, Rate of Change (ROC), and Volume Ratio. This tool offers both single-factor and multi-factor analysis, including the Fama-French three-factor model.

## Features
1. Query stock closing price data.
2. Retrieve detailed stock data, including turnover rate, market cap, and liabilities.
3. Perform single or multiple-factor analysis:
   - Single Factor Analysis: Choose one factor for regression analysis.
   - Multi-Factor Analysis: Use Fama-French three-factor model or custom factor combinations.
4. Exit the program.

## How to Use
### Prerequisites
- Python 3.11 or above.
- Data files (`closeprice.csv`, `volume.csv`, etc.) in the working directory.

### Running the Program
1. Clone this repository:
   ```
   git clone <repository_url>
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
1. Select Option `3` in the menu.
2. Enter a valid NASDAQ 100 stock code.
3. Choose `single` analysis and select the desired factor:
   - Market Factor
   - Size Factor
   - Value Factor
   - ROC
   - Volume Ratio

#### Multi-Factor Analysis
1. Select the `Fama-French three-factor model` or `custom factors`.
2. Provide valid factors for analysis.

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
├── FactorAnalysisTool.py      # Main program file
├── DataProcessingUtils.py     # Data preprocessing utilities
├── FactorComputation.py       # Factor calculation functions
├── StatisticalModeling.py     # Statistical analysis and visualization
├── README.md                  # Project instructions
└── Data files (*.csv)         # Required stock data
```

