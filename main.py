# Import required libraries
import yfinance as yf
import ta
import pandas as pd
from backtesting import Backtest, Strategy

# Import the crossover function from the lib module
from backtesting.lib import crossover 

# Define a strategy class that inherits from the base Strategy class
class SMAcross(Strategy):
    # Define two class variables for the length of the two moving averages
    n1 = 50
    n2 = 100

    # Define the init method to initialize the strategy
    def init(self):
        # Get the close prices from the data
        close = self.data.Close
        
        # Calculate the first moving average using the ta library's sma_indicator function
        self.sma1 = self.I(ta.trend.sma_indicator, pd.Series(close), self.n1)
        
        # Calculate the second moving average using the ta library's sma_indicator function
        self.sma2 = self.I(ta.trend.sma_indicator, pd.Series(close), self.n2)

    # Define the next method to execute trades based on the strategy logic
    def next(self):
        # Check if the first moving average crosses over the second moving average
        if crossover(self.sma1, self.sma2):
            # If it does, buy
            self.buy()
        # If the second moving average crosses over the first moving average
        elif crossover(self.sma2, self.sma1):
            # Sell
            self.sell()

# Download BTC-USD data from Yahoo Finance using the yfinance library
df = yf.download('BTC-USD')

# Create a Backtest object, passing in the data and the strategy
bt = Backtest(df, SMAcross, cash=100000, commission=0.002, exclusive_orders=True)

# Run the backtest
output = bt.run()

# Print the output
output

# Optimize the strategy using the backtest's optimize method
optim = bt.optimize(n1 = range(50, 160,10),
                               n2 = range(50,160,10),
                               constraint= lambda x: x.n2 - x.n1 > 20,
                               maximize= 'Return [%]')

# Plot the results of the optimization
bt.plot()

# Print optimized results 
optim