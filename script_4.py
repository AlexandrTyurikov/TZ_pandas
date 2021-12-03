import pandas as pd


df_USDC = pd.read_csv('WETH_USDC_normalized.csv')
df_USDT = pd.read_csv('WETH_USDT_normalized.csv')

df_USD = pd.DataFrame({
    'date': df_USDC['time'],
    'USDC price': df_USDC['price'],
    'USDT price': df_USDT['price'],
    'Average USD price': (df_USDC['price'] + df_USDT['price']) / 2
})

df_USD.to_csv('WETH_USD.csv')


# res = pd.concat([df_1['price'], df_2['price']], axis=1)