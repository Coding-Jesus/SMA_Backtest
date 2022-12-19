# Moving Average Cross Strategy
This repository contains a Python script that implements a simple trading strategy based on moving averages and backtests it using historical data.

## Requirements

- Python 3.6 or later
- yfinance library
- ta library
- pandas library
- backtesting library

## Running the code

1. Make sure you have Jupyter installed on your system. You can check if you have Jupyter installed by running the command jupyter --version in your terminal. If you don't have Jupyter installed, you can install it by following the instructions at this link: https://jupyter.org/install.

2. Install the required libraries using pip. For example, to install the yfinance library, run the command pip install yfinance.

3. Open a terminal and navigate to the directory where you want to save the code file.

4. Run the command jupyter notebook to launch the Jupyter Notebook application. This will open a new browser window with the Jupyter dashboard.

5. In the dashboard, click on the 'New' button on the right and select 'Python 3' from the dropdown menu. This will open a new Jupyter notebook in a new tab.

6. The Jupyter notebook consists of cells. Each cell can contain code or text. You can type the code in the first cell of the Jupyter notebook or you can paste the code that you copied from the repository.

7. To run the code, you can either click on the'Run' button in the toolbar or use the keyboard shortcut Shift + Enter. This will execute the code in the current cell and advance to the next cell.

8. Repeat this process until you have run all the cells in the notebook.

## Output
The code will download BTC-USD data from Yahoo Finance, create a Backtest object, run the backtest, optimize the strategy, and plot the results of the optimization.

The output of the backtest includes the performance metrics such as the return, the Sharpe ratio, and the drawdown. The optimization process finds the optimal values of the moving average lengths that maximize the return while satisfying the constraints. The plot shows the performance of the optimized strategy.

## Troubleshooting
If you encounter any issues while running the code, you can check the requirements and make sure that you have all the required libraries installed and that you are using the correct version of Python. If the issue persists, you can try reaching out to the repository owner or the community for help.
