import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import networkx as nx


class DataProcessor:
    """Cleans and preprocesses stock data."""

    def __init__(self, dataframe):
        self.data = dataframe

    def remove_empty_columns(self):
        """Remove columns with all-zero values."""
        self.data = self.data.loc[:, (self.data.sum(axis=0) != 0)]
        return self.data

    def fill_missing(self):
        """Fill missing values using forward and backward fill."""
        self.data.ffill(inplace=True)
        self.data.bfill(inplace=True)
        return self.data

    def scale_to_unit_range(self):
        """Normalize numeric columns to a 0-1 range."""
        for column in self.data.select_dtypes(include=[np.number]).columns:
            self.data[column] = (self.data[column] - self.data[column].min()) / \
                                (self.data[column].max() - self.data[column].min())
        return self.data


class FactorGenerator:
    """Calculates financial factors from stock data."""

    def __init__(self, dataframe):
        self.data = dataframe

    def compute_market_influence(self):
        """Calculate the market influence factor."""
        return self.data['market_value'] * self.data['closing_price'].pct_change()

    def compute_company_size(self):
        """Calculate firm size based on market value."""
        return self.data['market_value']

    def compute_financial_strength(self):
        """Calculate debt ratio."""
        debt = self.data['debt_amount']
        financial_strength = self.data['market_value'] / debt.replace(0, np.nan)
        return financial_strength.replace([np.inf, -np.inf], np.nan).fillna(0)

    def compute_price_momentum(self):
        """Calculate price momentum as percentage change."""
        momentum = self.data['closing_price'].pct_change() * 100
        return momentum.replace([np.inf, -np.inf], np.nan).fillna(0)

    def compute_turnover_ratio(self):
        """Calculate turnover ratio."""
        turnover_ratio = self.data['trading_volume'] / self.data['trading_volume'].shift(1)
        return turnover_ratio.replace([np.inf, -np.inf], np.nan).fillna(0)

    def compute_liquidity(self):
        """Calculate liquidity as volume-to-market-value ratio."""
        liquidity = self.data['trading_volume'] / self.data['market_value']
        return liquidity.replace([np.inf, -np.inf], np.nan).fillna(0)

    def compute_price_volatility(self, window=10):
        """Calculate price volatility over a rolling window."""
        volatility = self.data['closing_price'].rolling(window=window).std()
        return volatility.replace([np.inf, -np.inf], np.nan).fillna(0)


class StatisticalModeler:
    """Performs statistical analysis and visualizations."""

    def __init__(self, data):
        self.data = data

    def run_regression(self, dependent_var, independent_vars):
        """Run linear regression."""
        X = sm.add_constant(self.data[independent_vars])
        y = self.data[dependent_var]
        model = sm.OLS(y, X)
        return model.fit()

    def plot_factor_importance(self, results, dependent_var):
        """Visualize factor significance with a directed graph."""
        effects = pd.DataFrame({
            'Coefficient': results.params,
            'P-Value': results.pvalues,
            'R-Squared': results.rsquared
        })

        G = nx.DiGraph()
        G.add_node(dependent_var, color='blue')

        for factor in effects.index:
            if factor != 'const':
                G.add_node(factor, color='red')
                width = 2 if effects.loc[factor, 'P-Value'] < 0.05 else 1
                G.add_edge(factor, dependent_var, weight=width)

        pos = nx.spring_layout(G)
        colors = [G.nodes[n]['color'] for n in G.nodes]
        weights = [G[u][v]['weight'] for u, v in G.edges]
        nx.draw(G, pos, with_labels=True, node_color=colors, width=weights, edge_color='black')
        plt.title("Factor Relationships")
        plt.show()
