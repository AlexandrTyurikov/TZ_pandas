import pandas as pd


df_AAVE_ETH = pd.read_csv('AAVE_ETH_normalized.csv')
df_WETH_USD = pd.read_csv('WETH_USD.csv')

df_AAVE_USD = pd.DataFrame({
    'time': df_AAVE_ETH['time'],
    'USD price': df_AAVE_ETH['price'] * df_WETH_USD['Average USD price']
})

df_AAVE_USD.to_csv('AAVE_USD.csv')
