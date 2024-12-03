import pandas as pd
import numpy as np
from FinancialAnalysisToolkit import DataProcessor, FactorGenerator, StatisticalModeler


def fetch_stock_data(stock_symbol):
    """Fetch stock data from CSV files."""
    file_paths = {
        'closing_price': 'closeprice.csv',
        'trading_volume': 'volume.csv',
        'turnover_rate': '%turnover.csv',
        'market_value': 'Cap.csv',
        'debt_amount': 'debt.csv'
    }
    data_frames = []

    for key, path in file_paths.items():
        df = pd.read_csv(path, encoding='gbk', low_memory=False, na_values="——")
        if stock_symbol in df.columns:
            data_frames.append(df[[stock_symbol]].rename(columns={stock_symbol: key}))

    return pd.concat(data_frames, axis=1)


def calculate_factors(cleaned_data):
    """Generate all factors for analysis."""
    generator = FactorGenerator(cleaned_data)
    factors = {
        'Market Influence': generator.compute_market_influence(),
        'Firm Size': generator.compute_company_size(),
        'Debt Ratio': generator.compute_financial_strength(),
        'Price Momentum': generator.compute_price_momentum(),
        'Turnover Ratio': generator.compute_turnover_ratio(),
        'Liquidity Factor': generator.compute_liquidity(),
        'Volatility Factor': generator.compute_price_volatility()
    }
    factors_df = pd.DataFrame(factors)
    factors_df['Stock Price'] = cleaned_data['closing_price'].iloc[len(cleaned_data) - len(factors_df):].reset_index(drop=True)
    return factors_df


def main():
    print("Welcome to the Advanced Stock Analysis Tool!")

    while True:
        choice = input(
            "Please choose an option:\n"
            "1. View historical closing prices\n"
            "2. Retrieve detailed stock data\n"
            "3. Analyze stock performance with factors\n"
            "4. Exit the program\n"
            "Your choice: "
        )

        if choice == '1':
            stock_symbol = input("Enter the stock symbol to view closing prices (e.g., AMZN.O): ")
            price_data = fetch_stock_data(stock_symbol)[['closing_price']]
            price_data.to_csv(f"{stock_symbol}_closing_prices.csv")
            print(f"Closing price data saved as {stock_symbol}_closing_prices.csv")

        elif choice == '2':
            stock_symbol = input("Enter the stock symbol to retrieve detailed data (e.g., AMZN.O): ")
            stock_data = fetch_stock_data(stock_symbol)
            stock_data.to_csv(f"{stock_symbol}_details.csv")
            print(f"Detailed stock data saved as {stock_symbol}_details.csv")

        elif choice == '3':
            stock_symbol = input("Enter the stock symbol for factor analysis (e.g., AMZN.O): ")
            raw_data = fetch_stock_data(stock_symbol)

            # Data cleaning
            processor = DataProcessor(raw_data)
            processed_data = processor.remove_empty_columns()
            processed_data = processor.fill_missing()
            processed_data = processor.scale_to_unit_range()

            # Calculate factors
            factors = calculate_factors(processed_data)
            factors.to_csv('calculated_factors.csv')
            print("Calculated factors saved to calculated_factors.csv")

            # Perform analysis
            analysis_type = input(
                "Would you like to perform single-factor or multi-factor analysis? (Enter 'single' or 'multiple'): "
            )

            factor_map = {
                '1': 'Market Influence',
                '2': 'Firm Size',
                '3': 'Debt Ratio',
                '4': 'Price Momentum',
                '5': 'Turnover Ratio',
                '6': 'Liquidity Factor',
                '7': 'Volatility Factor'
            }

            if analysis_type == 'single':
                print("Available factors:")
                for key, value in factor_map.items():
                    print(f"{key}. {value}")
                selected_factor = input("Choose a factor by entering its number: ")
                chosen_factor = factor_map.get(selected_factor)

                if chosen_factor:
                    factors.dropna(inplace=True)
                    factors.replace([np.inf, -np.inf], 0, inplace=True)
                    modeler = StatisticalModeler(factors)
                    results = modeler.run_regression('Stock Price', [chosen_factor])
                    print(results.summary())
                    modeler.plot_factor_importance(results, 'Stock Price')
                else:
                    print("Invalid selection. Please try again.")

            elif analysis_type == 'multiple':
                print("Available factors:")
                for key, value in factor_map.items():
                    print(f"{key}. {value}")
                selected_factors = input("Enter the numbers of the factors you want to analyze, separated by spaces: ").split()
                chosen_factors = [factor_map.get(factor) for factor in selected_factors if factor_map.get(factor)]

                if chosen_factors:
                    factors.dropna(inplace=True)
                    factors.replace([np.inf, -np.inf], 0, inplace=True)
                    modeler = StatisticalModeler(factors)
                    results = modeler.run_regression('Stock Price', chosen_factors)
                    print(results.summary())
                    modeler.plot_factor_importance(results, 'Stock Price')
                else:
                    print("No valid factors selected. Please try again.")

        elif choice == '4':
            print("Thank you for using the Advanced Stock Analysis Tool. Goodbye!")
            break

        else:
            print("Invalid input. Please select a valid option.")


if __name__ == "__main__":
    main()
